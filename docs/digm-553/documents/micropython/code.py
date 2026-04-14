# DIGM 553 — Signal Chain: MPR121 capacitive touch → USB serial
# Adafruit QT Py RP2040 + MPR121 12-key capacitive touch sensor
# Sends touch/release events AND raw capacitance over USB for the OSC bridge

import board
import busio
import usb_cdc
import time
import adafruit_mpr121 # type: ignore

# ── SETUP ─────────────────────────────────────────────────────────────────────

i2c = busio.I2C(board.SCL1, board.SDA1)
mpr = adafruit_mpr121.MPR121(i2c)   # Default I2C address 0x5A

serial = usb_cdc.data              # USB serial data channel

# ── MAIN LOOP ─────────────────────────────────────────────────────────────────

last_touched = mpr.touched()

while True:
    current = mpr.touched()

    for i in range(12):
        bit = 1 << i
        was = last_touched & bit
        now = current & bit

        # Raw capacitance: baseline minus filtered (higher = more touch pressure)
        baseline = mpr.baseline_data(i)
        filtered = mpr.filtered_data(i)
        raw = baseline - filtered  # 0 at rest, increases with touch

        if not was and now:
            msg = f"TOUCH,{i},{raw}\n"
            serial.write(msg.encode())

        elif was and not now:
            msg = f"RELEASE,{i},{raw}\n"
            serial.write(msg.encode())

        elif now:
            # Continuous data while held — comment out if too noisy
            msg = f"RAW,{i},{raw}\n"
            serial.write(msg.encode())

    last_touched = current
    time.sleep(0.01)   # 100Hz polling