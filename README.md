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

Note: For Anniversarator to function as a command line utility it must be installed using pipx. The following instructions assume you have both pip and pipx installed. If you do not, install instructions for both can be found here: [pip](https://pip.pypa.io/en/stable/installation/) | [pipx](https://pipx.pypa.io/latest/installation/)

- Download the latest Anniversarator release and extract the contents
- Enter the Anniversarator folder (wherever you extracted it)
    - Linux Example:
    ```bash
    cd path/to/anniversarator-versionName
    ```

    - Windows: Example
    ```ps
    cd C:\path\to\anniversarator-versionName
    ```

___

```bash
    | This is where you should be
.   v     
└── anniversarator-versionName
    ├── License
    ├── pyproject.toml
    ├── README.md
    └── src
```

- From inside the aforementioned directory install the package using pipx
```bash
pipx install .
```
- Once the package is installed the extracted folder and zip file can be deleted
- Enjoy!

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
- pip and pipx

## Author

Mike Vance

## License

This project is licensed under the MIT License - see the [License](License) file for details.

## Future Features

- next upcoming event function
- delete all function
