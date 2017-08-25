import argparse


def parseDay(weekDay, sunday):
    daysOfTheWeek = {'S': 'saturday', 'S2': 'sunday', 'M': 'monday', 'T': 'tuesday',
                     'W': 'wednesday', 'R': 'thursday', 'F': 'friday'}

    splitDay = weekDay.split(',')

    if sunday:
        day = 'S2'
        splitDay.pop(0)
    else:
        day = splitDay.pop(0)[0]

    dayOfTheWeek = daysOfTheWeek[day]

    if len(splitDay) == 0:
        return(dayOfTheWeek, None)
    else:
        dayArray = []
        for time in splitDay:
            dayArray.append(time)

        return(dayOfTheWeek, "'000' = {}\n".format(dayArray))


def main(punchCard):
    tab = '  '
    title = punchCard.pop(0).rstrip('\n')
    day = tab+"projects = ['000']\n\n"

    for line in punchCard:
        line = line.rstrip('\n')
        if 'saturday' in day and line[0] == 'S':
            weekday = parseDay(line, True)
        else:
            weekday = parseDay(line, False)
        if weekday[1]:
            day = '{}{}[day.{}]\n{}{}{}\n'.format(day, tab, weekday[0], tab, tab, weekday[1])
        else:
            day = '{}{}[day.{}]\n{}{}{}\n'.format(day, tab, weekday[0], tab, tab, '')

    return "title = '{}'\n\n[day]\n\n{}".format(title, day)


if __name__ == '__main__':  # pragma: no cover
    description = 'This is a script to convert PunchCards from the old format to the new TOML format.'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('file', nargs='?', type=argparse.FileType('r'), default='-',
                        help='The old format PunchCard to be converted or if no file given read stdin')
    args = parser.parse_args()

    oldPunchCard = []

    for line in args.file:
        oldPunchCard.append(line)

    newPunchCard = main(oldPunchCard).rstrip('\n')

    if args.file.name == '<stdin>':
        print(newPunchCard)
    else:
        with open(args.file.name+'.toml', 'w') as newFile:
            newFile.write(newPunchCard)
