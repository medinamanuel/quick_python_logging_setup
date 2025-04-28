import logging.config
import json
from pathlib import Path
from typing import Literal


class LoggingSetup:
    MAIN_LOGGER_NAME = "main_logger"
    LOGGING_CONFIGURATION_FILE = "logging_config.json"
    LOG_DIRECTORY_NAME = "logs"
    LOGFILE_NAME = "main_log_file.log"
    SUB_LOGGER_NAME = "sub_logger"
    SUB_LOGFILE_NAME = "sub_log_file.log"

    @classmethod
    def _get_project_root_directory_path(cls) -> Path:
        return Path(__file__).parent

    @classmethod
    def get_logging_configuration_file_path(cls) -> Path:
        return (
            cls._get_project_root_directory_path()
            / cls.LOGGING_CONFIGURATION_FILE
        )

    @classmethod
    def get_log_directory_path(cls) -> Path:
        return cls._get_project_root_directory_path() / cls.LOG_DIRECTORY_NAME

    @classmethod
    def _is_main_logger_already_configured(cls) -> bool:
        return not len(logging.getLogger(cls.MAIN_LOGGER_NAME).handlers) == 0

    @classmethod
    def _is_logger_already_configured(
        cls, logger_name: Literal["main_logger", "sub_logger"]
    ):
        return not len(logging.getLogger(logger_name).handlers) == 0

    @classmethod
    def setup_logging(
        cls,
        logger_name: Literal["main_logger", "sub_logger"] = MAIN_LOGGER_NAME,
    ):

        if cls._is_logger_already_configured(logger_name):
            return

        logfile_name = (
            cls.LOGFILE_NAME
            if logger_name == cls.MAIN_LOGGER_NAME
            else cls.SUB_LOGFILE_NAME
        )
        log_directory_path = cls.get_log_directory_path()
        logfile_path = log_directory_path / logfile_name

        if not log_directory_path.is_dir():
            Path.mkdir(log_directory_path, parents=True, exist_ok=True)

        if not logfile_path.is_file():
            logfile_path.touch()

        with open(cls.get_logging_configuration_file_path(), "rt") as f:
            config = json.load(f)

        logging.config.dictConfig(config)
