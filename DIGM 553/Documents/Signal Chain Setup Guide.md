---
title: "Signal Chain Setup Guide"
tags: [DIGM553, hardware, circuitpython, serial, setup]
---
# Signal Chain Setup Guide

> Getting your microcontroller talking to your computer. From unboxing to touch data flowing into Max, TouchDesigner.

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

> [!note] The RP2040 does **not** have built-in WiFi. This board communicates over **USB serial** — it sends plain text data directly to your laptop, where TouchDesigner, Max/MSP, or PlugData reads it. No intermediate script needed.

---

### Primary Sensor — Adafruit MPR121 12-Key Capacitive Touch

The **MPR121** gives you 12 capacitive touch inputs (labeled `0` through `11`). Each input can be connected to any conductive material — copper tape, conductive thread, metal objects, wire — and the sensor detects when that material is touched.

Key facts:
- **I2C address:** `0x5A` (default). Can be changed to `0x5B`, `0x5C`, or `0x5D` by bridging the `ADDR` jumper pad on the breakout — useful if you need to stack multiple MPR121s on the same bus
- **Connects via STEMMA QT** → one cable, no soldering required for basic use
- **Electrode pads:** The `0`–`11` pads on the breakout are where you attach conductive materials. Alligator clips, solid-core wire, or copper tape all work.
- **CircuitPython library:** `adafruit_mpr121`

---

## Part 1 — Flash CircuitPython onto the QT Py RP2040

CircuitPython is the firmware that lets you write and run Python scripts on the board. You only need to do this once.

### Step 1 — Download the firmware

Go to: https://circuitpython.org/board/adafruit_qtpy_rp2040/

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

CircuitPython uses a `lib/` folder on the `CIRCUITPY` drive. You copy library files there manually.

### Get the library bundle

Download the **Adafruit CircuitPython Bundle** from:
https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases

Download the bundle matching your CircuitPython version (e.g., `adafruit-circuitpython-bundle-10.x-mpy-YYYYMMDD.zip`). Unzip it — you'll get a large folder of `.mpy` files.

### Libraries to copy into `lib/`

**For MPR121 (required):**
```
adafruit_mpr121.mpy
adafruit_connection_manager.mpy
```

> [!note] The board sends plain text over USB serial. Your receiving software (TouchDesigner, Max/MSP, or PlugData) reads that text directly — no additional libraries or scripts needed on the laptop side.

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

The board runs two files: `boot.py` (enables the USB serial data channel) and `code.py` (reads the MPR121 and sends touch data as plain text). Your software on the laptop reads that text directly — no bridge script needed.

---

### `code.py` (on the board)

Save this as `code.py` on the `CIRCUITPY` drive:

```python
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
mpr = adafruit_mpr121.MPR121(i2c)   # Default I2C address 0x5A

serial = usb_cdc.data              # USB serial data channel

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
        raw = baseline - filtered  # 0 at rest, increases with touch

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
    time.sleep(0.01)   # 100Hz polling
```

>[!note] To fix the error messages when pasting the code from here in VS Code:
>1. Open Find/Replace (`Ctrl+H`).
>2. Enable regex (`.*`).
>3. In **Find**, type `\u00A0`.
>4. **Replace** all with a normal space.
>5. Save.

You also need to enable the USB serial data channel. Create a file called `boot.py` on `CIRCUITPY` with this content:

```python
# boot.py — enables USB serial data channel on RP2040
import usb_cdc
usb_cdc.enable(console=True, data=True)
```

After saving `boot.py`, **unplug and replug the board** for it to take effect.

---

## Part 5 — Receiving Serial Data

The board appears as **two serial ports** on your computer once `boot.py` is in place — a console port (the REPL) and a data port. You want the **data port** (usually the larger number).

**Finding the data port:**
- **Mac:** run `ls /dev/tty.usbmodem*` in Terminal — you'll see two entries; the data port is typically the one with the higher number
- **Windows:** open Device Manager → Ports (COM & LPT) — two COM ports will appear; try the one you haven't used before

---

### In TouchDesigner

#### Step 1 — Serial DAT

1. Press **Tab** and add a **Serial DAT**
2. In its parameters, set **Port** to your data port (e.g. `/dev/cu.usbmodem...` on Mac, `COM4` on Windows)
3. Set **Row/Callback Format** to `One Per Line`
4. Set **Baud Rate** to `115200` (USB CDC ignores this but TD requires a value)
5. Touch an electrode — you should see rows appearing: `TOUCH,2,18`, `RAW,2,24`, `RELEASE,2,3`

#### Step 2 — DAT Execute to write the table

1. Press **Tab** and add a **DAT Execute**
2. Wire your **Serial DAT** into it as the input
3. In the DAT Execute parameters, turn on **Row Change** and turn off everything else
4. Paste this into the script:

