---
title: "AMG8833 - From Sensor to Image in TouchDesigner"
tags: [DIGM553, hardware, sensors, touchdesigner, thermal, AMG8833]
---

# AMG8833 - From Sensor to Image in TouchDesigner
## Turning your 64 temperature readings into a heat-map you can see

---

> [!note] Where this guide picks up
> You've already got the AMG8833 wired to your QT Py RP2040, and the CircuitPython sketch is sending one frame per row over USB serial - eight lines per frame, ten frames per second, in this format:
>
> `amg,<row_index>,<v0>,<v1>,<v2>,<v3>,<v4>,<v5>,<v6>,<v7>`
>
> This guide takes you from there to a real-time, color-mapped thermal image inside TouchDesigner. Nothing here changes the sketch on the board - it's all on the TD side.

---

## What you're building

```
[ AMG8833 + QT Py ]                  ← already working
        │
        │  USB serial, 115200 baud
        ▼
[ Serial DAT ]                       ← TD reads from your COM port
        │
        ▼
[ DAT Execute  (parses each line) ]
        │
        ▼
[ Table DAT  (8 × 8 of floats) ]     ← one frame, kept fresh
        │
        ▼
[ DAT to CHOP ]  →  [ CHOP to TOP ]  ← table → channels → image
        │
        ▼
[ Level TOP ]                        ← remap °C to 0..1
        │
        ▼
[ Resolution TOP ]                   ← scale up, soft filter
        │
        ▼
[ Lookup TOP ]  ←  [ Ramp TOP ]      ← apply thermal colormap
```

*You'll build it once, save the project, and from then on you just plug the sensor in and open the file.*

---

## Part 0 - Find your COM port

Before anything else, figure out which port Windows assigned to your QT Py.

1. Plug the QT Py in.
2. Open **Device Manager**.
3. Expand **Ports (COM & LPT)**.
4. You should see something like *USB Serial Device (COM5)* or *Adafruit QT Py (COM7)*. Note the COM number - that's what you'll point TD at.

> [!tip] If you don't see your board in Device Manager
> - Try a different USB cable.
> - If no port shows up, briefly tap the reset button on the QT Py.

---

## Part 1 - Update the CircuitPython sketch

The default Adafruit example we added before prints each row as a Python *list* like `['22.1', '22.4', '22.5', ...]` with quotes and brackets, plus blank lines between rows. That's nice for reading in the REPL but messy for TouchDesigner to parse line by line. We're going to change it to print one tidy comma-separated row per line instead.

A copy of the modified `code.py` file was provided. Copy this onto your board and replace the code.py there.

1. Each row prints as `amg,<row_index>,<v0>,<v1>,...,<v7>` (no quotes, no brackets, no blank lines), and
2. `time.sleep(0.1)` instead of `time.sleep(1)` so you get ~10 frames per second instead of 1, faster and smoother reads.

Open the  Serial Monitor REPL (connect to your device COM port) > Start Monitoring, just long enough to confirm you're seeing lines like this:

```
amg,0,22.1,22.2,22.4,22.0,21.9,22.0,22.1,22.0
amg,1,22.0,22.1,22.5,22.3,22.0,21.9,22.0,22.1
amg,2,...
```

When you see that, **close the REPL (Stop Monitoring)** because TD can't open the port if VS Code has it running.

---

## Part 2 - Build the TouchDesigner network

### Node 1 - `serial1` (Serial DAT)

Open TouchDesigner:

Add a **Serial DAT** to your network. Set its parameters:

| Parameter | Value |
|---|---|
| Active | **On** |
| Port | your QT Py's COM port (e.g. `COM5`) |
| Baud Rate | `115200` |
| Data Bits | `8` |
| Parity | `None` |
| Stop Bits | `1` |
| Row/Callback Format | **One Per Line** |

Lines should start filling in within a second of turning *Active* on. You'll see things like:

