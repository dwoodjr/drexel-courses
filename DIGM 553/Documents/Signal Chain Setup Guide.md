---
title: "Signal Chain Setup Guide"
tags: [DIGM553, hardware, circuitpython, osc, setup]
---
# Signal Chain Setup Guide

> Getting your microcontroller talking to your computer. From unboxing to OSC data flowing into Max, TouchDesigner, or whatever receives it.

This guide assumes you have hardware in hand. If you're still figuring out *which* sensors match your practice, start with [[Hardware Clarifications — Thinking Toward Sensors|Hardware Clarifications — Thinking Toward Sensors]] first.

---

## Required Hardware

### Microcontroller — Adafruit QT Py RP2040

The **QT Py RP2040** is the course microcontroller. It's tiny, has a built-in **STEMMA QT / Qwiic connector** (the 4-pin JST-SH port on the end of the board), and runs **CircuitPython** cleanly.

Key pins to know:
- **SDA** → GPIO 22 (also labeled `SDA` on the board)
- **SCL** → GPIO 23 (also labeled `SCL`)
- **STEMMA QT port** → directly wired to SDA/SCL — no wiring needed if you use a STEMMA QT cable
- **3.3V and GND** → available on the pin headers for anything that doesn't use STEMMA QT

> [!note] The RP2040 does **not** have built-in WiFi. For OSC communication we use **USB serial** instead of UDP over WiFi. This means: the board sends data over USB to a Python script running on your laptop, and that script forwards it as OSC to Max/MSP or TouchDesigner. See Part 4 for the full code.

---

### Primary Sensor — Adafruit MPR121 12-Key Capacitive Touch

The **MPR121** gives you 12 capacitive touch inputs (labeled `0` through `11`). Each input can be connected to any conductive material — copper tape, conductive thread, metal objects, wire — and the sensor detects when that material is touched.

Key facts:
- **I2C address:** `0x5A` (default). Can be changed to `0x5B`, `0x5C`, or `0x5D` by bridging the `ADDR` jumper pad on the breakout — useful if you need to stack multiple MPR121s on the same bus
- **Connects via STEMMA QT** → one cable, no soldering required for basic use
- **Electrode pads:** The `0`–`11` pads on the breakout are where you attach conductive materials. Alligator clips, solid-core wire, or copper tape all work.
- **CircuitPython library:** `adafruit_mpr121`

---

## Bonus Hardware

### MCP4725 — 12-bit DAC (Digital-to-Analog Converter)

The **MCP4725** converts a digital number (0–4095) into an analog voltage (0–3.3V). Useful for driving a piezo buzzer, analog LED brightness, or sending a control voltage into an analog synth.

- **I2C address:** `0x60` (default; some boards allow `0x61`)
- **Connects via STEMMA QT** → chains onto the same I2C bus as the MPR121
- **CircuitPython library:** `adafruit_mcp4725`
- **Use case in this course:** mapping a touch gesture to an analog voltage — a signal chain that goes *back out* into the physical world

---

### Gikfun DS18B20 — Waterproof Temperature Probe

The **DS18B20** is a waterproof 1-Wire temperature sensor on a probe cable — designed to go into liquid. It reads temperature in Celsius.

- **Protocol:** 1-Wire — uses a single data wire (not I2C, not the STEMMA QT bus)
- **Wiring:** Three wires — red (3.3V), black (GND), yellow or white (data). The data wire **requires a 4.7kΩ pull-up resistor** between data and 3.3V. This is not optional.
- **Any free GPIO pin** can be the data pin
- **CircuitPython libraries:** `adafruit_onewire` (bus layer) + `adafruit_ds18x20` (sensor driver) — both required
- **Use case in this course:** tracking temperature change in a water vessel as materials dissolve — the slight heat from a citric acid reaction is real data that can drive synthesis parameters

---

## Part 1 — Flash CircuitPython onto the QT Py RP2040

CircuitPython is the firmware that lets you write and run Python scripts on the board. You only need to do this once.

### Step 1 — Download the firmware

Go to: **https://circuitpython.org/board/adafruit_qtpy_rp2040/**

Download the latest stable `.uf2` file (green "DOWNLOAD .UF2 NOW" button).

### Step 2 — Enter bootloader mode

1. Hold the **BOOT** button on the QT Py (the small button on the board)
2. While holding it, plug the USB-C cable into the board and your computer
3. Release the BOOT button
4. The board mounts as a USB drive called **`RPI-RP2`**

### Step 3 — Drag and drop

Drag the `.uf2` file you downloaded directly onto the `RPI-RP2` drive. The board will reboot automatically.

