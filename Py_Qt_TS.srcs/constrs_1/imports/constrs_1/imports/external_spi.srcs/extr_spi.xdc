#MOSI
set_property PACKAGE_PIN AA11 [get_ports spi_rtl_io0_io]
#MISO
set_property PACKAGE_PIN Y10 [get_ports spi_rtl_io1_io]
#SCLK
set_property PACKAGE_PIN AA9 [get_ports spi_rtl_sck_io]
#SS
set_property PACKAGE_PIN Y11 [get_ports {spi_rtl_ss_io[0]}]


set_property IOSTANDARD LVCMOS33 [get_ports {spi_rtl_*}]

set_property PULLDOWN true [get_ports {spi_rtl_*}]