```
amg,0,22.1,22.2,22.4,22.0,...
amg,1,22.0,22.1,22.5,22.3,...
amg,2,...
```

If you see that, the connection is good. Move on.

> [!warning] If the Serial DAT stays empty
> 1. Wrong COM port - re-check Device Manager.
> 2. Another program (like VS Code IDE Serial Monitor) is holding the port. Close it and toggle *Active* off and back on.
> 3. Baud rate mismatch with your sketch. The code.py you've been using is 115200 - confirm the Serial DAT matches.

---

### Node 2 - `text_callbacks` (Text DAT)

Add a **Text DAT** and rename it `text_callbacks`. Paste this inside:

```python
# Callbacks for serial1 - one call per received line.
#
# Each line looks like: "amg,3,22.1,22.4,23.5,22.9,..."
# That's: literal "amg", a row index (0..7), and 8 temperature floats.

def onReceive(dat, rowIndex, message, bytes, peer):
    parts = message.strip().split(",")

    # Bail out if the line is malformed or doesn't start with "amg".
    if len(parts) != 10 or parts[0] != "amg":
        return

    try:
        row_idx = int(parts[1])
        temps = [float(x) for x in parts[2:]]
    except ValueError:
        return  # a value didn't parse as a number - skip the line

    # Look up the destination table. If it doesn't exist yet, bail out
    # quietly instead of throwing on every line.
    table = op('table_amg')
    if table is None:
        return

    # Write the 8 temperatures into the matching row of the table.
    for col, temp in enumerate(temps):
        table[row_idx, col] = round(temp, 2)
    return
```

Now go back to `serial1` and under the **Received Data** tab set its **Callbacks DAT** parameter to `text_callbacks`. From now on, every received line fires `onReceive` and ends up in the table.

---

### Node 3 - `table_amg` (Table DAT)

Add a **Table DAT** and **rename it to exactly `table_amg`** (lowercase, with the underscore). TD drops new Table DATs in as `table1` by default - you have to rename it, otherwise the callback can't find it.

You also need it pre-shaped to **8 rows × 8 columns** before the callbacks start writing. Two easy ways:

- **Simple way:** in the Table DAT's viewer, right-click → *Set Table > By Size* → 8 rows, 8 columns.

After everything is wired up, you should see the table cells flicker as new values arrive. Most cells hover around room temperature (~22°C); a few will climb into the high 20s or low 30s when something warm is in front of the sensor - your hand, a coffee cup, etc.

> [!note] The table is your first checkpoint
> If the table is updating with believable temperatures, you have a working sensor pipeline. **Everything from here on is just visualization.** If something downstream looks broken later, come back to this table.

---

### Node 4 - `datto1` (DAT to CHOP)

Add a **DAT to CHOP**. Wire `table_amg` into it. Set:

| Parameter | Value |
|---|---|
| DAT | `table_amg` |
| Output | **Channels per Row** |
| First Row is Names | **Off** |
| First Column is Names | **Off** |

You should now have a CHOP with **8 channels × 8 samples**. Each channel = one row of the thermal grid; each sample within a channel = one column.

Open the CHOP viewer - you'll see eight wiggling lines drifting between roughly 20 and 32. That wiggle *is* the heat moving across the sensor.

---

### Node 5 - `chopto1` (CHOP to TOP)

Add a **CHOP to TOP**. Wire `datto1` into it. Set:

| Parameter | Value |
|---|---|
| CHOP | `datto1` |
| Data Format | **R** (single channel - temperatures are scalar, one number per pixel) |

You now have an 8×8 image where pixel brightness corresponds to temperature. **That's your sensor as a picture.** It will look tiny and pixelly. That's correct: the sensor really is only 64 pixels.

---

### Node 6 - make it readable

Right after `chopto1`, add two more TOPs:

1. **`level1` (Level TOP)** - temperature values are in Celsius (~20 to ~32), but TOPs expect 0 to 1. Use Level's **Pre-Range** Low/High to remap:
   - Pre-Range Low: `20`
   - Pre-Range High: `32`
   - Post-Range Low: `0`
   - Post-Range High: `1`

   Now cooler cells are black, hotter cells are white.

2. **`resolution1` (Resolution TOP)** - sets the output to whatever pixel size you want. 256×256 with **Filter = Gaussian** gives you the soft-blob thermal-cam look. Wire `level1` into it.

You should see a softly glowing blob roaming the frame whenever something warm is in the sensor's field of view.

> [!tip] Tune the pre-range to your room
> The 20–32 numbers are a starting guess. Watch the table while the sensor sees both ambient (room temp) and something warm (your hand). Set Pre-Range Low to roughly the ambient value and Pre-Range High to roughly the warmest reading you see. That gives you the best contrast in the image.

---

### Node 7 - colormap (the part that makes it look like a real thermal cam)

Real thermal cameras don't show grayscale; they use color ramps (inferno, plasma, the classic blue→red rainbow). Two more nodes get you there.

1. Add a **Ramp TOP** named `ramp_thermal`. Set:
   - Type: **Horizontal**
   - Resolution: 256 × 1
   - Click *Custom* and add color stops along the bar:
     - 0.00 → deep blue (cold)
     - 0.20 → cyan
     - 0.40 → green
     - 0.60 → yellow
     - 0.80 → orange
     - 1.00 → red / white (hottest)

2. Add a **Lookup TOP**. Wire your `resolution1` (the grayscale image) into the **first** input, and `ramp_thermal` into the **second** input.

The Lookup TOP uses the brightness of the first input to *sample* colors from the second input. Result: a thermal-camera-looking image whose colors are physically meaningful - blue is cold, red is hot, and the gradient between them tracks temperature.

---

## Troubleshooting checklist

- **Serial DAT is empty.** Wrong port, port held by another program, or sketch isn't running on the board. Check Device Manager and your CircuitPython REPL.
- **`'NoneType' object does not support item assignment`.** Your Table DAT isn't named `table_amg`. Rename it.
- **Table fills, but the image is solid black.** Level TOP's pre-range is wrong - your hot values are below the high threshold and getting clamped. Lower the high.
- **Image is solid white.** Opposite - pre-range is too narrow or shifted too low. Raise the high.
- **Cells stuck at zero in places.** A line failed to parse. Open `text_callbacks` and add `print(parts)` near the top of `onReceive` to see what's actually arriving.
- **Image looks frozen.** The QT Py probably got reset or unplugged. Toggle the Serial DAT's *Active* off and on, or unplug/replug the board.

---

## What to try next

- **Tune the colormap.** The blue→red ramp is just one choice. Try inferno (black → purple → red → orange → yellow), or grayscale, or something completely unrelated to "heat" - like a custom palette that fits the rest of your project's look.
- **Bypass the colormap.** The grayscale image is just data. Feed it into a Displace TOP, a Noise TOP's offset, a particle system's force field, or an audio filter cutoff via TOP-to-CHOP. Once it's a TOP, anything in TD can use it.
- **Smooth the image.** The 8×8 grid is *very* coarse. Try inserting a Blur TOP between `resolution1` and `level1` to soften it further. Or feed it through a Composite TOP with itself at lower opacity for trails.
- **Record a session.** Use a Movie File Out TOP to capture a few minutes of your thermal image. You'll have a clip you can scrub through and use later, even when the sensor isn't around.

> [!question]- One thing worth thinking about as an artist
> The AMG8833 sees temperature, and we're treating it like a camera. But it's not a camera - it's an instrument that sees a slice of the infrared spectrum your eyes can't see. The "image" you just made is a translation, not a picture. What gets gained, and what gets lost, in turning a thermal field into something that *looks like* a picture? That tension is the work, not a side effect of it.
