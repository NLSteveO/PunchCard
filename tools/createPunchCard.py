import argparse
from datetime import datetime, timedelta
from enum import Enum

class Weekday(Enum):
    MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY = range(7)

def printPunchCard():
    tab = '  '
    fridayDate = getFridayDate()
    title = f'Week ending on {fridayDate.strftime("%m/%d/%y")}'
    print(title)

def getFridayDate():
    today = datetime.today().date()
    weekday = today.weekday()
    if weekday is Weekday.FRIDAY:
        return today
    elif (weekday in [Weekday.SATURDAY, Weekday.SUNDAY]):
        return today + timedelta(7 - (weekday % 4))
    else:
        return today + timedelta(4 - weekday)

def main():
    printPunchCard()

if __name__ == '__main__': # pragma: no cover
    description = 'This is a script to create a PunchCard interactively.'
    parser = argparse.ArgumentParser(description=description)

    args = parser.parse_args()
    main()