```python
def onRowChange(dat, rows):
    for row in rows:
        line = dat[row, 0].val.strip()
        if not line:
            continue
        
        cells = line.split(',')
        if len(cells) < 3:
            continue
        
        event = cells[0]
        idx = int(cells[1])
        raw = int(cells[2])
        
        table = op('/project1/electrode_state')
        if event == 'TOUCH':
            table[idx + 1, 1] = 1
            table[idx + 1, 2] = raw
        elif event == 'RELEASE':
            table[idx + 1, 1] = 0
            table[idx + 1, 2] = raw
        elif event == 'RAW':
            table[idx + 1, 2] = raw
```

#### Step 3 — Create the state table

Now create the `electrode_state` Table DAT that the script writes into. Open the **Textport** with **Alt+T** and run each of these three steps separately:

**Step 3a** — create the DAT:
```python
t = op('/project1').create(tableDAT, 'electrode_state')
```

**Step 3b** — clear it and add the 12 electrode rows:
```python
t = op('/project1/electrode_state')
t.clear()
for i in range(12):
    t.appendRow([i, 0, 0])
```

**Step 3c** — insert the header row at position 0:
```python
t.insertRow(['electrode', 'state', 'raw'], 0)
```

> [!note] These must be run as three separate Textport commands — the Textport can't follow a `for` loop with an additional statement in the same block.

You should end up with 13 rows — a header row plus one row per electrode. The `insertRow(..., 0)` adds the headers after the data rows so electrode 0's data never overwrites the column names.

#### Step 4 — Into CHOP land

Add a **DAT to CHOP** after `electrode_state`. Each electrode becomes a named channel you can feed directly into audio, visuals, or any other part of your network:

```
Serial DAT → DAT Execute → (writes to) electrode_state Table DAT
                                               ↓
                                        DAT to CHOP
                                               ↓
                                        Select CHOP → your network
```

---

### In Max/MSP

Use the `[serial]` object:

```
[serial a 115200]        ← 'a' picks the first available port; change to b, c etc. for the data port
        |
  [fromsymbol]
        |
   [zl join]
        |
  [route TOUCH RAW RELEASE]
```

The messages arriving are plain text lines like `TOUCH,2,18`. Use `[regexp]` or `[sprintf]` to split on the comma and extract electrode number and raw value.

> [!tip] In Max, open the **Serial** menu (Extras → Serial) to see which port letter corresponds to your data port.

---

### In PlugData

> [!warning] PlugData does not currently support serial communication reliably for this use case. The `[comport]` external outputs raw bytes as numbers rather than parsed text strings, meaning the `TOUCH`, `RAW`, and `RELEASE` message content never arrives intact — `[route]` has nothing to work with.

**Use Max/MSP or TouchDesigner instead.** Both handle USB serial text correctly out of the box with no additional setup.

If you are committed to a Pd-based environment, one workaround is a small Python script on your laptop that reads serial and forwards data as OSC, received in PlugData via `[oscreceive]`. However this reintroduces bridge script complexity and is better suited to an ESP32/Feather setup with built-in WiFi — ask your instructor if that path makes sense for your project.

---

## Troubleshooting

**Board not showing up as `CIRCUITPY` drive**
→ Try a different USB cable — many cables are charge-only; you need a data cable
→ The QT Py RP2040 uses USB-C; confirm your cable supports data

**`No I2C device found` / import error on MPR121**
→ Check the STEMMA QT cable is fully seated on both ends (they click in slightly)
→ Confirm `adafruit_mpr121.mpy` is in the `lib/` folder on `CIRCUITPY`

**Serial data not arriving in Max/TD/PlugData**
→ Make sure `boot.py` was saved and the board was replugged after — the data port only appears after `boot.py` runs
→ Confirm you are connected to the **data port**, not the console/REPL port (there will be two ports; try the other one)
→ On Mac the port looks like `/dev/cu.usbmodem...`; on Windows `COM3` or similar

**Touch data triggering randomly / too sensitive**
→ Tune thresholds in `code.py` after MPR121 init: `mpr.set_thresholds(12, 6)` — lower numbers = more sensitive; raise the first value to reduce false triggers
→ Keep electrode wires short and away from power cables where possible

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
  USB serial → laptop  (plain text: TOUCH,2,18 / RAW,2,24 / RELEASE,2,3)
        ↓
  Max/MSP or TouchDesigner  (receive, parse, route, map)
        ↓
  audio / visual / other output
```

Each arrow is a transformation. Something is amplified; something is reduced. The MPR121 reduces a complex capacitance field to 12 states. The serial protocol reduces those to timestamped text strings. Max or TouchDesigner maps those strings to something audible or visible. At no point is the original touch fully preserved.

