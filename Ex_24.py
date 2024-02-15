DAY_SEC = 86400
HOUR_SEC = 3600
MIN_SEC = 60
day = int(input('Введите количество дней: '))
hour = int(input('Введите количество часов: '))
minute = int(input('Введите количество минут: '))
second = int(input('Введите количество секунд: '))
count_day = day * DAY_SEC
count_hour = hour * HOUR_SEC
count_minute = minute * MIN_SEC
total_second = count_day + count_hour + count_minute + second
print('Количество секунд: ', total_second)