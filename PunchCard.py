import argparse
import fileinput


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
        print('{}: {} hours'.format(day, floatHours))
    elif timeFormat == 'HH:mm':
        print('{}: {} hours {} minutes'.format(day, intHours, intMinutes))
    else:
        print('{}: {} hours {} minutes({} hours)'.format(day, intHours, intMinutes, floatHours))


def printWeekHours(hours, timeFormat):
    floatHours = round(hours, 3)
    intHours = int(floatHours)
    intMinutes = int((floatHours - intHours)*60)
    if timeFormat == 'HH.hhh':
        print('\nTotal hours for the week: {} hours'.format(floatHours))
    elif timeFormat == 'HH:mm':
        print('\nTotal hours for the week: {} hours {} minutes'.format(intHours, intMinutes))
    else:
        print('\nTotal hours for the week: {} hours {} minutes({} hours)'.format(intHours, intMinutes, floatHours))


def main(input, timeFormat):  # pragma: no cover
    weekHours = 0.0
    print(input.pop(0))
    for line in input:
        daySplit = line.split(',')
        dayLetter = daySplit.pop(0)[0]
        dayHours = calculateDay(daySplit)
        printDaysHours(dayLetter, dayHours, timeFormat)
        weekHours += dayHours

    printWeekHours(weekHours, timeFormat)


if __name__ == '__main__':  # pragma: no cover
    description = 'This is a simple program meant to calculate my work hours.'
    parser = argparse.ArgumentParser(description=description)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-H', '--hours', action='store_true', help='Outputs hours only as a decimal')
    group.add_argument('-m', '--minutes', action='store_true', help='Outputs hours and minutes')
    parser.add_argument('file', nargs='?', type=argparse.FileType('r'), default='-',
                        help='The file to be read or if no file given read stdin')
    args = parser.parse_args()

    lines = []
    if args.file.name == '<stdin>':
        for line in fileinput.input('-'):
            lines.append(line)
    else:
        for line in fileinput.input(args.file.name):
            lines.append(line)

    if args.hours:
        timeFormat = 'HH.hhh'
    elif args.minutes:
        timeFormat = 'HH:mm'
    else:
        timeFormat = None

    main(lines, timeFormat)
