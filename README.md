# WorkingTime

The program is a tool written in Python, which is used to record the daily working time and breaks.
The recorded times are saved in a Git repository created especially for the tool.

## Overview
```
Usage:
  workingtime [command]

Available commands:
  list
  add
  edit
  del
```

```
Usage:
  workingtime list [options]

Options:
  -a, --all                                      List all available days
  -d, --day                                      Lists a specific day
```

```
Usage:
  workingtime add [options]

Options:
  -d, --day                                      Day of entry
  -s, --start-time                               Start of work
  -e, --end-time                                 Working time end
  -b, --break-time                               Work break in minutes
  -c, --comment                                  Comment on the working day
```

```
Usage:
  workingtime edit [options]

Options:
  -d, --day                                      Day of entry
  -s, --start-time                               Start of work
  -e, --end-time                                 Working time end
  -b, --break-time                               Work break in minutes
  -c, --comment                                  Comment on the working day
```

```
Usage:
  workingtime edit [options]

Options:
  -d, --day                                      Day of entry
  -r, --reset-repo                               Resetting the whole repository
```
