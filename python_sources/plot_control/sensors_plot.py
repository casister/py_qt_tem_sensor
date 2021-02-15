from PyQt5 import QtGui, QtCore  # , QtWidgets  # QtGui,

from constants.plot_graph_constants import AppConstants
import numpy as np
import time
from log_file_manager.log_write import LogManager


TAG = "PlotController"


class PlotController(QtGui.QMainWindow):
    def __init__(self, plot_graph, rx_tx_ctrl):
        QtGui.QMainWindow.__init__(self)
        # self.timer = QtCore.QTimer()
        self.plot_graph = plot_graph
        self.rx_tx_ctrl = rx_tx_ctrl
        # self.transceiver = serial.Serial('/dev/ttyACM0', baudrate=115200)
        # self.zedboard = ZedboardController(self.transceiver)

        # methods associated to buttons
        self._connect_signals_to_methods()

        # configure timer
        self._configure_timers()

        # set baud rates available for the QComBox
        self.uart_baud_rates = plot_graph
        for baud_rate in AppConstants.baudrates:
            self.uart_baud_rates.cBox_CommSpeed.addItem(str(baud_rate))

        # sensors initial array
        self.sensor_1 = np.zeros(AppConstants.samples2plot, float)
        self.sensor_2 = np.zeros(AppConstants.samples2plot, float)
        self.sensor_3 = np.zeros(AppConstants.samples2plot, float)
        self.sensor_4 = np.zeros(AppConstants.samples2plot, float)
        self.sensor_5 = np.zeros(AppConstants.samples2plot, float)
        self.sensor_6 = np.zeros(AppConstants.samples2plot, float)
        self.sensor_7 = np.zeros(AppConstants.samples2plot, float)
        self.sensor_8 = np.zeros(AppConstants.samples2plot, float)
        self.sensor_9 = np.zeros(AppConstants.samples2plot, float)
        self.sensor_10 = np.zeros(AppConstants.samples2plot, float)
        self.sensor_11 = np.zeros(AppConstants.samples2plot, float)
        self.sensor_12 = np.zeros(AppConstants.samples2plot, float)
        self.sensor_13 = np.zeros(AppConstants.samples2plot, float)
        self.sensor_14 = np.zeros(AppConstants.samples2plot, float)
        self.sensor_15 = np.zeros(AppConstants.samples2plot, float)
        self.sensor_16 = np.zeros(AppConstants.samples2plot, float)

        # declaration of each sensor plot
        self.plot_sensor_1 = self.plot_graph.graphComponent.plot()
        self.plot_sensor_2 = self.plot_graph.graphComponent.plot()
        self.plot_sensor_3 = self.plot_graph.graphComponent.plot()
        self.plot_sensor_4 = self.plot_graph.graphComponent.plot()
        self.plot_sensor_5 = self.plot_graph.graphComponent.plot()
        self.plot_sensor_6 = self.plot_graph.graphComponent.plot()
        self.plot_sensor_7 = self.plot_graph.graphComponent.plot()
        self.plot_sensor_8 = self.plot_graph.graphComponent.plot()
        self.plot_sensor_9 = self.plot_graph.graphComponent.plot()
        self.plot_sensor_10 = self.plot_graph.graphComponent.plot()
        self.plot_sensor_11 = self.plot_graph.graphComponent.plot()
        self.plot_sensor_12 = self.plot_graph.graphComponent.plot()
        self.plot_sensor_13 = self.plot_graph.graphComponent.plot()
        self.plot_sensor_14 = self.plot_graph.graphComponent.plot()
        self.plot_sensor_15 = self.plot_graph.graphComponent.plot()
        self.plot_sensor_16 = self.plot_graph.graphComponent.plot()

        # plot point to number of 'screens'
        self.ptr = 0
        # configures
        self._configure_plot()

    def _configure_plot(self):
        """
        - setup specific elements of the PyQtGraph plot
        - no return
        """
        # self.ui.plt.setBackground(background=None)
        # self.ui.plt.setAntialiasing(True)
        # self._plt = self.ui.plt.addPlot(row=1, col=1)
        # self._plt.setLabel('bottom', Constants.plot_xlabel_title, Constants.plot_xlabel_unit)

        # title
        self.plot_graph.graphComponent.setTitle(AppConstants.app_plot_title, size='16pt', color='#FFFFFF', bold=True)

        # x axi label
        self.plot_graph.graphComponent.setLabel('left', AppConstants.plot_y_label, AppConstants.plot_y_label_unit,
                                                color='white', size=40)

        # x axi range
        axi_x_ticks = [0, 1, 2, 3, 4, 5, 6, 7]
        # self.plot_graph.graphComponent.PlotWidget.AxisItem('bottom')  # , showValues=True)

        # y axi label
        self.plot_graph.graphComponent.setLabel('bottom', AppConstants.plot_x_label, AppConstants.plot_x_label_unit,
                                                color='white', size=40)
        # grid ON (TRUE)
        self.plot_graph.graphComponent.showGrid(x=True, y=True, alpha=0.3)

    def _connect_signals_to_methods(self):
        """
        - make up the connections between signals and UI elements
        - no return
        """
        self.plot_graph.sendButton.clicked.connect(self._write2leds)
        self.plot_graph.pB_Start.clicked.connect(self._start_acq)
        self.plot_graph.pB_Stop.clicked.connect(self._stop_acq)
        # self.plot_graph.cBox_CommSpeed.activated[str].connect(self._baud_rate_sel) # currentIndexChanged
        self.plot_graph.cBox_CommSpeed.currentIndexChanged.connect(self.baud_rate_sel) # currentIndexChanged


    def _write2leds(self):
        leds = [self.plot_graph.led8_2,
                self.plot_graph.led7_2,
                self.plot_graph.led6_2,
                self.plot_graph.led5_2,
                self.plot_graph.led4_2,
                self.plot_graph.led3_2,
                self.plot_graph.led2_2,
                self.plot_graph.led1_2]
        position = 0
        result = 0
        for led in leds:
            if led.isChecked():
                result += 2 ** position

            position += 1

        self.plot_graph.ledInformation.append(
            '<h1>LEDs Value ==>  Integer: {0:d}  -  Binary: {0:b}</h1>'.format(result))

        self.rx_tx_ctrl.zedboard.setGPIOS(result)

    def _configure_timers(self):
        """
        - Configures timers to be used for the plot (samples/sec)
        - return: none
        """
        self._timer_plot = QtCore.QTimer(self)
        self._timer_plot.timeout.connect(self._update_plot)
        # self.timer = QtCore.QTimer()

    def _start_acq(self):
        """
        - start the acquisition of data
        - associated to the 'Start' button.
        - no return
        """
        LogManager.i(TAG, "Start Button Clicked")
        self.plot_graph.pButton_Status.setStyleSheet("background-color: green")
        # self._timer_plot.timeout.connect(self.timeout_reached)
        self._timer_plot.start(AppConstants.t_bt_samples)  # n in msec, time between readings

    def _stop_acq(self):
        LogManager.i(TAG, "Stop Button Clicked")
        if self._timer_plot:
            self.plot_graph.pButton_Status.setStyleSheet("background-color: red")
            self._timer_plot.stop()

    def baud_rate_sel(self, i):
        LogManager.i(TAG, "Baud Rate Change")
        # for count in range(self.plot_graph.cBox_CommSpeed.count()):
        #     print(self.plot_graph.cBox_CommSpeed.itemText(count))
        print("Current index", i, "selection changed ", self.plot_graph.cBox_CommSpeed.currentText())
        current_baud_rate = self.plot_graph.cBox_CommSpeed.currentText()
        return current_baud_rate

    def _update_plot(self):
        """
         - plots the input signals, and update them with a new value every s and redraws the graphics in the plot.
         - self._timer_plot.timeout.connect(self._update_plot) time
         - no return
         """
        # global ptr

        self.ptr += 1

        t_initial = time.time()
        tic = time.perf_counter()
        # received_data = []
        received_data = self.rx_tx_ctrl.zedboard.read_temperature_sensor(AppConstants.number_sensors)
        # print(received_data[0])
        # print(received_data[1])
        # print(received_data[2])

        # sensor 1
        self.sensor_1[:-1] = self.sensor_1[1:]
        self.sensor_1[-1] = received_data[0]
        if self.plot_graph.chBox_1.isChecked():
            self.plot_sensor_1.setData(self.sensor_1, pen=AppConstants.plot_colors['s1'])  # 'r')  # QPen(QColor(255, 0, 255)), width=1)        # 'r')
            self.plot_sensor_1.setPos(self.ptr, 0)
        else:
            self.plot_sensor_1.setData(self.sensor_1, pen=None)
            self.plot_sensor_1.setPos(self.ptr, 0)

        # sensor 2
        self.sensor_2[:-1] = self.sensor_2[1:]
        self.sensor_2[-1] = (received_data[1])
        if self.plot_graph.chBox_2.isChecked():
            self.plot_sensor_2.setData(self.sensor_2, pen=AppConstants.plot_colors['s2'])
            self.plot_sensor_2.setPos(self.ptr, 0)
        else:
            self.plot_sensor_2.setData(self.sensor_2, pen=None)
            self.plot_sensor_2.setPos(self.ptr, 0)

        # self.plot_sensor_2.setData(self.sensor_2, pen='g')

        # sensor 3
        self.sensor_3[:-1] = self.sensor_3[1:]
        self.sensor_3[-1] = (received_data[2])
        if self.plot_graph.chBox_3.isChecked():
            self.plot_sensor_3.setData(self.sensor_3, pen=AppConstants.plot_colors['s3'])
            self.plot_sensor_3.setPos(self.ptr, 0)
        else:
            self.plot_sensor_3.setData(self.sensor_3, pen=None)
            self.plot_sensor_3.setPos(self.ptr, 0)

        # self.plot_sensor_3.setData(self.sensor_3, pen='y')
        #
        # sensor 4
        self.sensor_4[:-1] = self.sensor_4[1:]
        self.sensor_4[-1] = received_data[3]
        if self.plot_graph.chBox_4.isChecked():
            self.plot_sensor_4.setData(self.sensor_4, pen=AppConstants.plot_colors['s4'])
            self.plot_sensor_4.setPos(self.ptr, 0)
        else:
            self.plot_sensor_4.setData(self.sensor_4, pen=None)
            self.plot_sensor_4.setPos(self.ptr, 0)

        #
        # sensor 5
        self.sensor_5[:-1] = self.sensor_5[1:]
        self.sensor_5[-1] = (received_data[4])
        if self.plot_graph.chBox_5.isChecked():
            self.plot_sensor_5.setData(self.sensor_5, pen=AppConstants.plot_colors['s5'])
            self.plot_sensor_5.setPos(self.ptr, 0)
        else:
            self.plot_sensor_5.setData(self.sensor_5, pen=None)
            self.plot_sensor_5.setPos(self.ptr, 0)
        # # self.plot_sensor_2.setData(self.sensor_2, pen='g')
        #
        # sensor 6
        self.sensor_6[:-1] = self.sensor_6[1:]
        self.sensor_6[-1] = (received_data[5])
        if self.plot_graph.chBox_6.isChecked():
            self.plot_sensor_6.setData(self.sensor_6, pen=AppConstants.plot_colors['s6'])
            self.plot_sensor_6.setPos(self.ptr, 0)
        else:
            self.plot_sensor_6.setData(self.sensor_6, pen=None)
            self.plot_sensor_6.setPos(self.ptr, 0)
        #
        # sensor 7
        self.sensor_7[:-1] = self.sensor_7[1:]
        self.sensor_7[-1] = received_data[6]
        if self.plot_graph.chBox_7.isChecked():
            self.plot_sensor_7.setData(self.sensor_7, pen=AppConstants.plot_colors['s7'])
            self.plot_sensor_7.setPos(self.ptr, 0)
        else:
            self.plot_sensor_7.setData(self.sensor_7, pen=None)
            self.plot_sensor_7.setPos(self.ptr, 0)
        #
        # sensor 8
        self.sensor_8[:-1] = self.sensor_8[1:]
        self.sensor_8[-1] = (received_data[7])
        if self.plot_graph.chBox_8.isChecked():
            self.plot_sensor_8.setData(self.sensor_8, pen=AppConstants.plot_colors['s8'])
            self.plot_sensor_8.setPos(self.ptr, 0)
        else:
            self.plot_sensor_8.setData(self.sensor_8, pen=None)
            self.plot_sensor_8.setPos(self.ptr, 0)

        # # self.plot_sensor_2.setData(self.sensor_2, pen='g')
        #
        # sensor 9
        self.sensor_9[:-1] = self.sensor_9[1:]
        self.sensor_9[-1] = (received_data[8])
        if self.plot_graph.chBox_9.isChecked():
            self.plot_sensor_9.setData(self.sensor_9, pen=AppConstants.plot_colors['s9'])
            self.plot_sensor_9.setPos(self.ptr, 0)
        else:
            self.plot_sensor_9.setData(self.sensor_9, pen=None)
            self.plot_sensor_9.setPos(self.ptr, 0)
        # # self.plot_sensor_3.setData(self.sensor_3, pen='y')
        #
        # sensor 10
        self.sensor_10[:-1] = self.sensor_10[1:]
        self.sensor_10[-1] = received_data[9]
        if self.plot_graph.chBox_10.isChecked():
            self.plot_sensor_10.setData(self.sensor_10, pen=AppConstants.plot_colors['s10'])
            self.plot_sensor_10.setPos(self.ptr, 0)
        else:
            self.plot_sensor_10.setData(self.sensor_10, pen=None)
            self.plot_sensor_10.setPos(self.ptr, 0)
        #
        # sensor 11
        self.sensor_11[:-1] = self.sensor_11[1:]
        self.sensor_11[-1] = (received_data[10])
        if self.plot_graph.chBox_11.isChecked():
            self.plot_sensor_11.setData(self.sensor_11, pen=AppConstants.plot_colors['s11'])
            self.plot_sensor_11.setPos(self.ptr, 0)
        else:
            self.plot_sensor_11.setData(self.sensor_11, pen=None)
            self.plot_sensor_11.setPos(self.ptr, 0)
        # # self.plot_sensor_2.setData(self.sensor_2, pen='g')
        #
        # sensor 12
        self.sensor_12[:-1] = self.sensor_12[1:]
        self.sensor_12[-1] = (received_data[11])
        if self.plot_graph.chBox_12.isChecked():
            self.plot_sensor_12.setData(self.sensor_12, pen=AppConstants.plot_colors['s12'])
            self.plot_sensor_12.setPos(self.ptr, 0)
        else:
            self.plot_sensor_12.setData(self.sensor_12, pen=None)
            self.plot_sensor_12.setPos(self.ptr, 0)
        #
        # sensor 13
        self.sensor_13[:-1] = self.sensor_13[1:]
        self.sensor_13[-1] = received_data[12]
        if self.plot_graph.chBox_13.isChecked():
            self.plot_sensor_13.setData(self.sensor_13, pen=AppConstants.plot_colors['s13'])
            self.plot_sensor_13.setPos(self.ptr, 0)
        else:
            self.plot_sensor_13.setData(self.sensor_13, pen=None)
            self.plot_sensor_13.setPos(self.ptr, 0)
        #
        # sensor 14
        self.sensor_14[:-1] = self.sensor_14[1:]
        self.sensor_14[-1] = (received_data[13])
        if self.plot_graph.chBox_14.isChecked():
            self.plot_sensor_14.setData(self.sensor_14, pen=AppConstants.plot_colors['s14'])
            self.plot_sensor_14.setPos(self.ptr, 0)
        else:
            self.plot_sensor_14.setData(self.sensor_14, pen=None)
            self.plot_sensor_14.setPos(self.ptr, 0)
        # # self.plot_sensor_2.setData(self.sensor_2, pen='g')
        #
        # sensor 15
        self.sensor_15[:-1] = self.sensor_15[1:]
        self.sensor_15[-1] = (received_data[14])
        if self.plot_graph.chBox_15.isChecked():
            self.plot_sensor_15.setData(self.sensor_15, pen=AppConstants.plot_colors['s15'])
            self.plot_sensor_15.setPos(self.ptr, 0)
        else:
            self.plot_sensor_15.setData(self.sensor_15, pen=None)
            self.plot_sensor_15.setPos(self.ptr, 0)
        #
        # sensor 16
        self.sensor_16[:-1] = self.sensor_16[1:]
        self.sensor_16[-1] = (received_data[15])
        if self.plot_graph.chBox_16.isChecked():
            self.plot_sensor_16.setData(self.sensor_16, pen=AppConstants.plot_colors['s16'])
            self.plot_sensor_16.setPos(self.ptr, 0)
        else:
            self.plot_sensor_16.setData(self.sensor_16, pen=None)
            self.plot_sensor_16.setPos(self.ptr, 0)

        # value to LCD display
        self.plot_graph.lcd.display(received_data[0])
        t_final = time.time()
        toc = time.perf_counter()
        print("Plot time:   ", t_final-t_initial)
        print(f"Plot update time {toc-tic:0.4f} sec")