### Step 4 — Confirm it worked

After rebooting, the board remounts as a new USB drive called **`CIRCUITPY`**. You should see a `code.py` file and a `lib/` folder. Done.

---

## Part 2 — Install Libraries

CircuitPython uses a `lib/` folder on the `CIRCUITPY` drive. You copy library files there manually — no package manager, no internet connection required on the board.

### Get the library bundle

Download the **Adafruit CircuitPython Bundle** from:
**https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases**

Download the bundle matching your CircuitPython version (e.g., `adafruit-circuitpython-bundle-9.x-mpy-YYYYMMDD.zip`). Unzip it — you'll get a large folder of `.mpy` files.

### Libraries to copy into `lib/`

**For MPR121 (required):**
```
adafruit_mpr121.mpy
```

> [!note] The USB serial → OSC bridge (Part 4) runs on your **laptop**, not the board, so there are no additional CircuitPython libraries needed for OSC itself. The board just sends plain text over USB; the laptop script translates it.

---

## Part 3 — Wire It Up

### MPR121 via STEMMA QT (no soldering)

1. Take a **STEMMA QT / Qwiic cable** (the small 4-pin JST cable — usually included with Adafruit breakouts, or buy separately)
2. Plug one end into the **STEMMA QT port** on the QT Py RP2040
3. Plug the other end into either STEMMA QT port on the **MPR121** breakout
4. That's it. Power and I2C data are all on that cable.

**Attaching electrodes:**
- Clip or solder a wire to any of the `0`–`11` pads on the MPR121
- Connect the other end to your conductive material — copper tape, conductive thread, a metal object, a piece of foil pressed against something
- The sensor detects when conductance at that pad changes (i.e., when a human body or grounded conductor touches it)

---

## Part 4 — The Code

This is a two-part system:
1. **`code.py`** runs on the board — reads the MPR121 and sends data over USB serial
2. **`osc_bridge.py`** runs on your laptop — receives the serial data and forwards it as OSC

---

### Part A — `code.py` (on the board)

Save this as `code.py` on the `CIRCUITPY` drive:

```python
# DIGM 553 — Signal Chain: MPR121 capacitive touch → USB serial
# Adafruit QT Py RP2040 + MPR121 12-key capacitive touch sensor
# Sends touch/release events as plain text over USB for the OSC bridge to forward

import board
import busio
import usb_cdc
import time
import adafruit_mpr121

# ── SETUP ─────────────────────────────────────────────────────────────────────

i2c = busio.I2C(board.SCL, board.SDA)
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

        if not was and now:
            # Electrode just touched — send: TOUCH,<electrode>\n
            msg = f"TOUCH,{i}\n"
            serial.write(msg.encode())

        elif was and not now:
            # Electrode just released — send: RELEASE,<electrode>\n
            msg = f"RELEASE,{i}\n"
            serial.write(msg.encode())

    last_touched = current
    time.sleep(0.01)   # 100Hz polling
```

You also need to enable the USB serial data channel. Create a file called `boot.py` on `CIRCUITPY` with this content:

```python
# boot.py — enables USB serial data channel on RP2040
import usb_cdc
usb_cdc.enable(console=True, data=True)
```

After saving `boot.py`, **unplug and replug the board** for it to take effect.

---

### Part B — `osc_bridge.py` (on your laptop)

This script runs on your computer. It reads the serial data from the board and sends OSC messages to Max/MSP or TouchDesigner.

**Install dependencies first (run once in terminal):**
```
pip install pyserial python-osc
```

Then save and run this script:

