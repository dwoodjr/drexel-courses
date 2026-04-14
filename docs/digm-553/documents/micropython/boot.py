# boot.py — runs once at power-on, before code.py
# Enables the USB CDC data channel so usb_cdc.data is available in code.py

import usb_cdc

usb_cdc.enable(console=True, data=True)