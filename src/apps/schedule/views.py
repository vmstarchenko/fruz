import datetime
import json
from collections import defaultdict as DDict

from django.shortcuts import render, HttpResponse

from .models import Period
from .tools import (
    VERBOSE_PERIODS, detect_time, load_new_audiences, update_periods_database)


def show_audiences(request):
    periods = DDict(lambda: DDict(list))

    for period in Period.objects.all():
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
        'now': detect_time(datetime.datetime.today())
        'debug': 
    }
    return render(request, 'schedule/show_audience.html', context)


def update_periods(request):
    result = update_periods_database(load_new_audiences())
    # exmp = [{'auditorium': '318',
    #       'beginLesson': '08:00',
    #       'building': 'Н.Н., Львовская, 1в', }, ]
    # result = update_periods_database(exmp)
    return HttpResponse(json.dumps(result), content_type='application/json')
