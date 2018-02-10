PunchCard Tools
===========
This directory contains tools that can be used with the main project.

Convert PunchCard Tool
----------
This tool takes the old format for PunchCards(e.g. [test1](/fixtures/tools/Old-PunchCard-Sample1)) and converts them into the new [TOML](http://github.com/toml-lang/toml) formatted PunchCards(e.g. [test1.toml](/fixtures/PunchCard-Sample1.toml)) that I use.

**Usage**:

This method will create a new file of the same name(and in the same path) with .toml added to the end.
```
$ python3 tools/convertPunchCardToToml.py fixtures/tools/Old-PunchCard-Sample1
```

These methods will output to the screen using stdout but can be combined with similar output techniques as seen in [Running Advanced](/README.md#user-content-advanced) of the main README.
```
# Output to stdout
$ python3 tools/convertPunchCardToToml.py < fixtures/tools/Old-PunchCard-Sample1

# Output redirected to a file from stdout
$ python3 tools/convertPunchCardToToml.py < fixtures/tools/Old-PunchCard-Sample1 > PunchCard-Sample1.toml

# Output to file and still print to screen
$ python3 tools/convertPunchCardToToml.py < fixtures/tools/Old-PunchCard-Sample1 | tee PunchCard-Sample1.toml
```

#### Tests
There are tests for this tool in tests/tools directory. They are ran when running the mentioned usage in the main README:
```
$ python3 -m unittest
```

Clean Script
----------
This is just a bash script that cleans up some artifacts created by python and the test libraries I use.

**Usage**:
```
$ ./tools/clean.sh
```
