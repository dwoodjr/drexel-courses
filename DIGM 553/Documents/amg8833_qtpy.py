# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
#
# DIGM 553 — modified from the Adafruit AMG88xx example so that each row
# prints as a single, machine-readable line that TouchDesigner's Serial
# DAT can parse cleanly. The format is:
#
#     amg,<row_index>,<v0>,<v1>,<v2>,<v3>,<v4>,<v5>,<v6>,<v7>
#
# (Followed by the newline that print() automatically adds.)
#
# To install: copy this file onto your QT Py's CIRCUITPY drive and rename
# it to code.py. CircuitPython will auto-run it on every reset.

import time
import board
import busio
import adafruit_amg88xx

i2c = busio.I2C(board.SCL, board.SDA)
amg = adafruit_amg88xx.AMG88XX(i2c)

while True:
    # amg.pixels is a list of 8 lists, each holding 8 floats (degrees C).
    for row_idx, row in enumerate(amg.pixels):
        values = ",".join(f"{temp:.1f}" for temp in row)
        print(f"amg,{row_idx},{values}")
    time.sleep(0.1)  # ~10 frames per second
