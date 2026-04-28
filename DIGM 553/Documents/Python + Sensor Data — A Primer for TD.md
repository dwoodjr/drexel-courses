# Python + Sensor Data — A Primer for TouchDesigner

---

## Part 1 — Python Fundamentals (the pieces you'll actually use)

### Variables: giving a value a name

A variable is just a label you stick on a piece of data so you can use it later.

```python
temperature = 24.5       # a decimal number (float)
channel = 3              # a whole number (integer)
sensor_name = "AMG8833"  # text (string)
is_ready = True          # True or False (boolean)
```

No special keyword needed, just write `name = value`. Python figures out the type automatically.

---

### Lists: an ordered collection of values

A **list** holds multiple values in a row, indexed from `0`.

```python
rgb = [255, 128, 0]   # three values: red, green, blue

print(rgb[0])  # → 255  (first item)
print(rgb[1])  # → 128  (second item)
print(rgb[2])  # → 0    (third item)
```

> [!note] **Why lists matter for sensors:** Almost every sensor gives you more than one number at a time. A color sensor gives you R, G, B, and maybe infrared. An IMU gives you X, Y, Z acceleration. A list is the natural container for all of those channels.

---

### Loops: doing something for every item

```python
channels = [12, 34, 56, 78]

for value in channels:
    print(value)
# prints: 12, then 34, then 56, then 78
```

You can also loop over a range of numbers:

```python
for i in range(4):
    print(i)
# prints: 0, 1, 2, 3
```

Combining both (useful when you need the index *and* the value):

```python
channels = [12, 34, 56, 78]

for i, value in enumerate(channels):
    print(f"channel {i} = {value}")
# channel 0 = 12
# channel 1 = 34
# ...
```

---

### f-strings: building text with values inside

The `f"..."` syntax lets you drop variables directly into a string using `{}`.

```python
x = 128
y = 64
print(f"x={x},y={y}")   # → x=128,y=64
```

This is the main way you'll format data to send over serial or OSC (one line of text per reading).

---

### Functions: reusable named blocks of code

```python
def read_sensor():
    # ... code to read the sensor ...
    return [r, g, b]

data = read_sensor()
print(data)
```

`def` defines the function. `return` sends a value back to whoever called it.

---

### The main loop pattern

CircuitPython programs (on devices like the Adafruit QT Py) run continuously. The standard structure is:

```python
import time

# 1. Setup — runs once
i2c = busio.I2C(board.SCL1, board.SDA1)
sensor = SomeSensor(i2c)

# 2. Loop — runs forever
while True:
    data = sensor.read()
    # ... do something with data ...
    time.sleep(0.05)   # wait 50ms → 20Hz polling rate
```

---

## Part 2 — Sensor Data as Tables

**Sensor data is naturally tabular.**

| Sensor | What it gives you | Shape |
|---|---|---|
| TCS3430 | X, Y, Z, IR light channels | 1 row × 4 columns |
| APDS9999 | R, G, B, Lux, proximity | 1 row × 5 columns |
| AMG8833 | 8×8 thermal pixel grid | 8 rows × 8 columns |

A single reading = one row. Multiple readings over time = a growing table. TouchDesigner's DAT system is built around exactly this idea.

---

### Representing a single reading as a Python list

```python
# TCS3430 — one reading, four channels
reading = [x_channel, y_channel, z_channel, ir_channel]

# APDS9999 — one reading, five channels
reading = [red, green, blue, lux, proximity]
```

---

### Representing a matrix as a list of lists

The AMG8833 thermal camera gives you 64 temperature values arranged in an 8×8 grid. In Python, that's a **list of lists** (each inner list is one row).

```python
# An 8×8 grid (simplified with placeholder values)
grid = [
    [21.0, 21.2, 21.5, 22.0, 22.3, 22.1, 21.8, 21.4],  # row 0
    [21.1, 21.4, 21.9, 22.4, 22.8, 22.5, 22.0, 21.6],  # row 1
    # ... 6 more rows
]

# Access a single pixel: row 2, column 5
pixel = grid[2][5]

# Loop over every pixel:
for row in grid:
    for temp in row:
        print(temp)
```

---

### How your sensor's behavior determines your table shape

Before you build a table in TD, ask yourself one question: **does my sensor send data constantly, or only when something happens?**

This is the most important thing to get right. The answer determines everything about how your table should be structured.

**Streaming sensors** send a new reading every few milliseconds, whether or not anything has changed. Color sensors (TCS3430, APDS9999), thermal cameras (AMG8833), and most environmental sensors work this way. The current reading simply replaces the last one — there's nothing to accumulate.

→ Your table should have **one data row**. Every incoming message overwrites it with fresh values.

```
r     g     b     clear
1024  892   1156  340      ← always the current reading, overwritten each frame
```

**Event-driven sensors** only send data when a discrete thing happens — a touch starts, a touch ends, a threshold is crossed. The MPR121 capacitive touch sensor works this way. Between events, silence. The table has to *remember* the last known state of each input.

