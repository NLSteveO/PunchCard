PunchCard Tools
===========
This directory contains tools that can be used with the main project.

Convert PunchCard Tool
----------
This tool takes the old format for PunchCards(e.g. [test1](/tests/tools/test1)) and converts them into the new [TOML](http://github.com/toml-lang/toml) formatted PunchCards(e.g. [test1.toml](/tests/test1.toml)) that I use.

**Usage**:

This method will create a new file of the same name(and in the same path) with .toml added to the end.
```
$ python3 tools/convertPunchCardToToml.py test/tools/test1
```

These methods will output to the screen using stdout but can be combined with similar output techniques as seen in [Running Advanced](/README.md#user-content-advanced) of the main README.
```
# Output to stdout
$ python3 tools/convertPunchCardToToml.py < test/tools/test1

# Output redirected to a file from stdout
$ python3 tools/convertPunchCardToToml.py < test/tools/test1 > test1.toml

# Output to file and still print to screen
$ python3 tools/convertPunchCardToToml.py < test/tools/test1 | tee test1.toml
```

#### Tests
There are tests for this tool in tests/tools directory.

Clean Script
----------
This is just a bash script that cleans up some artifacts created by python and the test libraries I use.

**Usage**:
```
$ ./tools/clean.sh
```
