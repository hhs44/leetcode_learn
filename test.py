#!/usr/bin/python3
import sys
from datetime import datetime


def is_leap(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def get_days(year, month):
    days = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = days[month]
    return total + 1 if month == 2 and is_leap(year) else total


def main():
    if len(sys.argv) == 3:
        month, year = map(int, sys.argv[1:])
    else:
        curr_date = datetime.now()
        year, month = curr_date.year, curr_date.month
    y, m = (year, month) if month > 2 else (year - 1, month + 12)
    c, y = y // 100, y % 100
    w = y + y // 4 + c // 4 - 2 * c + 26 * (m + 1) // 10
    w %= 7

    month_names = ['', 'January', 'Feburary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                   'November', 'December']
    print(f'{month_names[month]} {year}'.center(20))
    print('Su Mo Tu We Th Fr Sa')
    print('  ' * w * 3, end='')
    days = get_days(year, month)
    for day in range(1, days + 1):
        print(f'{day}'.rjust(2), end=' ')
        w += 1
        if w == 7:
            w = 0
            print()
    print()


if __name__ == "__main__":
    main()
