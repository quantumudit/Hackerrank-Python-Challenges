import calendar

month, day, year = map(int, input().split())

weekday_num = calendar.weekday(year, month, day)
day_name = calendar.day_name[weekday_num].upper()

print(day_name)
