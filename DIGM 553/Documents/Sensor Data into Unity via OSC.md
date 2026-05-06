---
title: "Sensor Data into Unity via OSC"
tags: [DIGM553, hardware, unity, osc, circuitpython, esp32, rp2040, extOSC, apds9999, mpr121]
---
# Sensor Data into Unity via OSC

> Two paths, one destination: routing live microcontroller sensor data into Unity using the OSC protocol and the extOSC plugin.

This guide covers both hardware configurations in the class:

- **Path A — QT Py RP2040 + MPR121**: Touch data → USB serial → Python bridge → OSC → Unity
- **Path B — Feather ESP32 + APDS-9999**: Color/proximity/lux data → WiFi → OSC → Unity 

**If you haven't set up your RP2040 yet**, start with [[Signal Chain Setup Guide]] first — it covers flashing CircuitPython, installing the MPR121 library, and getting touch data flowing over serial. This guide picks up from there.

---

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/1189762208?title=0&amp;byline=0&amp;portrait=0&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media; web-share" referrerpolicy="strict-origin-when-cross-origin" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="digm553-UnityOSC"></iframe></div>

---
## What is OSC?

**OSC (Open Sound Control)** is a lightweight network protocol for sending real-time data between applications and devices. It was designed for music and media performance — so it's built for low latency and frequent updates. An OSC message has two parts:

- An **address** — a path like `/sensor/proximity` or `/touch/3` that identifies what data you're sending
- One or more **values** — integers, floats, or strings

OSC travels over UDP, which means:
- **Fast** — no connection handshake overhead
- **Lossy** — dropped packets are not resent (this is usually fine for continuous sensor data)
- **Network-based** — both sender and receiver need to agree on an IP address and port number

---

## Part 1 — Unity Setup with extOSC

This section is the same regardless of which hardware path you're on. Do this first.

![[Screenshot 2026-05-06 160822.png]]

### Step 1 — Create or Open Your Unity Project

Open Unity Hub and create a new project (3D Core is fine). If you already have a project, open it.

> [!note] extOSC works with Unity 2020 and later. If you're on an older version, update Unity Hub first.

### Step 2 — Install extOSC

1. Add to Unity Assets from Asset Store
2. In Unity, go to **Window → Package Manager**
2. Click the **+** button in the top-left corner of the Package Manager window
3. Choose **My Assets**
4. Search extOSC
5. Click **Add** or **install** and wait for Unity to download and compile the package

OR
1. Go to the GitHub: https://github.com/Iam1337/extOSC
2. Download the latest source code
3. Extract all...
4. Copy the extOSC folder into your projects `Assets` directory

When it finishes, you'll see **extOSC** listed under your project's packages. No restart needed.

![[Screenshot 2026-05-06 160856.png]]

### Step 3 — Create the OSC Receiver GameObject

1. In the **Hierarchy** panel (top-left of the Unity window), right-click in an empty area
2. Choose **Create Empty**
3. Rename the new object to `OSC Manager` (click it once to select, then press F2 or double-click the name)
4. With `OSC Manager` selected, look at the **Inspector** panel on the right
5. Click **Add Component** at the bottom of the Inspector
6. Search for `OSC Receiver` and select it

You should now see an **OSC Receiver** component on your object. Find the **Local Port** field and set it to `9000`. This is the port Unity will listen on — your microcontroller or bridge script will send data to this port.

> [!tip] Leave **Auto Connect** checked. This means Unity will start listening automatically when you enter Play Mode.

![[Screenshot 2026-05-06 160617.png]]

### Step 4 — Create a C# Script to Handle Incoming Data

Now you need a script that tells Unity what to *do* when an OSC message arrives. The script you need depends on which hardware path you're on — see Path A or Path B below. But first, here's how to create and attach any C# script in Unity:

