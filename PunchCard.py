import argparse
import re
import sys
import toml
from datetime import timedelta


def calcWorkTime(timeIn, timeOut):
    if timeIn.hour > timeOut.hour:
        timeOut.replace(timeOut.hour + 12)

    deltaIn = timedelta(hours=timeIn.hour, minutes=timeIn.minute)
    deltaOut = timedelta(hours=timeOut.hour, minutes=timeOut.minute)
    timeDifference = deltaOut - deltaIn
    print(timeDifference)

    return timeDifference


def calculateDay(dayEntry, projects):
    dayHours = {'total': timedelta()}
    errors = {}
    for project in projects:
        if project not in dayEntry or not dayEntry[project]:
            continue
        if not validDay(dayEntry[project]):
            errors[project] = '{}: Invalid number of time punches'.format(project)
            continue
        index = 0
        dayHours[project] = timedelta()
        while(index < len(dayEntry[project])):
            dayHours[project] += calcWorkTime(dayEntry[project][index], dayEntry[project][index+1])
            index += 2
        dayHours['total'] += dayHours[project]
        print(dayHours[project])
    return (dayHours, errors)


def calculateWeek(weekEntry, projects, daysOfTheWeek):
    weekHours = {'total': 0.0}

    for project in projects:
        weekHours[project] = 0.0

    for day in daysOfTheWeek:
        if day not in weekEntry or not weekEntry[day]:
            continue
        weekHours['total'] += weekEntry[day]['total']
        for project in projects:
            if project not in weekEntry[day] or not weekEntry[day][project]:
                continue
            weekHours[project] += weekEntry[day][project]
    return weekHours


def printDaysHours(day, dayHours, timeFormat, projects, errors):
    floatTotalHours = round(dayHours['total'], 3)
    intTotalHours = int(floatTotalHours)
    intTotalMinutes = int((floatTotalHours - intTotalHours)*60)
    dayHoursOutput = ''
    if timeFormat == 'HH.hhh':
        dayHoursOutput = '{}\n{}: {} hours'.format(dayHoursOutput, day, floatTotalHours)
    elif timeFormat == 'HH:mm':
        dayHoursOutput = '{}\n{}: {} hours {} minutes'.format(dayHoursOutput, day, intTotalHours, intTotalMinutes)
    else:
        dayHoursOutput = (
            '{}\n{}: {} hours {} minutes({} hours)'.format(dayHoursOutput, day, intTotalHours, intTotalMinutes, floatTotalHours)
        )
    for project in projects:
        if project not in dayHours:
            if project in errors:
                dayHoursOutput = '{}\n\t{}'.format(dayHoursOutput, errors[project])
            continue  # pragma: no cover because https://bitbucket.org/ned/coveragepy/issues/198/continue-marked-as-not-covered
        floatHours = round(dayHours[project], 3)
        intHours = int(floatHours)
        intMinutes = int((floatHours - intHours)*60)
        if project in errors:
            dayHoursOutput = '{}\n\t{}'.format(dayHoursOutput, errors[project])
        if timeFormat == 'HH.hhh':
            dayHoursOutput = '{}\n\t{}: {} hours'.format(dayHoursOutput, project, floatHours)
        elif timeFormat == 'HH:mm':
            dayHoursOutput = '{}\n\t{}: {} hours {} minutes'.format(dayHoursOutput, project, intHours, intMinutes)
        else:
            dayHoursOutput = (
                '{}\n\t{}: {} hours {} minutes({} hours)'.format(dayHoursOutput, project, intHours, intMinutes, floatHours)
            )

    return dayHoursOutput


def printWeekHours(weekHours, timeFormat, projects):
    floatTotalHours = round(weekHours['total'], 3)
    intTotalHours = int(floatTotalHours)
    intTotalMinutes = int((floatTotalHours - intTotalHours)*60)
    weekHoursOutput = ''
    if timeFormat == 'HH.hhh':
        weekHoursOutput = '{}\nTotal hours for the week: {} hours'.format(weekHoursOutput, floatTotalHours)
    elif timeFormat == 'HH:mm':
        weekHoursOutput = (
            '{}\nTotal hours for the week: {} hours {} minutes'.format(weekHoursOutput, intTotalHours, intTotalMinutes)
        )
    else:
        weekHoursOutput = '{}\nTotal hours for the week: {} hours {} minutes({} hours)'.format(
            weekHoursOutput, intTotalHours, intTotalMinutes, floatTotalHours
        )
    for project in projects:
        if project not in weekHours or not weekHours[project]:
            continue  # pragma: no cover because https://bitbucket.org/ned/coveragepy/issues/198/continue-marked-as-not-covered
        floatHours = round(weekHours[project], 3)
        intHours = int(floatHours)
        intMinutes = int((floatHours - intHours)*60)
        if timeFormat == 'HH.hhh':
            weekHoursOutput = '{}\n\t{}: {} hours'.format(weekHoursOutput, project, floatHours)
        elif timeFormat == 'HH:mm':
            weekHoursOutput = '{}\n\t{}: {} hours {} minutes'.format(weekHoursOutput, project, intHours, intMinutes)
        else:
            weekHoursOutput = (
                '{}\n\t{}: {} hours {} minutes({} hours)'.format(weekHoursOutput, project, intHours, intMinutes, floatHours)
            )

    return weekHoursOutput


def validDay(day):
    return len(day) % 2 == 0


# def validTime(time):
#     if time is None:
#         return False
#     pattern = re.compile('^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$')
#     return pattern.match(time)


def main(config, timeFormat):
    daysOfTheWeek = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
    projects = config['day']['projects']
    week = {'total': 0.0}
    punchCardOutput = '{}{}'.format(config['title'], '\n')
    for day in daysOfTheWeek:
        if day not in config['day'] or not config['day'][day]:
            punchCardOutput = (
                '{}{}'.format(punchCardOutput, printDaysHours(day.capitalize(), {'total': 0.0}, timeFormat, projects, ''))
            )
            continue
        dayHours = calculateDay(config['day'][day], projects)
        punchCardOutput = (
            '{}{}'.format(punchCardOutput, printDaysHours(day.capitalize(), dayHours[0], timeFormat, projects, dayHours[1]))
        )
        week[day] = dayHours[0]

    weekHours = calculateWeek(week, projects, daysOfTheWeek)
    return '{}{}{}'.format(punchCardOutput, '\n', printWeekHours(weekHours, timeFormat, projects))


if __name__ == '__main__':  # pragma: no cover
    description = 'This is a simple program meant to calculate my work hours.'
    parser = argparse.ArgumentParser(description=description)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-H', '--hours', action='store_true', help='Outputs hours only as a decimal')
    group.add_argument('-m', '--minutes', action='store_true', help='Outputs hours and minutes')
    parser.add_argument('file', nargs='?', type=argparse.FileType('r'), default='-',
                        help='The file to be read or if no file given read stdin')
    args = parser.parse_args()

    if args.file.name == '<stdin>':
        config = toml.loads(sys.stdin.read())
    else:
        with open(args.file.name, 'r') as confFile:
            config = toml.loads(confFile.read())

    if args.hours:
        timeFormat = 'HH.hhh'
    elif args.minutes:
        timeFormat = 'HH:mm'
    else:
        timeFormat = None

    print(main(config, timeFormat))
