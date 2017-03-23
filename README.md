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
- [Examples](#user-content-examples)
    - [Input Example](#user-content-input-example)
    - [Output Example](#user-content-output-example)
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
$ python3 -m PunchCard tests/test.toml
```

#### Advanced
It is also possible to pass the input file in through stdin like so:
```
$ python3 -m PunchCard < tests/test.toml
```
However you can also then redirect the standard out to a file rather than have the output print to the screen like this:
```
$ python3 -m PunchCard tests/test.toml > test.out
```
Also, if you want to have the output go to a file and your screen you can do the following:
```
$ python3 -m PunchCard tests/test.toml | tee test.out
```

#### Flags
There are two additional Flags that you can pass to the program to alter who the output looks. These flags are mutually exclusive, so you can only specify one or the other. To see the output you get without either flag see the [Examples Output section](#user-content-output-example).

- `-H, --hours`    Outputs hours only as a decimal

```
$ python3 -m PunchCard tests/test.toml -H
Week ending on 12/9/16

saturday: 0 hours
sunday: 0 hours
monday: 8.5 hours
tuesday: 8.0 hours
wednesday: 8.0 hours
thursday: 0 hours
friday: 0.0 hours

Total hours for the week: 24.5 hours
```
- `-m, --minutes`  Outputs hours with minutes

```
$ python3 -m PunchCard tests/test.toml -m
Week ending on 12/9/16

saturday: 0 hours 0 minutes
sunday: 0 hours 0 minutes
monday: 8 hours 30 minutes
tuesday: 8 hours 0 minutes
wednesday: 8 hours 0 minutes
thursday: 0 hours 0 minutes
friday: 0 hours 0 minutes

Total hours for the week: 24 hours 30 minutes
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
$ python3 -m unittest -bv tests/PunchCard-test
```

Examples
--------
#### Input Example
The input should be a [TOML](https://github.com/toml-lang/toml) file like the example below. The title in the input will be the first line in your output, you can skip days of the week or leave them empty, and the array of time punches for each day can be done in 12 hour or 24 hour format as long as it is consistent for the array.

*NOTE:* The projects array is for future implementation where you can add your hours to separate projects. For now set one number in the array and use that as the key to your week days array like in the example.

For Example:
```
title = "Week ending on 12/9/16"

[day]
  projects = [000]

  [day.sunday]

  [day.saturday]

  [day.monday]
    000 = ['8:10', '12:00', '12:30', '5:10']

  [day.tuesday]
    000 = ['8:10', '10:00', '10:10', '12:10', '12:40', '2:00', '2:10', '5:00']

  [day.wednesday]
    000 = ['8:00', '4:00']

  [day.thursday]

  [day.friday]
    000 = ['8:00', '8:00']
```

#### Output Example
The output will be a simple text file, the first line will be "Week ending on [mm/dd/yy]". The following 5 lines will start with the day of the week then the number of hours and minutes worked that day. The last line will say "Total hours for the week: [x]" where [x] is the sum of the hours and minutes from the 5 previous lines.

For Example:
```
Week ending on 12/9/16

saturday: 0 hours 0 minutes(0 hours)
sunday: 0 hours 0 minutes(0 hours)
monday: 8 hours 30 minutes(8.5 hours)
tuesday: 8 hours 0 minutes(8.0 hours)
wednesday: 8 hours 0 minutes(8.0 hours)
thursday: 0 hours 0 minutes(0 hours)
friday: 0 hours 0 minutes(0.0 hours)

Total hours for the week: 24 hours 30 minutes(24.5 hours)
```

What's New
----------
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