1. In the **Project** panel (bottom of the screen), right-click in the **Assets** folder, create a **Scripts** folder
2. Choose **Create → C# Script**
3. Name it (e.g., `TouchReceiver` or `SensorReceiver`)
4. **Double-click** the script to open it in Visual Studio or Rider
5. Replace all the default code with the code from your path below
6. Save the file
7. Back in Unity, select your `OSC Manager` GameObject
8. Drag the script from the Project panel onto the Inspector (or use **Add Component** and search for the script name)
9. In the Inspector, you'll see a field labeled **Receiver** — drag the `OSC Manager` GameObject itself into that slot

---

## Path A — QT Py RP2040 + MPR121 → OSC → Unity

### What Your Board Is Already Sending

If you've followed the [[Signal Chain Setup Guide]], your RP2040 is already outputting lines like this over USB serial:

```
TOUCH,2,18
RAW,2,24
RELEASE,2,3
```

Each line is `EVENT,electrode_number,raw_value`. The RP2040 has no WiFi, so it can't send OSC directly. Instead, a small Python script on your laptop reads that serial data and forwards it as OSC messages to Unity.

### Step 1 — Install the Python Bridge Dependencies

Open a terminal (Mac: Terminal; Windows: Command Prompt or PowerShell) and run:

```bash
pip install pyserial python-osc
```

If you're on a Mac and get a permissions error, try:
```bash
pip3 install pyserial python-osc
```

### Step 2 — Find Your Serial Port

Plug in your RP2040 (make sure `boot.py` is on the board — see [[Signal Chain Setup Guide]]). Then:

**Mac:**
```bash
ls /dev/tty.usbmodem*
```
You'll see two entries. The data port is typically the one with the higher number (e.g., `/dev/cu.usbmodem2101`).

**Windows:**
Open Device Manager → expand **Ports (COM & LPT)**. You'll see two COM ports — try the one you haven't used before (usually the higher number, e.g., `COM5`).

### Step 3 — The Python Bridge Script

Create a new file on your laptop called `osc_bridge.py`. Paste in this code and edit the two lines marked with `← CHANGE THIS`:

>[!note] I put this script on the board.

```python
# DIGM 553 — Serial to OSC bridge
# Reads MPR121 touch data from RP2040 USB serial, forwards as OSC to Unity
#
# Requires: pip install pyserial python-osc

import serial
import time
from pythonosc import udp_client

# ── CONFIGURE THESE ────────────────────────────────────────────────────────────
SERIAL_PORT = "/dev/cu.usbmodem2101"   # ← CHANGE THIS to your data port - i.e. "COM7"
BAUD_RATE   = 115200
UNITY_IP    = "127.0.0.1"             # 127.0.0.1 = same computer as Unity - OSC Manager will give it to you
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
```

Run the script from your terminal:
```bash
python osc_bridge.py
```

When you touch an electrode, you should see output like:
```
  TOUCH  pad  2  raw=18
  RELEASE pad  2  raw=3
```

If you see `Error: [Errno 2] No such file or directory`, the serial port path is wrong — double-check Step 2.

### Step 4 — The Unity Script (Path A)

Create a C# script called `TouchReceiver` and paste in this code:

