"""
amg8833_synth.py
================
A pretend AMG8833 thermal sensor that talks over a (virtual) serial port.

This script does NOT need any hardware. It writes to a serial COM port the
*exact same bytes* your real AMG8833 sketch on the QT Py RP2040 sends over
USB serial:

    amg,<row_index>,<v0>,<v1>,<v2>,<v3>,<v4>,<v5>,<v6>,<v7>\n

Eight lines per frame (one per row of the 8x8 grid), ~10 frames per second.

How this fits in:

    [ amg8833_synth.py ]  --writes-->  [ COM10 ]
                                          |         (virtual cable created
                                          |          by com0com on Windows
                                          |          or socat on macOS)
                                          v
    [ TouchDesigner Serial DAT ] --reads-- [ COM11 ]

You set up com0com (Windows) or socat (macOS) once, which gives you a pair of
linked virtual ports. This script writes to one side; TouchDesigner reads from
the other. No hardware needed.

When you eventually use the real QT Py, the only thing that changes in TD is
the port number (e.g. COM5 instead of COM11). Same Serial DAT, same parser,
same image network.

----------
First-time setup (Windows)
----------
1. Install com0com:
     https://sourceforge.net/projects/com0com/
   Use the "Setup" tool to create a port pair, e.g. COM10 <-> COM11.
2. Install pyserial:
     pip install pyserial
   (or, on Windows: py -m pip install pyserial)
3. Run this script, pointing at one side of the pair:
     python amg8833_synth.py COM10
4. In TouchDesigner, open a Serial DAT on the OTHER side (COM11).

----------
First-time setup (macOS / Linux)
----------
1. Install socat:
     brew install socat        # macOS with Homebrew
2. Install pyserial:
     pip install pyserial
3. In a separate terminal, create a virtual port pair:
     socat -d -d pty,raw,echo=0 pty,raw,echo=0
   socat will print two device paths, e.g. /dev/ttys001 and /dev/ttys002.
4. Run this script on one side:
     python amg8833_synth.py /dev/ttys001
5. In TouchDesigner, open a Serial DAT on the other side (/dev/ttys002).

Stop the script with Ctrl+C in its terminal.
"""

import math
import random
import sys
import time

try:
    import serial  # pyserial
except ImportError:
    print(
        "[amg8833_synth] pyserial isn't installed.\n"
        "  Install it with one of:\n"
        "    pip install pyserial\n"
        "    py -m pip install pyserial   (Windows)\n"
        "    python3 -m pip install pyserial  (macOS/Linux)"
    )
    sys.exit(1)

# ---------------------------------------------------------------------------
# Settings you can tweak
# ---------------------------------------------------------------------------

DEFAULT_PORT = "COM10"   # used if you don't pass one on the command line
BAUD_RATE = 115200       # match this to your TD Serial DAT
FRAME_HZ = 10.0          # how many frames per second (real AMG8833 ~10Hz)

AMBIENT_C = 22.0     # baseline room temperature in Celsius
AMBIENT_NOISE = 0.15 # tiny random jitter on every cell, in Celsius
HOTSPOT_PEAK = 10.0  # how much hotter than ambient the "hand" gets
HOTSPOT_RADIUS = 1.6 # how spread out the hotspot is, in grid cells

# ---------------------------------------------------------------------------
# Synthesizing one frame of fake thermal data
# ---------------------------------------------------------------------------

def build_frame(t):
    """
    Return an 8x8 list-of-lists of temperatures (degrees C) for time t.

    The grid is mostly ambient room temperature with a little noise, plus
    a 2D Gaussian "hand" hotspot whose center moves in a slow circle.
    """
    cx = 3.5 + 2.5 * math.cos(t * 0.8)
    cy = 3.5 + 2.5 * math.sin(t * 0.6)

    grid = []
    for row in range(8):
        row_values = []
        for col in range(8):
            dx = col - cx
            dy = row - cy
            dist_sq = dx * dx + dy * dy

            hotspot = HOTSPOT_PEAK * math.exp(
                -dist_sq / (2 * HOTSPOT_RADIUS * HOTSPOT_RADIUS)
            )
            noise = random.uniform(-AMBIENT_NOISE, AMBIENT_NOISE)
            row_values.append(AMBIENT_C + hotspot + noise)
        grid.append(row_values)
    return grid


def frame_to_bytes(grid):
    """
    Convert an 8x8 grid into the byte string the real sensor would send.

    Format (one line per row, terminated with \\n):
        amg,<row_index>,<v0>,<v1>,<v2>,<v3>,<v4>,<v5>,<v6>,<v7>\\n
    """
    lines = []
    for row_idx, row in enumerate(grid):
        values = ",".join(f"{v:.1f}" for v in row)
        lines.append(f"amg,{row_idx},{values}\n")
    return "".join(lines).encode("utf-8")


# ---------------------------------------------------------------------------
# Main loop: open the port, stream frames, close on Ctrl+C
# ---------------------------------------------------------------------------

def stream(port_name):
    try:
        ser = serial.Serial(port_name, baudrate=BAUD_RATE, timeout=1)
    except serial.SerialException as e:
        print(f"[amg8833_synth] could not open {port_name}: {e}")
        print("  - On Windows, confirm com0com is installed and the port pair exists.")
        print("  - Make sure nothing else (TD, Arduino IDE Serial Monitor) has the port open.")
        sys.exit(1)

    print(f"[amg8833_synth] writing to {port_name} @ {BAUD_RATE} baud  (Ctrl+C to stop)")
    print(f"[amg8833_synth] open the OTHER side of the pair in TouchDesigner's Serial DAT")

    frame_period = 1.0 / FRAME_HZ
    t0 = time.time()

    try:
        while True:
            t = time.time() - t0
            grid = build_frame(t)
            payload = frame_to_bytes(grid)
            try:
                ser.write(payload)
                ser.flush()
            except serial.SerialException as e:
                print(f"[amg8833_synth] write error: {e}")
                break
            time.sleep(frame_period)
    except KeyboardInterrupt:
        print("\n[amg8833_synth] stopped")
    finally:
        try:
            ser.close()
        except Exception:
            pass


if __name__ == "__main__":
    # Take the port name from the command line if given, else use DEFAULT_PORT.
    #     python amg8833_synth.py COM10
    #     python amg8833_synth.py /dev/ttys001
    port = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_PORT
    stream(port)
