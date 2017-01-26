import fileinput

weekHours = 0.0
dayHours = 0.0

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

  global dayHours
  dayHours += newHour + (newMinutes / 60)

def calculateDay(dayEntry):
  day = dayEntry.pop(0)[0]
  index = 0
  while(index < len(dayEntry)):
    calcWorkTime(dayEntry[index], dayEntry[index+1])
    index += 2
  print day + ': ' + str(dayHours)


lines=[]
for line in fileinput.input():
  lines.append(line)

print lines.pop(0)
for line in lines:
  calculateDay(line.split(','))
  weekHours += dayHours
  dayHours = 0.0

print '\nTotal hours for the week: ' + str(weekHours)