```csharp
using UnityEngine;
using extOSC;

// Attach this to the OSC Manager GameObject.
// Drag the OSC Manager itself into the "Receiver" field in the Inspector.
public class TouchReceiver : MonoBehaviour
{
    [Header("OSC — drag the OSC Manager GameObject here")]
    public OSCReceiver Receiver;

    // Called when Unity enters Play Mode
    private void OnEnable()
    {
        // Bind all 12 pads individually
        Receiver.Bind("/touch/0",  OnTouchReceived);
        Receiver.Bind("/touch/1",  OnTouchReceived);
        Receiver.Bind("/touch/2",  OnTouchReceived);
        Receiver.Bind("/touch/3",  OnTouchReceived);
        Receiver.Bind("/touch/4",  OnTouchReceived);
        Receiver.Bind("/touch/5",  OnTouchReceived);
        Receiver.Bind("/touch/6",  OnTouchReceived);
        Receiver.Bind("/touch/7",  OnTouchReceived);
        Receiver.Bind("/touch/8",  OnTouchReceived);
        Receiver.Bind("/touch/9",  OnTouchReceived);
        Receiver.Bind("/touch/10", OnTouchReceived);
        Receiver.Bind("/touch/11", OnTouchReceived);
    }

    private void OnDisable()
    {
        Receiver.Unbind(Receiver.Bind("/touch/0",  OnTouchReceived));
        Receiver.Unbind(Receiver.Bind("/touch/1",  OnTouchReceived));
        Receiver.Unbind(Receiver.Bind("/touch/2",  OnTouchReceived));
        Receiver.Unbind(Receiver.Bind("/touch/3",  OnTouchReceived));
        Receiver.Unbind(Receiver.Bind("/touch/4",  OnTouchReceived));
        Receiver.Unbind(Receiver.Bind("/touch/5",  OnTouchReceived));
        Receiver.Unbind(Receiver.Bind("/touch/6",  OnTouchReceived));
        Receiver.Unbind(Receiver.Bind("/touch/7",  OnTouchReceived));
        Receiver.Unbind(Receiver.Bind("/touch/8",  OnTouchReceived));
        Receiver.Unbind(Receiver.Bind("/touch/9",  OnTouchReceived));
        Receiver.Unbind(Receiver.Bind("/touch/10",  OnTouchReceived));
        Receiver.Unbind(Receiver.Bind("/touch/11",  OnTouchReceived));
    }

    private void OnTouchReceived(OSCMessage message)
    {
        // Extract the pad number from the OSC address (e.g. "/touch/3" → 3)
        string[] parts = message.Address.Split('/');
        int padIndex = int.Parse(parts[2]);

        int value = message.Values[0].IntValue; // 1 = touch, 0 = release

        if (value == 1)
        {
            Debug.Log($"Pad {padIndex} TOUCHED");
            // ── Put your logic here ──────────────────────────────────────
            // Examples:
            //   Play a sound:        AudioSource.PlayClipAtPoint(myClip, transform.position);
            //   Move an object:      myObjects[padIndex].transform.position += Vector3.up;
            //   Trigger an effect:   myParticles[padIndex].Play();
            // ────────────────────────────────────────────────────────────
        }
        else
        {
            Debug.Log($"Pad {padIndex} RELEASED");
        }
    }
}
```

Follow the steps in **Part 1 → Step 4** to attach this script to your `OSC Manager` object.

![[Screenshot 2026-05-06 160606.png]]

### Step 5 — Test It

1. Run `osc_bridge.py` in your terminal (leave it running)
2. In Unity, press **Play**
3. Touch an electrode on the MPR121
4. Look at the **Console** panel in Unity — you should see `Pad 2 TOUCHED` (or whichever electrode you touched)

If you see messages in the Console, data is flowing. Now replace the `Debug.Log` lines in the script with whatever your project needs.

> [!tip] Run Unity and the bridge script **on the same computer**. The `UNITY_IP = "127.0.0.1"` setting in the bridge script means "send to myself" — no network configuration needed.

---

>[!ERROR] I Do not have this specific board (the APDS-9999) while I can confirm the process and setup for the ESP32-S3 Feather board. I cannot confirm or validate the working code specifically for the APDS-9999. However, based on the Adafruit example code, it should look similar to this. 

## Path B — Feather ESP32 + APDS-9999 → WiFi OSC → Unity

The Feather ESP32 has built-in WiFi, so it can send OSC packets directly over your local network. YOU DO NOT NEED TH BRDIGE SCRIPT FROM ABOVE. The workflow is: sense → format as OSC → send via UDP → Unity receives. Like the RP2040, it runs **CircuitPython** and you edit files in **VS Code**.

