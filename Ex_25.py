DAY_SEC = 86400
HOUR_SEC = 3600
MIN_SEC = 60
second = int(input("Введите количество секунд: "))
day = second / DAY_SEC
second = second % DAY_SEC
hour = second / HOUR_SEC
second = second % HOUR_SEC
minute = second / MIN_SEC
second = second % MIN_SEC
print('Количество D:HH:MM:SS' ' %d:%02d:%02d:%02d' % (day, hour, minute, second))