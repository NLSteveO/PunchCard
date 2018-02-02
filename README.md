PunchCard
===========
This is a simple program meant to calculate my work hours for me.

[![Build Status](https://travis-ci.org/NLSteveO/PunchCard.svg?branch=master)](https://travis-ci.org/NLSteveO/PunchCard)

Table of Contents
=================
- [Installation](#user-content-installation)
- [Running](#user-content-running)
    - [Simple](#user-content-simple)
    - [Advanced](#user-content-advanced)
    - [Flags](#user-content-flags)
- [Testing](#user-content-testing)
    - [Linting](#user-content-linting)
    - [Unit tests](#user-content-unit-tests)
    - [Coverage](#user-content-coverage)
- [Examples](#user-content-examples)
    - [Input Example](#user-content-input-example)
    - [Output Example](#user-content-output-example)
- [Tools](#user-content-tools)
    - [Convert PunchCard Tool](#user-content-convert-punchcard-tool)
    - [Clean Script](#user-content-clean-script)
- [What's New](#user-content-whats-new)
- [License](#user-content-license)

Installation
------------
To install Punch Card you should first install python 3.6 and pip 3.4.3. Then you will clone this repository and install the requirements using pip:
```
git clone https://github.com/NLSteveO/PunchCard.git
cd PunchCard
pip3 install -r requirements.txt
```

Running
----------
#### Simple
To run this program you will want to pass the input file to the program as an argument and it will output to your screen:
```
$ python3 -m PunchCard fixtures/PunchCard-Sample1.toml
```

#### Advanced
It is also possible to pass the input file in through stdin like so:
```
$ python3 -m PunchCard < fixtures/PunchCard-Sample1.toml
```
However you can also then redirect the standard out to a file rather than have the output print to the screen like this:
```
$ python3 -m PunchCard fixtures/PunchCard-Sample1.toml > PunchCard-Sample1.out
```
Also, if you want to have the output go to a file and your screen you can do the following:
```
$ python3 -m PunchCard fixtures/PunchCard-Sample1.toml | tee PunchCard-Sample1.out
```

#### Flags
There are two additional Flags that you can pass to the program to alter how the output looks. These flags are mutually exclusive, so you can only specify one or the other. To see the output you get without either flag see the [Examples Output section](#user-content-output-example).

- `-H, --hours`    Outputs hours only as a decimal

```
$ python3 -m PunchCard fixtures/PunchCard-Sample1.toml -H
Week ending on 12/9/16

Saturday: 0.0 hours
Sunday: 0.0 hours
Monday: 8.5 hours
        000: 8.5 hours
Tuesday: 8.0 hours
        000: 8.0 hours
Wednesday: 8.0 hours
        000: 8.0 hours
Thursday: 0.0 hours
Friday: 0.0 hours
        000: 0.0 hours

Total hours for the week: 24.5 hours
        000: 24.5 hours
```
- `-m, --minutes`  Outputs hours with minutes

```
$ python3 -m PunchCard fixtures/PunchCard-Sample1.toml -m
Week ending on 12/9/16

Saturday: 0 hours 0 minutes
Sunday: 0 hours 0 minutes
Monday: 8 hours 30 minutes
        000: 8 hours 30 minutes
Tuesday: 8 hours 0 minutes
        000: 8 hours 0 minutes
Wednesday: 8 hours 0 minutes
        000: 8 hours 0 minutes
Thursday: 0 hours 0 minutes
Friday: 0 hours 0 minutes
        000: 0 hours 0 minutes

Total hours for the week: 24 hours 30 minutes
        000: 24 hours 30 minutes
```

Testing
-------
#### Linting
I am using [flake8](https://github.com/PyCQA/flake8) for my style guide linter. You can run the linter using:
```
$ flake8
```

#### Unit tests
I am using the [python standard library's unittest framework.](https://docs.python.org/3/library/unittest.html) You can run the tests using:
```
$ python3 -m unittest
```
*Note:* You can use the flag `-v` to get a more verbose output when running tests.

#### Coverage
I am using the library [coverage](https://bitbucket.org/ned/coveragepy) for creating coverage reports. To get a coverage report first run your unit tests using:
```
$ coverage run -m unittest discover
```
*Note:* You can use the flag `-v` to get a more verbose output when running tests.

Then to get a coverage report use:
```
$ coverage report
```
Or you can generate annotated HTML listings detailing missed lines by using:
```
$ coverage html
```

Examples
--------
#### Input Example
The input should be a [TOML](https://github.com/toml-lang/toml) file like the example below. The title in the input will be the first line in your output, you can skip days of the week or leave them empty, and the array of time punches for each day can be done in 12 hour or 24 hour format as long as it is consistent for the array. The key of each array in a day should be associated with a project code in the projects array. Both the project code in the array and the keys should be strings.


For Example:
```
title = "Week ending on 12/9/16"

[day]
  projects = ['001', '002', '003', '004']

  [day.saturday]

  [day.sunday]

  [day.monday]
    '001' = ['8:10', '12:00', '12:30', '5:10']

  [day.tuesday]
    '001' = ['8:10', '10:00', '2:10', '5:00']
    '002' = ['10:10', '12:10', '12:40', '2:00']

  [day.wednesday]
    '004' = ['8:00', '4:00']

  [day.thursday]
    '001' = ['8:15', '10:00']
    '002' = ['10:00', '12:00']
    '003' = ['12:30', '2:10']
    '004' = ['2:10', '5:15']

  [day.friday]
    '002' = ['8:15', '10:00', '2:10', '5:15']
    '003' = ['10:00', '12:00']
    '004' = ['12:30', '2:10']
```

#### Output Example
The output will be a simple text file, the first line will be "Week ending on [mm/dd/yy]". The following lines will start with the day of the week then the number of hours and minutes worked that day. For each day there will be an indented line for each project code used on that day in the format of project code followed by the number of hours and minutes worked that day for the given project code. The last lines will say "Total hours for the week: [z]" where [z] is the sum of the hours and minutes from the day totals on previous lines. That will be followed up with a line for each project code used during the week and its total hours and minutes for the week.

For Example:
```
Week ending on 12/9/16

Saturday: 0 hours 0 minutes(0.0 hours)
Sunday: 0 hours 0 minutes(0.0 hours)
Monday: 8 hours 30 minutes(8.5 hours)
        001: 8 hours 30 minutes(8.5 hours)
Tuesday: 8 hours 0 minutes(8.0 hours)
        001: 4 hours 40 minutes(4.667 hours)
        002: 3 hours 19 minutes(3.333 hours)
Wednesday: 8 hours 0 minutes(8.0 hours)
        004: 8 hours 0 minutes(8.0 hours)
Thursday: 8 hours 30 minutes(8.5 hours)
        001: 1 hours 45 minutes(1.75 hours)
        002: 2 hours 0 minutes(2.0 hours)
        003: 1 hours 40 minutes(1.667 hours)
        004: 3 hours 4 minutes(3.083 hours)
Friday: 8 hours 30 minutes(8.5 hours)
        002: 4 hours 49 minutes(4.833 hours)
        003: 2 hours 0 minutes(2.0 hours)
        004: 1 hours 40 minutes(1.667 hours)

Total hours for the week: 41 hours 30 minutes(41.5 hours)
        001: 14 hours 55 minutes(14.917 hours)
        002: 10 hours 10 minutes(10.167 hours)
        003: 3 hours 40 minutes(3.667 hours)
        004: 12 hours 45 minutes(12.75 hours)
```

Tools
----------
For more detailed information see the [README in the tools directory](tools/README.md)

#### Convert PunchCard Tool
This tool takes the old format for PunchCards(e.g. [test1](/fixtures/tools/Old-PunchCard-Sample1)) and converts them into the new [TOML](http://github.com/toml-lang/toml) formatted PunchCards(e.g. [test1.toml](/fixtures/PunchCard-Sample1.toml)) that I use.

#### Clean Script
This is just a bash script that cleans up some artifacts created by python and the test libraries I use.

What's New
----------
- 2017-06-06: Add handling for multiple project codes.
- 2017-05-12: Add unit tests for main method.
- 2017-04-20: Add time and day validation.
- 2017-04-14: Cleanup travis output.
- 2017-04-14: Add clean script.
- 2017-04-14: Rewrite of print methods.
- 2017-03-16: Add a new format for the Time Cards.
- 2017-03-02: Add coverage library to use coverage reports.
- 2017-02-21: Add argparse library to use command line flags.
- 2017-02-09: Fixed the project directory structure.
- 2017-02-05: Add gitignore file.
- 2017-02-04: Add unittest suite and unit tests.
- 2017-01-30: Add requirements file for easy dependency installation.
- 2017-01-30: Add flake8 python linter library.MIT
- 2017-01-26: Add travis-ci config file to start using continuous integration.
- 2017-01-26: Update code to use python 3.6.
- 2017-01-21: Initial commit, add PunchCard program with sample input and README.md.

License
-------
MIT