> [!note] This guide is written for the **Adafruit Feather ESP32** family with a STEMMA QT connector (ESP32-S2 or ESP32-S3). If you're not sure which variant you have, check the back of the board.

### What the APDS-9999 Gives You

The APDS-9999 is a combined color, proximity, and ambient light sensor. Unlike the APDS-9960.
Over OSC you'll receive:

| OSC Address | Value | Range |
|---|---|---|
| `/sensor/proximity` | integer | 0 (far) – 255 (close) |
| `/sensor/color/r` | integer | 0–255 (normalized) |
| `/sensor/color/g` | integer | 0–255 (normalized) |
| `/sensor/color/b` | integer | 0–255 (normalized) |
| `/sensor/lux` | float | 0.0+ (ambient light in lux) |

### Step 3 — Install CircuitPython Libraries

CircuitPython uses a `lib/` folder on the `CIRCUITPY` drive. You copy library files there manually — same process as the RP2040.

**Get the library bundle:**

Download the **Adafruit CircuitPython Bundle** from:
https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases

Download the bundle matching your CircuitPython version (e.g., `adafruit-circuitpython-bundle-9.x-mpy-YYYYMMDD.zip`). Unzip it.

**Copy these into the `lib/` folder on `CIRCUITPY`:**

```
adafruit_apds9999.mpy          ← the APDS-9999 library
adafruit_simplemath.mpy        ← adafruit pymath
adafruit_bus_device/           ← folder, required dependency
adafruit_register/             ← folder, required dependency
```

### Step 4 — Wire the APDS-9999

Use a **STEMMA QT / Qwiic cable** (the small 4-pin JST cable):

1. Plug one end into the STEMMA QT port on the **Feather ESP32** (on the end of the board)
2. Plug the other end into either STEMMA QT port on the **APDS-9999** breakout

That's the full wiring. Power and I2C data all travel on the one cable.

### Step 5 — Find Your Computer's IP Address

The Feather needs to know where to send OSC data. Find the IP address of the computer running Unity:

**Mac:** Open Terminal and run:
```bash
ipconfig getifaddr en0
```
You'll get something like `192.168.1.47`. Write this down.

**Windows:** Open Command Prompt and run:
```
ipconfig
```
Look for **IPv4 Address** under your active WiFi adapter. It will look like `192.168.1.47`.

> [!warning] Your computer and the Feather must be on the **same WiFi network**. School or university networks (like `dragonfly3`) sometimes have **client isolation** enabled, which blocks devices from communicating with each other. That is why I bring my TP-Link to class, to bypass this.

### Step 6 — Configure WiFi Credentials

CircuitPython 8+ stores secrets in a `settings.toml` file on the `CIRCUITPY` drive — never hardcode credentials in `code.py`.

Create (or open) `settings.toml` on the `CIRCUITPY` drive and fill it in:

```toml
# settings.toml — WiFi and OSC configuration
# This file stays on the board; do not share or commit it

CIRCUITPY_WIFI_SSID = "YOUR_NETWORK_NAME"
CIRCUITPY_WIFI_PASSWORD = "YOUR_PASSWORD"
UNITY_IP = "192.168.1.47" <- This needs to match with Unity OSC Manager as well
UNITY_PORT = "9000"
```

Replace the values with your actual network name, password, and your computer's IP from Step 5.

### Step 7 — The CircuitPython Code

Save this as `code.py` on the `CIRCUITPY` drive. The board runs it automatically on save.

