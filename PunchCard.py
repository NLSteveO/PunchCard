import argparse
import sys
import toml


def calcWorkTime(timeIn, timeOut):
    inSplit = timeIn.split(':')
    outSplit = timeOut.split(':')
    hourIn = float(inSplit[0])
    minuteIn = float(inSplit[1])
    hourOut = float(outSplit[0])
    minuteOut = float(outSplit[1])

    if hourIn > hourOut:
        newHour = (hourOut + 12) - hourIn
    else:
        newHour = hourOut - hourIn

    newMinutes = minuteOut - minuteIn
    if newMinutes < 0:
        newHour -= 1
        newMinutes += 60

    return newHour + (newMinutes / 60)


def calculateDay(dayEntry):
    index = 0
    dayHours = 0.0
    while(index < len(dayEntry)):
        dayHours += calcWorkTime(dayEntry[index], dayEntry[index+1])
        index += 2
    return dayHours


def printDaysHours(day, hours, timeFormat):
    floatHours = round(hours, 3)
    intHours = int(floatHours)
    intMinutes = int((floatHours - intHours)*60)
    if timeFormat == 'HH.hhh':
        return '\n{}: {} hours'.format(day.capitalize(), floatHours)
    elif timeFormat == 'HH:mm':
        return '\n{}: {} hours {} minutes'.format(day.capitalize(), intHours, intMinutes)
    else:
        return '\n{}: {} hours {} minutes({} hours)'.format(day.capitalize(), intHours, intMinutes, floatHours)


def printWeekHours(hours, timeFormat):
    floatHours = round(hours, 3)
    intHours = int(floatHours)
    intMinutes = int((floatHours - intHours)*60)
    if timeFormat == 'HH.hhh':
        return '\nTotal hours for the week: {} hours'.format(floatHours)
    elif timeFormat == 'HH:mm':
        return '\nTotal hours for the week: {} hours {} minutes'.format(intHours, intMinutes)
    else:
        return '\nTotal hours for the week: {} hours {} minutes({} hours)'.format(intHours, intMinutes, floatHours)


def main(config, timeFormat):  # pragma: no cover
    daysOfTheWeek = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
    weekHours = 0.0
    punchCardOutput = '{}{}'.format(config['title'], '\n')
    for day in daysOfTheWeek:
        if day not in config['day'] or not config['day'][day]:
            punchCardOutput = '{}{}'.format(punchCardOutput, printDaysHours(day, 0, timeFormat))
            continue
        dayHours = calculateDay(config['day'][day]['000'])
        punchCardOutput = '{}{}'.format(punchCardOutput, printDaysHours(day, dayHours, timeFormat))
        weekHours += dayHours

    return '{}{}{}'.format(punchCardOutput, '\n', printWeekHours(weekHours, timeFormat))


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
