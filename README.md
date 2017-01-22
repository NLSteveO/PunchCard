# PunchCard
This is a simple program meant to calculate my work hours for me.

## Input
The input should be a file where the first line states "Week ending on [mm/dd/yy]" The next 5 lines are the days of the week with comma separated values stating the times i start and end my day or various breaks.

For Example:
```
Week ending on 12/9/16
M,8:10,12:00,12:30,5:10
T,8:10,10:00,10:10,12:10,12:40,2:00,2:10,5:00
W,8:00,4:00
R
F,8:00,8:00
```

## Output
The output will be similar to the input file, the first line will be "Week ending on [mm/dd/yy]". The following 5 lines will start with the first letter of that day of the week then the number of hours worked that day. The last day will say "Total hours for the week: [x]" where [x] is the sum of the hours on the 5 previous lines.

For Example:
```
Week ending on 12/9/16

M: 20.5
T: 20.0
W: 20.0
R: 0
F: 0.0

Total hours for the week: 60.5
```

## How to run
To run this program you will want to pipe the input file through standard in to the program like so:
```
$ python PunchCard.py < test.in
```
However you can also then redirect the standard out to a file rather than have the output print to the screen like this:
```
$ python PunchCard.py < test.in > test.out
```
Also, if you want to have the output go to a file and your screen you can do the following:
```
$ python PunchCard.py < test.in | tee test.out
```

# License
MIT