```python
# DIGM 553 — Feather ESP32 + APDS-9999 → WiFi OSC → Unity
# Sends proximity, normalized RGB color, and ambient lux as OSC messages via UDP
#
# Libraries: adafruit_apds9999
# Credentials: set in settings.toml, not here

import os
import time
import struct
import board
import busio
import wifi
import socketpool
from adafruit_apds9960.apds9960 import APDS9960  # type: ignore

# ── LOAD CONFIG FROM settings.toml ────────────────────────────────────────────
WIFI_SSID  = os.getenv("CIRCUITPY_WIFI_SSID")
WIFI_PASS  = os.getenv("CIRCUITPY_WIFI_PASSWORD")
UNITY_IP   = os.getenv("UNITY_IP")
UNITY_PORT = int(os.getenv("UNITY_PORT", "9000"))

# ── OSC HELPER ─────────────────────────────────────────────────────────────────
def _pad4(data: bytes) -> bytes:
    """Pad bytes to the next 4-byte boundary with nulls."""
    r = len(data) % 4
    return data + (b"\x00" * (4 - r)) if r else data

def osc_message(address: str, *args) -> bytes:
    """
    Build a minimal OSC message payload.
    Supported types: int, float.
    """
    addr_bytes = _pad4(address.encode() + b"\x00")

    tags = ","
    for a in args:
        tags += "i" if isinstance(a, int) else "f"
    tag_bytes = _pad4(tags.encode() + b"\x00")

    data = b""
    for a in args:
        data += struct.pack(">i", a) if isinstance(a, int) else struct.pack(">f", a)

    return addr_bytes + tag_bytes + data

# ── WIFI ───────────────────────────────────────────────────────────────────────
print(f"Connecting to {WIFI_SSID}...")
wifi.radio.connect(WIFI_SSID, WIFI_PASS)
print(f"Connected! Feather IP: {wifi.radio.ipv4_address}")
print(f"Sending OSC to {UNITY_IP}:{UNITY_PORT}")

pool = socketpool.SocketPool(wifi.radio)
sock = pool.socket(pool.AF_INET, pool.SOCK_DGRAM)

def send_osc(address: str, *args):
    sock.sendto(osc_message(address, *args), (UNITY_IP, UNITY_PORT))

# ── SENSOR ─────────────────────────────────────────────────────────────────────
i2c = busio.I2C(board.SCL1, board.SDA1)
sensor = APDS9960(i2c)

sensor.enable_proximity = True
sensor.enable_color = True

print("Sensor ready. Sending data...")

# ── MAIN LOOP ─────────────────────────────────────────────────────────────────
while True:
    # Proximity (0 = far, 255 = close)
    proximity = sensor.proximity
    send_osc("/sensor/proximity", int(proximity))

    # Color + Lux
    if sensor.color_data_ready:
        r, g, b, c = sensor.color_data   # raw 16-bit RGBC values

        if c > 0:
            # Normalize each channel to 0–255 using the clear channel
            rn = min(255, int(r * 255 / c))
            gn = min(255, int(g * 255 / c))
            bn = min(255, int(b * 255 / c))
            send_osc("/sensor/color/r", rn)
            send_osc("/sensor/color/g", gn)
            send_osc("/sensor/color/b", bn)

        # Lux — calculated from the RGBC channels
        lux = sensor.calculate_lux(r, g, b)
        send_osc("/sensor/lux", float(lux))

    time.sleep(0.02)   # ~50 Hz
```

### Step 8 — Check the Serial Console

After saving `code.py`, restart the board. Open the Serial Monitor in VS Code, connect to the correct COM port, and you should see:

```
Connecting to MyNetwork...
Connected! Feather IP: 192.168.1.53
Sending OSC to 192.168.1.47:9000
Sensor ready. Sending data...
```

If WiFi fails to connect, check `settings.toml` — the SSID and password are case-sensitive. If the sensor errors, check the STEMMA QT cable seating.

### Step 9 — The Unity Script (Path B)

Create a C# script called `SensorReceiver` and paste in this code:

