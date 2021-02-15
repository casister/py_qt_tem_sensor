import serial
from constants.plot_graph_constants import AppConstants
from zedboard_rd_wr.zed_rd_wr import ZedboardController


class SerialSetup:
    def __init__(self):
        self.transceiver = serial.Serial(AppConstants.comm_port, baudrate=AppConstants.default_baudrate)
        self.zedboard = ZedboardController(self.transceiver)