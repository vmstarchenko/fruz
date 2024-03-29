import datetime
import json
from collections import defaultdict as DDict

from django.shortcuts import render, HttpResponse

from .models import Period, DataConfig
from .tools import (
    VERBOSE_PERIODS, detect_time, load_new_audiences, update_periods_database)


def show_audiences(request):
    today = datetime.datetime.today()
    data_config = DataConfig.get_solo()
    last_update = data_config.last_update
    was_updated = False
    if (last_update.year != today.year or
            last_update.month != today.month or
            last_update.day != today.day):
        was_updated = True
        results = update_periods_database()
        all_periods = results['new_periods']
        data_config.save()
    else:
        all_periods = Period.objects.all()

    periods = DDict(lambda: DDict(list))

    for period in all_periods:
        periods[period.time][period.floor].append(period)

    # order audiences and floors
    ordered_periods = []  # [(time, (floor, audiences))]
    for time, floor in periods.items():
        floor = [(floor_number, ', '.join(sorted(audience.title for audience in audiences)))
                 for floor_number, audiences in floor.items()]
        floor.sort()
        ordered_periods.append(
            [time, VERBOSE_PERIODS.get(time, 'UNKNOWN TIME'), floor])
    ordered_periods.sort()

    context = {
        'periods': ordered_periods,
        'now': detect_time(today),
        'today': today,
        'was_updated': was_updated,
    }
    return render(request, 'schedule/show_audience.html', context)


def update_periods(request):
    result = update_periods_database(load_new_audiences())
    return HttpResponse(json.dumps(result), content_type='application/json')
