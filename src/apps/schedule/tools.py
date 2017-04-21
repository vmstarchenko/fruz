
PERIODS_ENDS = [(10, 20), (11, 50), (13, 30), (15, 00), (16, 30), (17, 30), ]
VERBOSE_PERIODS = {
    1: 'Первая пара (9:00 - 10:20)',
    2: 'Вторая пара (10:30 - 11:50)',
    3: 'Третья пара (12:10 - 13:30)',
    4: 'Четвертая пара (13:40 - 15:00)',
    5: 'Пятая пара (15:10 - 16:30)',
    6: 'Шестая пара (16:40 - 17:30)',
}


def detect_time(time):
    hour, minute = time.hour, time.minute

    i = 1
    for p_hour, p_minute in PERIODS_ENDS:
        if hour <= p_hour:
            if minute <= p_minute:
                break
        i += 1
    return i
