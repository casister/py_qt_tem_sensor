import time
from constants.plot_graph_constants import AppConstants


class ZedboardController:
    def __init__(self, transceiver):
        self.transceiver = transceiver

    def setGPIOS(self, value):
        str_value = format(value, '03d')  # related to: scanf("%3s", state);
        print(str_value)
        self.transceiver.write('wr_leds{}\n'.format(str_value).encode())  # write to LEDs 'command'
        self.transceiver.flushOutput()

    def read_temperature_sensor(self, num_samples):
        temp_data = []
        # for i in range(num_samples):
        self.transceiver.write("rd_temp\n".encode())  # read temperature 'command'
        t_i = time.time()
        for i in range(num_samples):
            self.transceiver.flushOutput()
            data = self.transceiver.read(AppConstants.bytes2read)  # 7 Related to: printf("%2.4f", temperature);
            # print(data)
            temp_data.append(float(data.decode()))
            # print(temp_data, i)

        t_f = time.time()
        print("serial rx:  ", t_f-t_i)
        return temp_data