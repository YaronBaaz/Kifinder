Software for KiFinder. This is created by Yaron Baazov for CompE Design Project.

The demo must be started in the SimpleMFRC522-python Folder.


To enable UART for GPS you must first enable UART on the PI

1)In terminal write:

sudo raspi-config

2) Select the "5 Interfacing Options"

3) Select th "P6 Serial

4) When asked for login press "<No>"

5) When asked for hardware to be enabled press "<Yes>"

6) Press "<Ok>"


To check if enabled, in terminal write

	ls -l /dev

should see after some scrolling "serial0 -> ttyS0" on the right hand side, with serial0 in cyan in and ttyS0 in yellow.

ATTRIBUTION

RFID code was given by Fraida Fund in the lab manual.
The base for the location code was found in electricwings
