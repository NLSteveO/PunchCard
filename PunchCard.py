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


def main(input):
    weekHours = 0.0
    print(input.pop(0))
    for line in input:
        daySplit = line.split(',')
        dayLetter = daySplit.pop(0)[0]
        dayHours = calculateDay(daySplit)
        print(dayLetter + ': ' + str(dayHours))
        weekHours += dayHours

    print('\nTotal hours for the week: ' + str(weekHours))


if __name__ == '__main__':
    lines = []
    for line in fileinput.input():
        lines.append(line)
    main(lines)
