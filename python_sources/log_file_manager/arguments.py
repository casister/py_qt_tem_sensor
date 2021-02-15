import argparse

from log_file_manager.log_write import LogManager as LogM
from log_file_manager.log_write import LoggerLevel
from constants.plot_graph_constants import AppConstants

TAG = "Arguments"


class Arguments:
    """
    - wrapper for argparse package.
    """

    def __init__(self):
        self._parser = None

    def create(self):
        """
        - creates argument parser
        - define arguments to the created parser (parse.add_argument())
        - return: none
        """
        parser = argparse.ArgumentParser(description='-- Rel Time Plot Graph --\n \
                                    -- A real time plotting and logging application --',
                                         epilog='Enjoy the program! :)')
        parser.add_argument("-i", "--info",
                            dest="log_level_info",
                            action='store_true',
                            help="enable info messages"
                            )

        parser.add_argument("-d", "--debug",
                            dest="log_level_debug",
                            action='store_true',
                            help="enable debug messages"
                            )

        parser.add_argument("-v", "--verbose",
                            dest="log_to_console",
                            action='store_true',
                            help="show log messages in console",
                            default=AppConstants.log_default_console_log
                            )

        parser.add_argument("-s", "--samples",
                            dest="user_samples",
                            default=AppConstants.plot_default_samples,
                            help="Specify number of sample to show on plot"
                            )
        self._parser = parser.parse_args()

    def set_user_log_level(self):
        """
        - sets the user specified log level
        - return: none
        """
        if self._parser is not None:
            self._parse_log_level()
        else:
            LogM.w(TAG, "Parser was not created !")
            return None

    def get_user_samples(self):
        """
        - gets the user specified samples to show in the plot.
        - return: Samples specified by user, or default value if not specified.
        - rtype: int.
        """
        return int(self._parser.user_samples)

    def get_user_console_log(self):
        """
        - gets the user specified log to console flag
        - return: TRUE if log to console is enabled
        - rtype: bool
        """
        return self._parser.log_to_console

    def _parse_log_level(self):
        """
        - sets the log level depending on user specification.
        - It will also enable or disable log to console based on user specification.
        - return: none
        """
        log_to_console = self.get_user_console_log()
        level = LoggerLevel.INFO
        if self._parser.log_level_info:
            level = LoggerLevel.INFO
        elif self._parser.log_level_debug:
            level = LoggerLevel.DEBUG
        LogM(level, enable_console=log_to_console)
