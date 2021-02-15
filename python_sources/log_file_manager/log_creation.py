import os


class LogFileMethods:
    """
    - modules related to the log file
    """

    @staticmethod
    def create_dir(path=None):
        """
        - creates a directory if the specified doesn't exists.
        - param path: directory name or full path
        - type path: str
        - return: TRUE if the specified directory exists
        - rtype: bool
        """
        if path is not None:
            if not os.path.isdir(path):
                os.makedirs(path)
        return os.path.isdir(path)

    @staticmethod
    def create_file(filename, extension="txt", path=None):
        """
        - creates a file full path based on passed parameters
        - param filename: file name
        - type filename: str
        - param extension: extension for the file (txt by default)
        - type extension: str
        - param path: path for the file (optional)
        - type path: str
        - return: full path
        - rtype: str
        """
        if path is None:
            full_path = str("{}.{}".format(filename, extension))
        else:
            full_path = str("{}/{}.{}".format(path, filename, extension))
        return full_path

    @staticmethod
    def file_exists(filename):
        """
        - checks if a file exists
        - param filename: name of the file, including path.
        - type filename: str
        - return: TRUE if the file exists
        - rtype: bool
        """
        if filename is not None:
            return os.path.isfile(filename)
