from PyQt5 import QtGui


class AppConstants:
    """
    ----    Common constants used in the different Py modules   ----
    ---- That are part of the Real Time Plot Interface for Zynq ----
    ----          Based Data Acquisition Systems                ----
    """
    # ------ plot GUI values ------- #
    app_title = "RealTime_Plot"
    app_plot_title = "Real Time Plot - ICTP MLAB"
    app_version = '0.1'
    app_export_path = "log_info"
    app_comm_sources = ["Serial", "Simulator", "UDP"]
    app_encoding = "utf-8"

    # plot's default variables and values
    # plot_update_us = 200
    plot_y_label = "Voltage"
    plot_y_label_unit = "V"
    plot_x_label = "Time"
    plot_x_label_unit = "sec"
    # plot_signal_colors = ['#0072bd', '#d95319', '#edb120', '#7e2f8e', '#77ac30', '#4dbeee', '#a2142f']
    # plot_max_num_signals = len(plot_signal_colors)
    plot_default_samples = 1000
    plot_max_num_channels = 16

    # number of samples to plot
    samples2plot = 100
    # ------------------------------------ #

    # time in miliseconds between reads used to set the timer timeout
    t_bt_samples: int = 40

    # number of sensors to read per read
    number_sensors: int = 16

    # ------ serial comm constants ------ #
    # serial default baudrate
    default_baudrate = 115200
    baudrates = [115200, 128000, 230400, 460800, 921600]  # baud rates available in the Zynq
    serial_timeout_ms = 0.5

    # number of bytes to read each time
    bytes2read: int = 7  # in teh C code: printf("%2.4f", temperature);

    # default serial communication port
    comm_port = '/dev/ttyACM0'
    # ------------------------------------ #

    # -------- cvs export file default variables and values ------ #
    csv_default_filename = "%Y-%m-%d_%H-%M-%S"
    csv_delimiter = ","
    csv_file_extension = "csv"

    # -------- log file default variables and values ------- #
    log_filename = "{}.log".format(app_title)
    log_max_bytes = 5120
    # log_default_level = 1
    log_default_console_log = False

    # -------- dictionary to define plot color per each channel ------ #
    # https://www.rapidtables.com/web/color/RGB_Color.html
    plot_colors = {
        's1': QtGui.QColor(255, 255, 255),      # white     #FFFFFF
        's2': QtGui.QColor(255, 0, 0),          # red       #FF0000
        's3': QtGui.QColor(0, 255, 0),          # lime      #00FF00
        's4': QtGui.QColor(0, 0, 255),          # blue      #0000FF
        's5': QtGui.QColor(255, 255, 0),        # yellow    #FFFF00
        's6': QtGui.QColor(0, 255, 255),        # cyan      #00FFFF
        's7': QtGui.QColor(255, 0, 255),        # magenta   #FF00FF
        's8': QtGui.QColor(210, 105, 30),       # chocolate #D2691E
        's9': QtGui.QColor(188, 143, 143),      # rosy brown#BC8F8F
        's10': QtGui.QColor(128, 128, 0),       # olive     #808000
        's11': QtGui.QColor(0, 128, 0),         # green     #008000
        's12': QtGui.QColor(128, 0, 128),       # purple    #800080
        's13': QtGui.QColor(0, 128, 128),       # teal      #008080
        's14': QtGui.QColor(47, 79, 79),        # dark slate gray #2F4F4F
        's15': QtGui.QColor(255, 165, 0),       # orange    #FFA500
        's16': QtGui.QColor(210,180,140),       # tan       #D2B48C
    }
