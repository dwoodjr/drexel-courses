---
title: "Reading Sensors, Reading Docs"
tags: [DIGM553, hardware, sensors, debugging, documentation]
---

# Reading Sensors, Reading Docs
## A Practical Guide to Figuring Things Out

> You will probably spend more time figuring out what your sensor is doing than you will spend building with it. That is just how this works. And that is okay.
>
> A sensor is more like an instrument than a switch. It has a range, a feel, a set of tendencies. You learn it by practicing with it, listening to it, before you decide what to do with it.
> 
>  Hopefully, this guide can give you some method for doing that.

---

## The core habit: print first, map later

Before you wire anything into TouchDesigner, before you think about what the data will *do*, find out what it actually *is*.

The fastest way to do this is to print raw values directly from CircuitPython to the REPL/Console.

```python
import time

# (your sensor setup here)

while True:
    print(sensor.some_value)
    time.sleep(0.1)
```

Watch the numbers for a minute. Move your hand over the sensor. Get close, then far. Change the lighting. Cover it. Let it sit completely still. Ask yourself:

- What is the range? What's the lowest value you see? The highest?
- How fast does it change?
- Is it noisy (jumping around randomly) or stable?
- What happens at the edges, when nothing is happening, when something is happening strongly?

**You cannot make good creative decisions about data you haven't looked at.** A value that ranges from 0 to 65535 needs to be handled very differently from one that ranges from 18.0 to 32.0. A noisy signal may need smoothing (maybe) before it can drive something. A slow-moving signal might need amplification. None of this is visible until you look at it raw.

---

## Know your range: empirically and from the datasheet

There are two ways to find out what values your sensor produces: you can observe it (empirical) and you can look it up (documentation). Do both of these, because they tell you different things.

**Observing** tells you what the sensor does in your specific environment, with your specific setup, under the conditions of your project. This is always the ground truth.

**The datasheet** tells you the theoretical limits of the hardware. The absolute maximum and minimum values the sensor is capable of producing. It also tells you what those values “*mean*.” What physical quantity they correspond to, and how to convert them to useful units.

When they disagree, and sometimes they do, trust what you observe, but use the datasheet to understand why.

---

## Normalize everything to 0.0 – 1.0 (when it makes sense to)

Once you know your range, one of the most useful habits you can build is **normalizing** — scaling any sensor value to a 0.0 to 1.0 range before you do anything else with it. It is simpler to work with 0-1 than with, say, 0-4095.

```python
# Raw value from sensor
raw = sensor.proximity   # ranges from 0 to 255

# Normalize to 0.0 – 1.0
normalized = raw / 255.0
```

Now `normalized` is 0.0 when nothing is near and 1.0 when something is very close. It doesn't matter what the original range was, everything in 0–1 space speaks the same language.

From there, **mapping** means scaling that 0–1 value to whatever range your output needs:

```python
# Map normalized value to a TouchDesigner color parameter (0.0 – 1.0 already)
color = normalized

# Map to an audio frequency range (200Hz – 2000Hz)
frequency = 200 + (normalized * 1800)

# Map to a rotation in degrees (0° – 360°)
rotation = normalized * 360
```

The formula for most mappings will follow the same logic:

```python
output = output_min + (normalized * (output_max - output_min))
```

This is where your creative decisions actually live. The sensor doesn't decide what the data means for your work. You do, through the choices you make in mapping.

---

## Test the chain one link at a time

When something isn't working, the instinct is to look at the whole system at once. This almost never helps. Instead, test each link in the chain independently, from the sensor outward.

```
sensor hardware
      ↓
CircuitPython (reads sensor, formats message)
      ↓
USB serial (sends text to your computer)
      ↓
TouchDesigner (receives, parses, maps)
```

**Step 0 — Is the sensor on or powered?**
Is thing on? Are you reading me?

**Step 1 — Is the sensor being read?**
Add a `print()` inside your loop and watch the REPL/Console. If values appear and change when you interact with the sensor, this link is working. If you get an error, it's a wiring or library problem.

```python
while True:
    print(sensor.color_raw)   # does this print anything?
    time.sleep(0.1)
```

**Step 2 — Is the serial message formatted correctly?**
Print the exact string you're building before you send it. Look at it carefully, is it what you expect?

```python
msg = f"tcs,{r},{g},{b},{c}\n"
print(repr(msg))   # repr() shows you hidden characters like \n
serial.write(msg.encode())
```

**Step 3 — Is the software receiving anything?**
Open the object that imports the data and watch it. You should see raw lines appearing. If you don't, the problem is likely the serial connection. Check the port, check that no other app has the port open.

**Step 4 — Is the software parsing it correctly?**
Add a `print()` inside a DAT Execute script in TD:

