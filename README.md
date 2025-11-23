# Anniversarator

Never forget how long you've been married again!

Anniversarator is a simple Python command-line utility for persistent tracking of important dates and anniversaries.

## Features

-  Create and store important dates
-  Track elapsed time since events (years and days)
-  Calculate days until next occurrence
-  Persistent storage using pickle
-  Delete events you no longer need

## Installation

Install the package using pipx in the anniversarator directory:

```bash
pipx install .
```
Once the package is installed the downloaded folder can be deleted

Instructions on how to install pipx can be found [here](https://pipx.pypa.io/latest/installation/)

Note: pipx requires pip. Installation instructions for pip can be found [here](https://pip.pypa.io/en/stable/installation/)

## Usage

Run Anniversarator with the following commands:

```bash
# Create new events
anniversarator -n

# Print all stored events
anniversarator -p

# Delete events
anniversarator -d

# Combine options
anniversarator -n -p
```

### Options

- `-n, --new` - Create new events
- `-p, --print` - Print all events
- `-d, --delete` - Delete events

## Usage Examples

**Create a new anniversary:**
```bash
$ anniversarator -n
**** Create New Anniversarator Event ****
*   Valid inputs:                       *
*       Title: any                      *
*       Year: 0 < Year <= 9999          *
*       Month: 0 < Month <= 12          *
*       Day: 0 < Day <= days in month   *
*****************************************
Event title? An Anniversary 
Event year? 2013
Event month (1 - 12)? 11
Event day? 12

Event Title: An Anniversary | Event Date: 2013-11-12
Is this correct (y/n)? y
Would you like to add another event (y/n)? n
```

**View all events:**
```bash
$ anniversarator -p

**************  An Anniversary - 2013-11-12  **************
* Next Occurrence: 2026-11-12, in 354 day(s)              *
* Time Elapsed: 12 year(s) and 14 day(s)                  *
* Day(s) Elapsed: 4394 day(s)                             *
***********************************************************

**************  Another Event - 2018-06-23  ***************
* Next Occurrence: 2026-06-23, in 212 day(s)              *
* Time Elapsed: 7 year(s) and 155 day(s)                  *
* Day(s) Elapsed: 2710 day(s)                             *
***********************************************************
```
## File Storage

Events are stored in `/Home/.anniversarator/saves/events.pickle` using Python's pickle module. Debug logs are written to `/Home/.anniversarator/logs/debug.log`.

## Requirements

- Python 3.7+
- No external dependencies

## Author

Mike Vance

## License

This project is licensed under the MIT License - see the [License](License) file for details.

## Future Features

- next upcoming event function
- delete all function