```csharp
using UnityEngine;
using extOSC;

// Attach this to the OSC Manager GameObject.
// Drag the OSC Manager itself into the "Receiver" field in the Inspector.
public class SensorReceiver : MonoBehaviour
{
    [Header("OSC — drag the OSC Manager GameObject here")]
    public OSCReceiver Receiver;

    [Header("Optional: drag a GameObject to control with proximity")]
    public Transform ProximityTarget;

    [Header("Optional: drag a Renderer to control with color")]
    public Renderer ColorTarget;

    [Header("Optional: drag a Light to control with lux")]
    public Light AmbientLight;

    private void OnEnable()
    {
        Receiver.Bind("/sensor/proximity", OnProximityReceived);
        Receiver.Bind("/sensor/color/r",   OnColorRReceived);
        Receiver.Bind("/sensor/color/g",   OnColorGReceived);
        Receiver.Bind("/sensor/color/b",   OnColorBReceived);
        Receiver.Bind("/sensor/lux",       OnLuxReceived);
    }

    private void OnDisable()
    {
        Receiver.Unbind(Receiver.Bind("/sensor/proximity", OnProximityReceived));
        Receiver.Unbind(Receiver.Bind("/sensor/color/r",   OnColorRReceived));
        Receiver.Unbind(Receiver.Bind("/sensor/color/g",   OnColorGReceived));
        Receiver.Unbind(Receiver.Bind("/sensor/color/b",   OnColorBReceived));
        Receiver.Unbind(Receiver.Bind("/sensor/lux",       OnLuxReceived));
    }

    // Running values for color (updated separately per channel)
    private float _r, _g, _b;

    private void OnProximityReceived(OSCMessage message)
    {
        float proximity = message.Values[0].IntValue / 255f; // normalize to 0–1

        Debug.Log($"Proximity: {proximity:F2}");

        if (ProximityTarget != null)
        {
            // Example: scale an object based on proximity
            float scale = Mathf.Lerp(0.1f, 3f, proximity);
            ProximityTarget.localScale = Vector3.one * scale;
        }
    }

    private void OnColorRReceived(OSCMessage message)
    {
        _r = message.Values[0].IntValue / 255f;
        UpdateColor();
    }

    private void OnColorGReceived(OSCMessage message)
    {
        _g = message.Values[0].IntValue / 255f;
        UpdateColor();
    }

    private void OnColorBReceived(OSCMessage message)
    {
        _b = message.Values[0].IntValue / 255f;
        UpdateColor();
    }

    private void UpdateColor()
    {
        if (ColorTarget != null)
        {
            ColorTarget.material.color = new Color(_r, _g, _b);
        }
    }

    private void OnLuxReceived(OSCMessage message)
    {
        float lux = message.Values[0].FloatValue;

        Debug.Log($"Lux: {lux:F1}");

        if (AmbientLight != null)
        {
            // Example: dim/brighten a scene light based on ambient light level
            // Clamp to a reasonable range — adjust maxLux to match your environment
            float maxLux = 500f;
            AmbientLight.intensity = Mathf.Clamp(lux / maxLux, 0f, 1f) * 3f;
        }

        // ── Other things you could do with lux ──────────────────────────────
        // Trigger an event at low light:  if (lux < 20f) OnDark();
        // Map to fog density:             RenderSettings.fogDensity = 1f - (lux / maxLux);
        // ────────────────────────────────────────────────────────────────────
    }
}
```

Attach it to the `OSC Manager` object and optionally drag in a **ProximityTarget** (any GameObject) and a **ColorTarget** (any GameObject with a Renderer, like a Cube) to see the data drive something immediately.

![[Screenshot 2026-05-06 160557.png]]

### Step 9 — Test It

1. In Unity, press **Play**
2. Point your hand at the APDS-9999 — move it closer and farther
3. Check the Unity Console — you should see `Proximity: 0.73` and `Lux: 142.0` (or similar) updating in real time
4. If you assigned a ProximityTarget, the object should scale as your hand moves; if you assigned an AmbientLight, its intensity should respond to the room's light level

> [!tip] If you see nothing in the Console: confirm your computer's IP address in `settings.toml` is correct, confirm both devices are on the same WiFi network, and check that Unity's OSC Receiver Local Port is `9000`.

---
---