→ Your table should have **one row per input**, holding state between events.

```
electrode  state  raw
0          0      0
1          1      18      ← electrode 1 is currently being touched
2          0      0
...
```

**The rule:** if your sensor streams, your table is wide (many columns, one row). If your sensor sends events, your table is tall (many rows, one per input). Getting this backwards means your script will either overwrite data it needs to keep, or accumulate rows that should have been replaced.

When you look at someone else's TD setup and wonder "why is the table shaped like that?" — trace it back to what the sensor actually sends.

---

## Part 3 — Sending Data to TouchDesigner

Two methods get data from your device into TD. Use whichever fits your setup.

---

### Method A — USB Serial (simplest, works out of the box)

Your device sends plain text over USB. TD reads it with a **Serial DAT**.

**The idea:** format each reading as a comma-separated line, end it with `\n`.

```
# Single-channel format (one value per line)
"temperature,23.4\n"

# Multi-channel format (label + all values on one line)
"tcs3430,1024,892,1156,340\n"

# Matrix format (one row per line, repeat 8 times for AMG8833)
"amg8833,0,21.0,21.2,21.5,22.0,22.3,22.1,21.8,21.4\n"
"amg8833,1,21.1,21.4,21.9,22.4,22.8,22.5,22.0,21.6\n"
...
```

The third column in the AMG row is the **row index** (0–7), so TD knows which row it's receiving.

---

#### CircuitPython — Serial examples

**TCS3430 (XYZ color + IR):**

```python
import board
import busio
import usb_cdc
import time
import adafruit_tcs34725  # closest available library; TCS3430 uses similar interface

i2c = busio.I2C(board.SCL1, board.SDA1)
sensor = adafruit_tcs34725.TCS34725(i2c)
serial = usb_cdc.data

while True:
    r, g, b, c = sensor.color_raw   # raw R, G, B, Clear channels
    msg = f"tcs,{r},{g},{b},{c}\n"
    serial.write(msg.encode())
    time.sleep(0.05)
```

**APDS9999 (color + Lux + proximity):**

```python
import board
import busio
import usb_cdc
import time
import adafruit_apds9960.apds9960 as apds_lib  # APDS9999 uses the same CircuitPython driver

i2c = busio.I2C(board.SCL1, board.SDA1)
sensor = apds_lib.APDS9960(i2c)
sensor.enable_color = True
sensor.enable_proximity = True
serial = usb_cdc.data

while True:
    r, g, b, c = sensor.color_data     # raw R, G, B, Clear
    lux = (0.299 * r + 0.587 * g + 0.114 * b)  # approximate Lux from RGB
    prox = sensor.proximity             # 0 (far) – 255 (close)
    msg = f"apds,{r},{g},{b},{lux:.1f},{prox}\n"
    serial.write(msg.encode())
    time.sleep(0.05)
```

**AMG8833 (8×8 thermal array):**

```python
import board
import busio
import usb_cdc
import time
import adafruit_amg88xx

i2c = busio.I2C(board.SCL1, board.SDA1)
amg = adafruit_amg88xx.AMG88XX(i2c)
serial = usb_cdc.data

while True:
    pixels = amg.pixels   # list of 8 lists, each with 8 floats (°C)
    for row_idx, row in enumerate(pixels):
        values = ",".join(f"{v:.1f}" for v in row)
        msg = f"amg,{row_idx},{values}\n"
        serial.write(msg.encode())
    time.sleep(0.1)   # full 8×8 frame at ~10Hz
```

---

#### TouchDesigner — Serial DAT setup

1. Add a **Serial DAT** (`Tab → DAT → Serial`)
2. Set **Port** to the COM port your device appears on (check Device Manager on Windows, `/dev/tty.usbmodem*` on Mac)
3. Set **Baud Rate** to `115200`
4. Set **Row/Callback Format** to `One Per Line`
5. Add a **DAT Execute DAT** and use `onReceive` to parse incoming lines:

```python
# DAT Execute DAT — onReceive callback
def onReceive(dat, rowIndex, message, bytes):
    parts = message.strip().split(",")
    
    if parts[0] == "tcs":
        # parts = ["tcs", r, g, b, c]
        r, g, b, c = [int(x) for x in parts[1:]]
        op('tcs_table')[1, 'r'] = r
        op('tcs_table')[1, 'g'] = g
        op('tcs_table')[1, 'b'] = b
        op('tcs_table')[1, 'clear'] = c

    elif parts[0] == "apds":
        # parts = ["apds", r, g, b, lux, prox]
        r, g, b = int(parts[1]), int(parts[2]), int(parts[3])
        lux, prox = float(parts[4]), int(parts[5])
        op('apds_table')[1, 'r'] = r
        op('apds_table')[1, 'g'] = g
        op('apds_table')[1, 'b'] = b
        op('apds_table')[1, 'lux'] = lux
        op('apds_table')[1, 'proximity'] = prox

    elif parts[0] == "amg":
        # parts = ["amg", row_index, v0, v1, ..., v7]
        row_idx = int(parts[1])
        temps = [float(x) for x in parts[2:]]
        for col, temp in enumerate(temps):
            op('amg_table')[row_idx + 1, col] = temp   # +1 skips header row
```