```python
# osc_bridge.py — Serial → OSC bridge for DIGM 553 signal chain
# Run this on your laptop while the QT Py RP2040 is connected via USB
# Forwards MPR121 touch events as OSC messages to a local receiver

import serial
import serial.tools.list_ports
from pythonosc import udp_client
import time

# ── CONFIGURATION ─────────────────────────────────────────────────────────────

RECEIVER_IP   = "127.0.0.1"   # Loopback — receiver is on the same machine
RECEIVER_PORT = 8000           # Port Max/MSP or TouchDesigner is listening on
BAUD_RATE     = 115200

# ── FIND THE BOARD ────────────────────────────────────────────────────────────

def find_qtpy_port():
    """Auto-detect the QT Py serial port."""
    ports = serial.tools.list_ports.comports()
    for p in ports:
        if "CircuitPython" in p.description or "QT Py" in p.description:
            return p.device
    # Fallback: list all ports and pick the most likely one
    if ports:
        print("Could not auto-detect QT Py. Available ports:")
        for i, p in enumerate(ports):
            print(f"  [{i}] {p.device} — {p.description}")
        idx = int(input("Enter number: "))
        return ports[idx].device
    raise RuntimeError("No serial ports found. Is the board plugged in?")

# ── MAIN ──────────────────────────────────────────────────────────────────────

port = find_qtpy_port()
print(f"Connecting to board on {port}...")

osc = udp_client.SimpleUDPClient(RECEIVER_IP, RECEIVER_PORT)

with serial.Serial(port, BAUD_RATE, timeout=1) as ser:
    print(f"Connected. Forwarding OSC to {RECEIVER_IP}:{RECEIVER_PORT}")
    print("Touch the electrodes.\n")

    while True:
        line = ser.readline().decode("utf-8", errors="ignore").strip()
        if not line:
            continue

        parts = line.split(",")
        if len(parts) == 2:
            event, electrode = parts[0], parts[1]
            try:
                idx = int(electrode)
                if event == "TOUCH":
                    osc.send_message(f"/mpr121/{idx}/touch", 1)
                    print(f"→ OSC  /mpr121/{idx}/touch  1")
                elif event == "RELEASE":
                    osc.send_message(f"/mpr121/{idx}/touch", 0)
                    print(f"→ OSC  /mpr121/{idx}/touch  0")
            except ValueError:
                pass
```

**To run it:**
```
python osc_bridge.py
```

Leave it running in the background while you work in Max or TouchDesigner.

---

## Part 5 — Receiving OSC

### In Max/MSP

1. Create a `[udpreceive 8000]` object
2. Connect it to `[oscparse]`
3. Route the output with `[route /mpr121/0/touch /mpr121/1/touch]` etc.

**Minimal patch:**
```
[udpreceive 8000]
       |
  [oscparse]
       |
  [route /mpr121/0/touch /mpr121/1/touch]
```

### In TouchDesigner

1. Add an **OSC In DAT** node
2. Set **Network Port** to `8000`
3. The DAT table will populate with incoming OSC messages as they arrive
4. Route values using **DAT Execute** or an **OSC In CHOP**

---

## Troubleshooting

**Board not showing up as `CIRCUITPY` drive**
→ Try a different USB cable — many cables are charge-only; you need a data cable
→ The QT Py RP2040 uses USB-C; confirm your cable supports data

**`No I2C device found` / import error on MPR121**
→ Check the STEMMA QT cable is fully seated on both ends (they click in slightly)
→ Confirm `adafruit_mpr121.mpy` is in the `lib/` folder on `CIRCUITPY`

**`osc_bridge.py` can't find the board**
→ Make sure `boot.py` was saved and the board was replugged after
→ On Mac, the port will look like `/dev/cu.usbmodem...`; on Windows, `COM3` or similar

**OSC not arriving in Max/TD**
→ Confirm the bridge is running (you should see touch/release printed in the terminal)
→ Confirm both scripts are using the same port number (default: `8000`)

**Touch data triggering randomly / too sensitive**
→ Tune thresholds in `code.py` after MPR121 init: `mpr.set_thresholds(12, 6)` — lower numbers = more sensitive; raise the first value to reduce false triggers
→ Keep electrode wires short and away from power cables where possible

**DS18B20 reads `None` or `AttributeError`**
→ The 4.7kΩ pull-up resistor is required — without it the bus won't work
→ Double-check wire colors match your specific probe (Gikfun probes vary)

---

## The Signal Chain, Named

Once everything is running, here is what you have:

```
conductive material
        ↓
  MPR121 electrode  (capacitance → threshold event)
        ↓
  I2C → QT Py RP2040  (Python: detect change, format message)
        ↓
  USB serial → laptop
        ↓
  osc_bridge.py  (parse serial, build OSC packet, send UDP)
        ↓
  Max/MSP or TouchDesigner  (receive, route, map, generate)
        ↓
  audio / visual / other output
```

Each arrow is a transformation. Something is amplified; something is reduced. The MPR121 reduces a complex capacitance field to 12 binary on/off states. The serial protocol reduces those to timestamped text strings. The OSC packet reduces those to typed numbers on a named address. The Max patch maps those numbers to something audible or visible. At no point is the original touch fully preserved — and that's not a failure. That's the chain.

---

## Connected

[[Hardware Clarifications — Thinking Toward Sensors|← Hardware Clarifications — Thinking Toward Sensors]]
[[../Threads/Physical-Digital Entanglement|Physical-Digital Entanglement thread]]
[[../Threads/Enabling Constraints|Enabling Constraints thread]]
