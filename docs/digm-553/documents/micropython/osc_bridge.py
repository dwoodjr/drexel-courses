# DIGM 553 — Serial to OSC bridge
# Reads MPR121 touch data from RP2040 USB serial, forwards as OSC to Unity
#
# Requires: pip install pyserial python-osc

import serial
import time
from pythonosc import udp_client

# ── CONFIGURE THESE ────────────────────────────────────────────────────────────
SERIAL_PORT = "COM7"   # ← CHANGE THIS to your data port
BAUD_RATE   = 115200
UNITY_IP    = "192.168.1.156"             # 127.0.0.1 = same computer as Unity
UNITY_PORT  = 9000                    # Must match the Local Port in Unity's OSC Receiver
# ───────────────────────────────────────────────────────────────────────────────

client = udp_client.SimpleUDPClient(UNITY_IP, UNITY_PORT)

print(f"Connecting to {SERIAL_PORT}...")
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
print("Connected. Listening for touch data...")
print("Press Ctrl+C to stop.\n")

while True:
    try:
        line = ser.readline().decode("utf-8").strip()
        if not line:
            continue

        parts = line.split(",")
        if len(parts) < 3:
            continue

        event      = parts[0]           # TOUCH, RELEASE, or RAW
        electrode  = int(parts[1])      # 0–11
        raw        = int(parts[2])      # capacitance value

        if event == "TOUCH":
            client.send_message(f"/touch/{electrode}", 1)
            client.send_message(f"/touch/{electrode}/raw", raw)
            print(f"  TOUCH  pad {electrode:2d}  raw={raw}")

        elif event == "RELEASE":
            client.send_message(f"/touch/{electrode}", 0)
            client.send_message(f"/touch/{electrode}/raw", raw)
            print(f"  RELEASE pad {electrode:2d}  raw={raw}")

        elif event == "RAW":
            client.send_message(f"/touch/{electrode}/raw", raw)

    except KeyboardInterrupt:
        print("\nStopping bridge.")
        ser.close()
        break
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(0.1)