**Setting up the Table DATs:**

For single-channel sensors (TCS3430, APDS9999), create a **Table DAT** with a header row and one data row:

```
r    g    b    clear    proximity
0    0    0    0        0
```

For the APDS9999, add a `lux` column too:

```
r    g    b    lux    proximity
0    0    0    0.0    0
```

For AMG8833, create a **Table DAT** with 8 rows (plus header) and 8 columns:

```
col0   col1   col2   col3   col4   col5   col6   col7
0      0      0      0      0      0      0      0
0      0      0      0      0      0      0      0
... (8 data rows total)
```

---

### Method B — OSC over Network

OSC (Open Sound Control) sends structured data over UDP. Your device (or a Python bridge script on your computer) sends OSC messages; TD receives them with a **OSC In DAT**.

> **When to use this:** If you want to run Python on your laptop (not a microcontroller), or if you need to send data to TD from another room or machine.

---

#### Python (desktop) — OSC bridge using `python-osc`

Install the library first (Terminal / Command Prompt):
```
pip install python-osc
```

**Sending TCS3430 / APDS9999 style data:**

```python
from pythonosc import udp_client
import time
import random  # replace with real sensor reads

client = udp_client.SimpleUDPClient("127.0.0.1", 9000)  # TD listens on this port

while True:
    # Replace these with actual sensor reads
    r, g, b, c = 1024, 892, 1156, 340

    # Send as a single OSC message with multiple arguments
    client.send_message("/sensor/tcs", [r, g, b, c])

    time.sleep(0.05)
```

**Sending AMG8833 thermal grid:**

```python
from pythonosc import udp_client
import time

client = udp_client.SimpleUDPClient("127.0.0.1", 9000)

while True:
    # Replace with real amg.pixels
    pixels = [[21.0 + i * 0.1 + j * 0.05 for j in range(8)] for i in range(8)]

    for row_idx, row in enumerate(pixels):
        # Send each row as its own message: /sensor/amg/0, /sensor/amg/1, etc.
        client.send_message(f"/sensor/amg/{row_idx}", row)

    time.sleep(0.1)
```

---

#### TouchDesigner — OSC In DAT setup

1. Add an **OSC In DAT** (`Tab → DAT → OSC In`)
2. Set **Network Port** to `9000` (must match your Python script)
3. The DAT will log every incoming message — one row per message, columns for address and arguments
4. Add a **DAT Execute DAT** on the OSC In DAT to act on messages as they arrive:

```python
# DAT Execute DAT — onReceive for OSC In DAT
def onReceive(dat, rowIndex, message, bytes):
    # 'dat' is the OSC In DAT — read the latest row
    pass

# Better: use the 'tableChange' callback on a downstream Table DAT
# OR use the OSC In DAT directly — each row is already parsed:
#   col 0 = address (e.g. "/sensor/tcs")
#   col 1, 2, 3... = argument values
```

**Simpler TD approach using OSC In DAT + Select DAT:**

The OSC In DAT accumulates rows. Use a **Select DAT** to filter by address:

- Expression: `me.inputCell.val == "/sensor/tcs"` on the address column
- Then a **Convert DAT** to get just the numeric columns out

For the AMG8833 grid, one clean approach is to use a **Script DAT** that rebuilds the 8×8 table each time any `/sensor/amg/*` message arrives.

---

## Part 4 — Reading the Table in TD

Once your data is in a Table DAT, everything in TD can reference it.

```python
# In any TD Python field or Script CHOP:

# Read a single cell by row index and column name
r_val = op('tcs_table')[1, 'r']

# Read a whole row as a list
row = [op('tcs_table')[1, col] for col in range(8)]

# Convert a Table DAT column to a CHOP channel:
# Use a DAT to CHOP operator — set Transpose if needed
```

From a CHOP you can drive any parameter in TD: geometry color, audio amplitude, particle count, shader uniforms, anything.

---

## Troubleshooting

**Serial DAT shows nothing** — Check that the COM port is correct and no other app (VS Code, Arduino IDE monitor) has the port open. Only one app can hold a serial port at a time.

**OSC messages arrive but values look wrong** — Print the raw message in a DAT Execute to see what's actually coming in: `print(dat.row(rowIndex))`.

**AMG8833 grid looks scrambled in TD** — Make sure you're writing rows in order (0–7) and that the Table DAT has the right number of rows pre-created before data arrives.

**CircuitPython crashes or hangs** — Add a `try/except` around your sensor read so a bad reading doesn't kill the loop:

```python
while True:
    try:
        pixels = amg.pixels
        # ... send data ...
    except Exception as e:
        print(f"Error: {e}")
    time.sleep(0.05)
```
