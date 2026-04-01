---
title: "Hardware and Software Inventory"
week: 1
module: W01C
tags: [DIGM553, week01]
---
# W01C — Hardware and Software Inventory

> *"The digital system is material in its body, electric in function, and symbolic in control."*
> — Magnusson, *Sonic Writing*

---

## This Is Not a Setup Guide

You could read this note as a checklist of tools we *might* be using this term. But given what we've spent W01A and W01B establishing that tools are epistemic, that instruments condition what can be thought, that amplification is always also reduction. Well, we can't rightly do that with a straight face, can we?

Instead, consider this an **epistemic inventory**. For each element of the course toolkit, we'll be asking: what does this tool make possible, what does it foreclose, and why did we choose it?

---

## The Core Signal Chain

The physical-digital entanglement at the center of this course runs through a specific signal chain (maybe not this specifically, but something similar):

```
Body / Material World
        ↓
  MPR121 Sensor (capacitive touch)
        ↓
  Adafruit QT Py RP2040 (microcontroller)
        ↓
  CircuitPython (embedded code)
        ↓
  OSC / UDP (protocol over Wi-Fi)
        ↓
  TouchDesigner / Max/MSP / Ableton (host software)
        ↓
  Sound, Image, Data Output
```

> Each arrow in this chain is a transformation. Each of those transformations amplifies something and also reduces something else.

---

## Hardware

### Adafruit QT Py RP2040

The QT Py RP2040 is a small microcontroller board built around the Raspberry Pi RP2040 chip. It runs CircuitPython a version of Python designed for embedded systems with limited memory and no operating system. 
- Or it can also run Arduino or PlatformIO both versions of C++ for embedded systems.

**Why this board, epistemically?**

The QT Py is small enough to embed in an object, a garment, or a physical installation. We couldn’t do that with a desktop PC. So, this changes the relationship between the body and the computation. The computation moves toward the body rather than the body moving toward the computation. This also presents a design decision with consequences for what kind of physical-digital entanglement is possible.

It also has explicit constraints: limited memory, no file system (without an SD card), no display, no persistent storage across power cycles. These are `enabling constraints`. They push us toward thinking about computation as a *real-time* process happening *in* a physical context, not a processing pipeline running on a workstation, rendered, then presented.

**Ihde's modalities here:** In typical use, the microcontroller operates in a hermeneutic relation, meaning it produces data (sensor readings) that you then interpret in software. But as your fluency develops, it can shift toward an embodiment relation, where the hardware/body interface recedes and you're thinking directly in terms of interaction rather than data.

### MPR121 Capacitive Touch Sensor

The MPR121 detects electrical conductance at 12 separate electrode points. When a conductive object (a finger, a body part, water, conductive thread, foil, fruit, etc.) comes near or touches an electrode, the sensor registers a change in capacitance.

**Epistemic specifics:**

The MPR121 models the world as *twelve discrete contact points with threshold values*. It does not model pressure, velocity, texture, or gesture in any richer sense. This is a fairly substantial reduction, but also a generative constraint.

> [!question]- Why 12? A speculative aside on hardware and tonality
> The MPR121's 12-electrode architecture is almost certainly a pragmatic engineering choice. 12 is a highly composite number, divisible by 1, 2, 3, 4, 6, and 12 — which makes it a natural [Schelling point](https://en.wikipedia.org/wiki/Focal_point_(game_theory)) in design: enough channels for most multi-touch applications, manageable over I2C, and culturally unremarkable. We already organise time in 12s (months, hours (non-24)), commerce in 12s (dozens, gross), and space in 12s (inches to the foot). All this to say, the number doesn't need music theory to justify itself.
>
> But the coincidence is worth sitting with, I think: 12 also happens to map cleanly onto the chromatic scale of Western 12-tone equal temperament. A person who assigns one pitch per electrode isn't fighting the hardware. They'd working with a latent affordance the chip happens to carry. Whether that affordance was designed or accidental doesn't change the fact that it's *there*, and that it quietly favors a particular musical cosmology over others.
>
> The epistemic question it opens: *what would a 19-electrode sensor do to your compositional assumptions?* What practices would suddenly feel natural, and whose tuning systems, microtonal, spectral, non-Western, would feel less like workarounds?

What this reduction enables: you have to build gestural richness out of combination, sequencing, timing, and creative use of what "electrode" means materially. The sensor touching a piece of copper tape embedded in a textile or paper is not the same experience as touching a pad on a breakout board, even if the the electrical signal may be identical.

The sensor does not care about the materiality of what it touches. That indifference is the limitation. Making that indifference *expressive* is the research-creation challenge.

### Zoom H5

The Zoom H5 is a portable, mid-range field recorder. Four inputs (two XLR combo jacks, plus the built-in X/Y capsule pair), 24-32bit/96kHz recording, small enough to carry anywhere.

**Epistemic framing:** The H5 models the world as *microphone placements and headroom*. Unlike software recording, field recording asks you to solve problems in space and time before you can solve them in software. You can't EQ a bad room placement (kinda). The recorder forces decisions about *where you are* and *where the sound is* in a way that a software sampler does not.

The H5 is also a tool for practice-based research: documentation, listening, locating yourself in a sonic environment. Used as a research tool (not just a production tool), it is a way of attending to a space before you decide what to make there.

---

## Software

### CircuitPython

CircuitPython is Python stripped down for embedded environments. The key constraint: no concurrency, no threads, single-threaded event loop. Your code runs top to bottom, repeatedly, in a tight main loop.

