import logging
import logging.handlers
import sys
from enum import Enum

from log_file_manager.architecture import Architecture
from log_file_manager.log_creation import LogFileMethods
from constants.plot_graph_constants import AppConstants


class LogManager:
    """
    - log specific modules for the logging package
    """

    def __init__(self, level, enable_console=False):
        """
        - creates file logging (as csv) and to console, if requested.
        - param level: level to show in log (info, warning, critical, error, debug)
        - type level: int
        - param enable_console: enabled logging to console
        - type enable_console: bool
        """
        # create logger & set level for logging
        self.logger = logging.getLogger()  # (__name__)
        self.logger.setLevel(level.value)

        # create formatter
        log_format_file = logging.Formatter('%(asctime)s,%(levelname)s,%(message)s')
        log_format_console = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # create file handler
        LogFileMethods.create_dir(AppConstants.app_export_path)
        file_handler = logging.handlers.RotatingFileHandler("{}/{}"
                                                            .format(AppConstants.app_export_path,
                                                                    AppConstants.log_filename),
                                                            maxBytes=AppConstants.log_max_bytes,
                                                            backupCount=0)
        file_handler.setFormatter(log_format_file)

        # add file handler to logger
        self.logger.addHandler(file_handler)

        # if console logger is TRUE: create console handler & add consola handler to logger
        if enable_console:
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setFormatter(log_format_console)
            self.logger.addHandler(console_handler)

        self._show_user_info()

    @staticmethod
    def close():
        """
        - closes the enabled loggers.
        - return: none
        """
        logging.shutdown()

    @staticmethod
    def d(tag, msg):
        """
        - Logs at debug level
        - param tag: TAG to identify the log.
        - type tag: str
        - param msg: Message to log
        - type msg: str
        - return: none
        """
        logging.debug("[{}] {}".format(str(tag), str(msg)))

    @staticmethod
    def i(tag, msg):
        """
        - Logs at INFO level.
        - param tag: TAG to identify the log.
        - type tag: str.
        - param msg: Message to log.
        - type msg: str.
        - return:
        """
        logging.info("[{}] {}".format(str(tag), str(msg)))

    @staticmethod
    def w(tag, msg):
        """
        - Logs at WARNING level
        - param tag: TAG to identify the log
        - type tag: str
        - param msg: Message to log
        - type msg: str
        - return: none
        """
        logging.warning("[{}] {}".format(str(tag), str(msg)))

    @staticmethod
    def e(tag, msg):
        """
        - logs at ERROR level
        - param tag: TAG to identify the log
        - type tag: str
        - param msg: MSG to log
        - type msg: str
        - return: none
        """
        logging.error("[{}] {}".format(str(tag), str(msg)))

    @staticmethod
    def _show_user_info():
        """
        - USER info
        - return: none
        """
        tag = "User"
        LogManager.i(tag, "Platform: {}".format(Architecture.get_os_name()))
        LogManager.i(tag, "Path: {}".format(Architecture.get_path()))
        LogManager.i(tag, "Python: {}".format(Architecture.get_python_version()))


class LoggerLevel(Enum):
    """
    - enum for the logger levels
    """
    CRITICAL = logging.CRITICAL  # a serious error, indicating that the program itself may be unable to continue running
    ERROR = logging.ERROR  # due to a serious problem, the app has not been able to perform as expected
    WARNING = logging.WARNING  # an indication that something unexpected happened (default)
    INFO = logging.INFO  # confirmation that things are working as expected
    DEBUG = logging.DEBUG  # detailed info, typically of interest only when
    # diagnosing problems