```python
def onRowChange(dat, rows):
    for row in rows:
        line = dat[row, 0].val.strip()
        print(f"received: {line}")          # does this show up in the Textport?
        parts = line.split(',')
        print(f"parts: {parts}")            # are the parts what you expect?
```

***Isolating each step means you always know exactly where the problem is.*** This is called narrowing the scope.

---

## Reading documentation

Documentation is a set of answers to questions you haven't asked yet. The skill is knowing which questions to ask and where to look for the answers.

### Where to find it

**For Adafruit sensors**, start at the Adafruit product page for your specific sensor — search the sensor name plus "Adafruit." The product page has:
- A wiring diagram
- A CircuitPython quickstart guide with working example code
- Links to the CircuitPython library documentation

This is almost always your first stop. Adafruit's documentation is among the best in the hardware world: clear, practical, and written for people learning.

**For the CircuitPython library API**, go to [docs.circuitpython.org](https://docs.circuitpython.org) and search for the library name. This tells you every property and method the library exposes — what you can ask the sensor for, and what type of value you get back.

**For the sensor hardware itself**, search for the sensor part number (e.g., "TCS3430 datasheet") and look for a PDF from the manufacturer. The datasheet is the authoritative source on what the hardware is physically capable of.

### What to look for in a datasheet

Datasheets are written for electrical engineers and can be intimidating. Read for what you need, not cover to cover. Look for:

**Electrical characteristics / specifications table** — This usually appears near the front. Look for the operating voltage, current draw, and the output range for each measurement. This tells you what numbers to expect.

**Measurement description** — A section explaining what the sensor is actually measuring. For a color sensor, this tells you whether values are raw counts, lux, or something else, and how to interpret them.

**I2C address** — If you need to put two of the same sensor on the same bus, you'll need to change the address on one of them. The datasheet tells you what addresses are available and how to select them.

**Application / example circuits** — Often near the end. Sometimes useful for wiring reference.

The rest you can safely skip until you have a specific question later. Which you will…

### What to look for in CircuitPython library docs

Find the class for your sensor and look at its **properties** (the values you can read). For example, the AMG8833 library has a `pixels` property that returns the 8×8 temperature grid. The docs tell you the return type (list of lists), the units (degrees Celsius), and the range.

If a property isn't behaving as expected, check:
- What type does it return? (integer, float, tuple, list?)
- What are the units? (counts, lux, Celsius, normalized 0–1?)
- Does it require anything to be enabled first?

### When you can't find the answer

Search specifically. "APDS9999 CircuitPython proximity range" will get you further than "APDS9999 not working." The Adafruit forums and the CircuitPython GitHub issues are both indexed by Google and often have exactly the question you're asking.

If you find an answer in a forum post or GitHub issue, check the date. CircuitPython libraries update frequently and behavior can change between versions. An old answer might still work, but it might not. Verify against the current docs.

---

## Thinking with your sensor

The most useful shift in how you approach this work is moving from "how do I make it do what I want" to "what does it want to do, and what can I make of that?"

Every sensor has tendencies. The AMG8833's 8×8 resolution means it sees the world in 64 squares — that limiting constraint gives the data a particular character. The TCS3430 responds differently to different light temperatures in ways that are unpredictable until you test them in your actual space.

These are the sensor's personality: the particular way it translates the physical world into numbers. Work with that.

Print the raw values. Watch them. Find the edges. Then decide what to do.

---

## How to find good information when you're stuck

Not all sources are equally useful. When you're troubleshooting, knowing where to look, and how much to trust what you find, saves enormous amounts of time.

**High trust:**
- Manufacturer documentation and official datasheets
- The official CircuitPython library documentation (docs.circuitpython.org)
- Adafruit's product guides and Learning System tutorials
- The official GitHub repository for any library you're using

These sources are authoritative. They describe what the hardware and software actually do. When in doubt, go here first.

**Medium trust:**
- Stack Overflow answers with significant upvotes and a recent date
- Adafruit and Arduino forum posts where the original poster confirmed the solution worked
- GitHub issues where the problem was resolved

These are often genuinely useful but require some judgment. Check the date — library behavior changes between versions. Check whether the person asking had the same specific situation you have.

**Low trust:**
- Random blog posts and tutorials of unknown origin
- YouTube tutorials without a clear author or source
- AI-generated answers (including from tools like ChatGPT or Claude)

This last point is worth dwelling on. AI tools can be useful for understanding concepts, getting oriented in an unfamiliar area, or generating starting-point code. But they will confidently give you wrong library calls, outdated syntax, and hallucinated function names. Anything an AI tells you about specific code should be verified against the actual documentation before you use it. The documentation is the ground truth. The AI is a starting point.

**The search itself is a skill.** "APDS9999 not working" will get you nowhere. "APDS9999 CircuitPython proximity always returns 0" will get you somewhere. Be specific about the sensor, the platform, the symptom, and the context. The more precisely you can describe what's actually happening, the better your results.

---