**Epistemic consequence:** You cannot think about this system the way you think about desktop software. There is no background thread listening for events while the foreground does something else. Everything is sequential. This forces particular models of time, interaction, and performance. Actually, one that is closer to how musical performance works (step by step, no stopping) than how most software development works.

The loop structure also makes the code's relationship to time explicit. The latency between sensing and responding is determined by how much work you do in each loop iteration. You feel computation as time.

### OSC (Open Sound Control) over UDP

OSC is a protocol originally designed for real-time communication between musical instruments and software. It uses the UDP networking protocol, which means messages are sent in discrete packets that can arrive out of order or not at all. It is a protocol that prioritizes low latency over guaranteed delivery.

**Epistemic framing:** OSC messages have a specific structure: an address pattern (like `/sensor/touch/1`) and typed arguments. This structure makes the musical/physical origin of the data visible in the data itself. Unlike MIDI, which was designed around keyboard-and-note-number logic, OSC is relatively free, the address namespace is whatever you define.

The UDP choice (vs. TCP) is itself an argument about what matters: latency matters more than reliability. For real-time physical interaction, a dropped packet is usually less harmful than a 50ms delay. This is a design philosophy embedded in the computation and protocol.

### TouchDesigner

TouchDesigner is a node-based visual programming environment developed by Derivative, used widely for real-time visual performance, interactive installations, and physical computing. It receives OSC messages (among may other protocols like DMX, MIDI, etc.), processes them in a dataflow graph, and routes the results to visual, audio, or other outputs.

**Epistemic specifics:**

TouchDesigner models the world as a **cooking** system: operators (nodes) either cook (update their output) or don't, based on whether their inputs have changed. This is a specific model of reactive computation, and it is one that is very well suited for real-time visual work and less natural for sequential or text-based logic.

The node-based paradigm also has an epistemological consequence: your *decisions* are made visible as *connections*. You can see the shape of your logic. This is different from writing code in an IDE, where the structure of your reasoning is embedded in and enabled by syntax. 

The defaults matter here (returning to Magnusson): the built-in operators in TouchDesigner assume certain things about color, resolution, framerate, and timing that reflect the tool's origins in VVVV and cinema-influenced real-time graphics. When you use those defaults without questioning them, you're (perhaps subconsciously) making an implicit argument about what your work should look like.

### Max/MSP

Max/MSP (and its twin PureData) are the older cousins of TouchDesigner. They are node-based environments with deeper roots in algorithmic musical composition and signal processing. Where TouchDesigner is GPU-native and optimized for visual output, Max is CPU-native and optimized for audio, MIDI, and raw numerical data.

**Why both?** The choice between TouchDesigner and Max is not always a purely technical one. Often times, it is partly a question of disciplinary genealogy. TouchDesigner comes from the VJ / visual performance world; Max comes from the electroacoustic music world. They carry different assumptions about what a "performance" is, what "real-time" means, and what relationship between software and body is natural.

Using both is an opportunity to feel those differences in your body as you work and to make that felt for anyone interacting with your work.

---

## The Inventory as Critical Practice

Here is the exercise this note is preparing you for:

**Do your own epistemic inventory.** Pick tool(s) you already use in your practice, any tool(s) really, not necessarily the ones listed here. For each one:

1. What does it amplify? (What becomes easy, visible, measurable?)
2. What does it reduce? (What disappears, becomes invisible, gets rounded off?)
3. What world does it assume exists? (What is the implicit model of activity, interaction, body, material that its design encodes?)
4. Who designed those assumptions, and for what context?

*This exercise is the foundation of  one of your ASN 2 (Critical Technical Journal).*

---

## Key Terms

- **Signal chain** — the full sequence of transformations from physical world to digital output; each link is a reduction/amplification pair
- **OSC (Open Sound Control)** — a real-time messaging protocol that allows physical sensors and software to communicate; address-based, free-form namespace
- **Capacitive touch** — detection of electrical conductance changes; models touch as threshold-crossing events at discrete electrode points
- **Cooking system** — TouchDesigner's model of reactive computation; operators update only when inputs change
- **Default assumptions** — the inherited worldviews encoded in software's standard settings and built-in abstractions

---

## Thinking Toward Your Own Sensors

The hardware described above is the course's core signal chain — but it is not a prescription for yours. Before choosing sensors or purchasing hardware, work through your own practice first.

See → [[../../../Documents/Hardware Clarifications — Thinking Toward Sensors|Hardware Clarifications — Thinking Toward Sensors]] for a framework on how to move from practice thinking to sensor selection, a clarification on Stemma QT vs Qwiic, and the prompt to complete before our next hardware conversation.

---

## Setup Reference

For CircuitPython + MPR121 + OSC → TouchDesigner:

- [Adafruit CircuitPython documentation](https://docs.circuitpython.org/)
- [MPR121 CircuitPython library](https://github.com/adafruit/Adafruit_CircuitPython_MPR121)
- [TouchDesigner OSC In CHOP documentation](https://derivative.ca/UserGuide/OSC_In_CHOP)
- [MicroOSC library for CircuitPython](https://github.com/todbot/CircuitPython_MicroOSC) 
- [Additional Adafruit CircuitPython libraries](https://learn.adafruit.com/circuitpython-essentials/circuitpython-libraries)

---

---

## Connected Threads

[[../../Threads/Physical-Digital Entanglement|Physical-Digital Entanglement]]
[[../../Threads/Epistemic Tools|Epistemic Tools]]
[[../../Threads/Enabling Constraints|Enabling Constraints]]
