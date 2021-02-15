connect -url tcp:127.0.0.1:3121
source /mnt/data/projects/py_qt_temp_sensor/Py_Qt_TS.sdk/design_1_wrapper_hw_platform_0/ps7_init.tcl
targets -set -nocase -filter {name =~"APU*" && jtag_cable_name =~ "Digilent Zed 210248A397F3"} -index 0
loadhw -hw /mnt/data/projects/py_qt_temp_sensor/Py_Qt_TS.sdk/design_1_wrapper_hw_platform_0/system.hdf -mem-ranges [list {0x40000000 0xbfffffff}]
configparams force-mem-access 1
targets -set -nocase -filter {name =~"APU*" && jtag_cable_name =~ "Digilent Zed 210248A397F3"} -index 0
stop
ps7_init
ps7_post_config
targets -set -nocase -filter {name =~ "ARM*#0" && jtag_cable_name =~ "Digilent Zed 210248A397F3"} -index 0
rst -processor
targets -set -nocase -filter {name =~ "ARM*#0" && jtag_cable_name =~ "Digilent Zed 210248A397F3"} -index 0
dow /mnt/data/projects/py_qt_temp_sensor/Py_Qt_TS.sdk/Py_Qt_TS/Debug/Py_Qt_TS.elf
configparams force-mem-access 0
targets -set -nocase -filter {name =~ "ARM*#0" && jtag_cable_name =~ "Digilent Zed 210248A397F3"} -index 0
con
