import json
import itertools
import re
import datetime

from urllib.request import Request, urlopen
from urllib.parse import urlencode

from .models import Audience, Period

PERIODS_ENDS = [(10, 20), (11, 50), (13, 30),
                (15, 00), (16, 30), (18, 00),
                (19, 30), (21, 00), ]

PERIODS_NUMBER = len(PERIODS_ENDS)

VERBOSE_PERIODS = {
    0: 'Первая пара (9:00 - 10:20)',
    1: 'Вторая пара (10:30 - 11:50)',
    2: 'Третья пара (12:10 - 13:30)',
    3: 'Четвертая пара (13:40 - 15:00)',
    4: 'Пятая пара (15:10 - 16:30)',
    5: 'Шестая пара (16:40 - 18:00)',
    6: 'Седьмая пара (18:10 - 19:30)',
    7: 'Восьмая пара (19:40 - 21:00)',
}

RE_NUMBER = re.compile('^')


def detect_time(time):
    hour, minute = time.hour, time.minute

    i = 0
    for p_hour, p_minute in PERIODS_ENDS:
        if hour <= p_hour:
            if minute <= p_minute:
                break
        i += 1
    return i

# update database functions


def get_available_audiences():
    return set(audience.title for audience in Audience.objects.all())


def load_new_audiences():
    try:
        today = datetime.datetime.today()

        today_date = '%04d.%02d.%02d' % (today.year, today.month, today.day)

        req = Request('http://ruz.hse.ru/RUZService.svc/lessons?%s' % (
            urlencode({'fromdate': today_date, 'todate': today_date})
        ))
        req.add_header(
            'User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0')

        resp = urlopen(req)
        content = resp.read()

        return json.loads(content.decode())
        # with open('../../trying/lessons.json') as f:  # TODO: fix
        #     return json.loads(f.read())
    except:
        print('Error')  # TODO: fix
        return []


def lesson_begin_to_number(begin):
    return {'09:00': 0, '10:30': 1, '12:10': 2,
            '13:40': 3, '15:10': 4, '16:40': 5,
            '18:10': 6, '19:40': 7, }.get(begin, None)


def update_periods_database(new_audiences):
    available_audiences = get_available_audiences()
    new_audiences = list(filter(
        lambda data: 'Кочновский' in data.get('building', ''),
        new_audiences))

    busy_audiences = set()
    for lesson in new_audiences:
        busy_audiences.add(
            (lesson['auditorium'].strip(),
             lesson_begin_to_number(lesson['beginLesson'])))

    all_audiences = set(lesson for lesson in itertools.product(
        available_audiences, range(PERIODS_NUMBER)))
    free_audiences = all_audiences - busy_audiences

    new_periods = []
    for audience in free_audiences:
        new_periods.append(Period(
            title=audience[0],
            floor=parse_floor(audience[0]),
            time=audience[1]))

    Period.objects.all().delete()
    Period.objects.bulk_create(new_periods)


def parse_floor(floor):
    return int(floor) // 100
