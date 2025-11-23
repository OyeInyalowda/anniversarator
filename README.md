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
Note: Once the package is installed the downloaded folder can be deleted

Instructions on how to install pipx can be found [here](https://pipx.pypa.io/latest/installation/)

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
Event title? Wedding
Event year? 2020
Event month (1 - 12)? 6
Event day? 15
Event Title: Wedding | Event Date: 2020-06-15
Is this correct (y/n)? y
```

**View all events:**
```bash
$ anniversarator -p

********** Wedding **********
4 year(s) and 213 day(s) since 2020-06-15
1462 total day(s) since 2020-06-15
Wedding occurs next on 2025-06-15 in 152 day(s)
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
