#  from PyQt5 import QtGui, QtCore
# import numpy as np
# import serial
import sys
from PyQt5 import QtWidgets  # QtGui, QtCore
import logging
import logging.handlers
from log_file_manager.log_write import LogManager

from ui import Ui_plot_view
# from zedboard_rd_wr.zed_rd_wr import ZedboardController
# from plot_control.sensors_plot import PlotController
from serial_com.serial_setup import SerialSetup
from plot_control import sensors_plot
# from log_file_manager.log_write import LogManager as Log
from log_file_manager.arguments import *

# from ui.interfaz import Ui_Dialog


# class ZedboardController:
#     def __init__(self, transceiver):
#         self.transceiver = transceiver
#
#     def setGPIOS(self, value):
#         str_value = format(value, '03d')  # related to: scanf("%3s", state);
#         print(str_value)
#         self.transceiver.write('wr_leds{}\n'.format(str_value).encode())  # write LEDs
#         self.transceiver.flushOutput()
#
#     def read_temperature_sensor(self, num_samples):
#         temp_data = []
#         for i in range(num_samples):
#             self.transceiver.write("rd_temp\n".encode())  # read temperature
#             self.transceiver.flushOutput()
#             data = self.transceiver.read(AppConstants.bytes2read)  # 7 Related to: printf("%2.4f", temperature);
#             print(data)
#             temp_data.append(float(data.decode()))
#
#         return temp_data
# class SerialTxRx:
#     def __init__(self):
#         self.transceiver = serial.Serial(AppConstants.comm_port, baudrate=AppConstants.default_baudrate)
#         self.zedboard = ZedboardController(self.transceiver)

# class Controller:
#     def __init__(self, interface, rx_tx_ctrl):
#         self.timer = QtCore.QTimer()
#         self.interface = interface
#         self.rx_tx_ctrl = rx_tx_ctrl
#         # self.transceiver = serial.Serial('/dev/ttyACM0', baudrate=115200)
#         # self.zedboard = ZedboardController(self.transceiver)
#         self.connect_signals_to_methods()
#         self.dataY_1 = np.zeros(AppConstants.samples2plot)
#         self.dataY_2 = np.zeros(AppConstants.samples2plot)
#         self.dataY_3 = np.zeros(AppConstants.samples2plot)
#         self.line_y1 = self.interface.graphComponent.plot()
#         self.line_y2 = self.interface.graphComponent.plot()
#         self.line_y3 = self.interface.graphComponent.plot()
#
#     def connect_signals_to_methods(self):
#         self.interface.sendButton.clicked.connect(self.led_button_clicked)
#         self.interface.start.clicked.connect(self.start_button_clicked)
#         self.interface.stop.clicked.connect(self.stop_button_clicked)
#
#     def led_button_clicked(self):
#         leds = [self.interface.led8_2,
#                 self.interface.led7_2,
#                 self.interface.led6_2,
#                 self.interface.led5_2,
#                 self.interface.led4_2,
#                 self.interface.led3_2,
#                 self.interface.led2_2,
#                 self.interface.led1_2]
#         position = 0
#         result = 0
#         for led in leds:
#             if led.isChecked():
#                 result += 2 ** position
#
#             position += 1
#
#         self.interface.ledInformation.append('<h1>LEDs Actual Value: int: {0:d} - bin: {0:b}</h1>'.format(result))
#
#         self.rx_tx_ctrl.zedboard.setGPIOS(result)
#
#     def start_button_clicked(self):
#         self.interface.status.setStyleSheet("background-color: green")
#         self.timer.timeout.connect(self.timeout_reached)
#         self.timer.start(AppConstants.t_msec)  # n in msec, time between readings
#
#     def stop_button_clicked(self):
#         if self.timer:
#             self.interface.status.setStyleSheet("background-color: red")
#             self.timer.stop()
#
#     def timeout_reached(self):
#         received_data = self.rx_tx_ctrl.zedboard.read_temperature_sensor(AppConstants.number_samples)
#         print(received_data)
#         # channel 1
#         self.dataY_1[:-1] = self.dataY_1[1:]
#         self.dataY_1[-1] = received_data[0]
#         self.line_y1.setData(self.dataY_1, pen='r')
#
#         # channel 2
#         self.dataY_2[:-1] = self.dataY_2[1:]
#         self.dataY_2[-1] = (received_data[0])-1
#         self.line_y2.setData(self.dataY_2, pen='g')
#
#         # channel 3
#         self.dataY_3[:-1] = self.dataY_3[1:]
#         self.dataY_3[-1] = (received_data[0])+1
#         self.line_y3.setData(self.dataY_3, pen='y')
#
#         # value to LCD display
#         self.interface.lcd.display(received_data[0])

TAG = "RealTimePlots"

#
# def main():
#     _args = _init_logger()
#     qt_app = QtWidgets.QApplication([])
#     main_window = QtWidgets.QWidget()
#     my_interface = Ui_plot_view.Ui_plot_view()
#     my_interface.setupUi(main_window)
#     zed_serial_ctrl = SerialSetup() # my_interface)
#     t = sensors_plot.PlotController(my_interface, zed_serial_ctrl)
#     main_window.show()
#     qt_app.exec_()
#
#
# def _init_logger():
#     args = Arguments()
#     args.create()
#     args.set_user_log_level()
#     return args
#
#
# if __name__ == '__main__':
#     main()

class RTPlot:
    def __init__(self, argv=sys.argv):
        self._args = self._init_logger()
        self._qt_app = QtWidgets.QApplication([])

    def run(self):
        LogManager.i(TAG, "Starting RTPlot")
        main_window = QtWidgets.QWidget()
        my_interface = Ui_plot_view.Ui_plot_view()
        my_interface.setupUi(main_window)
        zed_serial_ctrl = SerialSetup() # my_interface)
        t = sensors_plot.PlotController(my_interface, zed_serial_ctrl)
        main_window.show()
        self._qt_app.exec_()
        LogManager.i(TAG, "Finishing RTPlot\n")
        main_window.close()

    @staticmethod
    def _init_logger():
        args = Arguments()
        args.create()
        args.set_user_log_level()
        return args


if __name__ == '__main__':
    RTPlot().run()
