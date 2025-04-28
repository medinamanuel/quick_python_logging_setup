import logging
from logging_setup import LoggingSetup

LoggingSetup.setup_logging(LoggingSetup.MAIN_LOGGER_NAME)
logger = logging.getLogger(LoggingSetup.MAIN_LOGGER_NAME)


def main():
    logger.info("This is an info message")
    # With the default configuration, this will show only on file, not on stdout
    logger.debug("This is a debug message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")


if __name__ == "__main__":
    main()
