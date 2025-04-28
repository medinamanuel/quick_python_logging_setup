# Quick Python Logging Setup

We've all been there at least once: We start with something easy and add print statements "just to check". Then, when we realize it, we have written a lot, made good progress,
and now those print statements look awful, or some of them should only be used on certain circumstances, or we also want to save them into a file.

Whatever the reason, configuring a proper logging setup is not fun, and for beginners it's even dreadful. 

Yes, now with LLMs it's easier than ever to just craft a prompt and have something functional in minutes. But for those who can't write a prompt to get good results, or those who 
just want something that works without too much hassle, use these files.


# Usage
See `log_test.py`. 

# Structure
The idea is to have at least one logger that has 2 handlers: One for stdout and one for file. For the latter, RotatingFileHandler is used. 
Be default, log files will be saved inside a `logs` directory. It will be created if it does not exist. You can change it on `LoggingSetup.LOG_DIRECTORY_NAME`

## Handlers
### Console
Just print to stdout. DEBUG messages won't be printed here by default

### File handlers
One per logger. See `Rotating File` below for details


## Rotating File
In summary: 

- A log file will be created
- Logs will be written there until the file reaches 20MB
- After 20 MBs, the log file will be renamed as `***_log_file.log.1`, and all subsequent logs will be written to a new log file
- Once there are 10 log files of the same logger, older ones will be replaced


# Configuration file
Standard JSON. Modify as you need.
