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

You could read this note as a checklist of tools we'll be using this term. But given what we've spent W01A and W01B establishing — that tools are epistemic, that instruments condition what can be thought, that amplification is always also reduction — we can't do that with a straight face.

This is an **epistemic inventory**. For each element of the course toolkit, we're asking: what does this tool make possible, what does it foreclose, and why did we choose it?

---

## The Core Signal Chain

The physical-digital entanglement at the center of this course runs through a specific signal chain:

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

Each arrow in this chain is a transformation — and each transformation amplifies something and reduces something. Understanding that chain, point by point, is what W01C is about.

---

## Hardware

### Adafruit QT Py RP2040

The QT Py RP2040 is a small microcontroller board built around the Raspberry Pi RP2040 chip. It runs CircuitPython — a version of Python designed for embedded systems with limited memory and no operating system.

**Why this board, epistemically?**

The QT Py is small enough to embed in an object, a garment, or a physical installation — it is not a "computer at a desk." This changes the relationship between the body and the computation. The computation moves toward the body rather than the body moving toward the computation. This is a design decision with consequences for what kind of physical-digital entanglement is possible.

It also has explicit constraints: limited memory, no file system (without an SD card), no display, no persistent storage across power cycles. These are enabling constraints — they push you toward thinking about computation as a *real-time* process happening *in* a physical context, not a processing pipeline running on a workstation.

**Ihde's modalities here:** In typical use, the microcontroller operates in a hermeneutic relation — it produces data (sensor readings) that you then interpret in software. But as your fluency develops, it can shift toward an embodiment relation, where the hardware/body interface recedes and you're thinking directly in terms of interaction rather than data.

### MPR121 Capacitive Touch Sensor

The MPR121 detects electrical conductance at 12 separate electrode points. When a conductive object (a finger, a body part, water, conductive thread, foil, fruit) comes near or touches an electrode, the sensor registers a change in capacitance.

**Epistemic specifics:**

The MPR121 models the world as *twelve discrete contact points with threshold values*. It does not model pressure, velocity, texture, or gesture in any richer sense. This is a substantial reduction — and a generative constraint.

What this reduction enables: you have to build gestural richness out of combination, sequencing, timing, and creative use of what "electrode" means materially. The sensor touching a piece of copper tape embedded in a textile is not the same experience as touching a pad on a breakout board — even though the electrical signal may be identical.

The sensor does not care about the materiality of what it touches. That indifference is the limitation. Making that indifference *expressive* is the research-creation challenge.

**Somax2 parallel:** IRCAM's Somax2 system works with a similar epistemological structure at a different scale — it models musical input as sequences of symbolic events, reducing the richness of live performance to labeled categories that can be used to drive improvisation. The reduction enables the machine to respond; but the quality of the musical interaction depends entirely on how thoughtfully the reduction was designed. Same principle applies here.

---

## Software

### CircuitPython

CircuitPython is Python stripped down for embedded environments. The key constraint: no concurrency, no threads, single-threaded event loop. Your code runs top to bottom, repeatedly, in a tight main loop.

**Epistemic consequence:** You cannot think about this system the way you think about desktop software. There is no background thread listening for events while the foreground does something else. Everything is sequential. This forces a particular model of time — one that is actually closer to how musical performance works (step by step, no stopping) than how most software development works.

The loop structure also makes the code's relationship to time explicit. The latency between sensing and responding is determined by how much work you do in each loop iteration. You feel computation as time.

### OSC (Open Sound Control) over UDP

OSC is a protocol originally designed for real-time communication between musical instruments and software. It uses the UDP networking protocol, which means messages are sent in discrete packets that can arrive out of order or not at all — the protocol prioritizes low latency over guaranteed delivery.

**Epistemic framing:** OSC messages have a specific structure: an address pattern (like `/sensor/touch/1`) and typed arguments. This structure makes the musical/physical origin of the data visible in the data itself. Unlike MIDI, which was designed around keyboard-and-note-number logic, OSC is relatively free — the address namespace is whatever you define. You are naming the world as you instrument it.

The UDP choice (vs. TCP) is itself an argument about what matters: latency matters more than reliability. For real-time physical interaction, a dropped packet is usually less harmful than a 50ms delay. This is a design philosophy embedded in the protocol.

### TouchDesigner

TouchDesigner is a node-based visual programming environment developed by Derivative, used widely for real-time visual performance, interactive installations, and physical computing. It receives OSC messages, processes them in a dataflow graph, and routes the results to visual, audio, or other outputs.

**Epistemic specifics:**

TouchDesigner models the world as a **cooking** system — operators (nodes) either cook (update their output) or don't, based on whether their inputs have changed. This is a specific model of reactive computation — one that is very good for real-time visual work and less natural for sequential or text-based logic.

The node-based paradigm also has an epistemological consequence: your *decisions* are made visible as *connections*. You can see the shape of your logic. This is different from writing code, where the structure of your reasoning is embedded in syntax. In TouchDesigner, the architecture *is* the code.

The defaults matter here (returning to Magnusson): the built-in operators in TouchDesigner assume certain things about color, resolution, framerate, and timing that reflect the tool's origins in VVVV and cinema-influenced real-time graphics. When you use those defaults without questioning them, you're making an implicit argument about what your work should look like.

### Max/MSP

Max/MSP is the older cousin of TouchDesigner — a node-based environment with deeper roots in algorithmic music composition and signal processing. Where TouchDesigner is GPU-native and optimized for visual output, Max is CPU-native and optimized for audio, MIDI, and data.

**Why both?** The choice between TouchDesigner and Max is not purely technical — it is partly a question of disciplinary genealogy. TouchDesigner comes from the VJ / visual performance world; Max comes from the electroacoustic music world. They carry different assumptions about what a "performance" is, what "real-time" means, and what relationship between software and body is natural.

Using both is an opportunity to feel those differences in your body as you work.

### Zoom H5

The Zoom H5 is a portable, mid-range field recorder. Four inputs (two XLR combo jacks, plus the built-in capsule capsule pair), 24-bit/96kHz recording, small enough to carry anywhere.

**Epistemic framing:** The H5 models the world as *microphone placements and headroom*. Unlike software recording, field recording asks you to solve problems in space and time before you can solve them in software. You can't EQ a bad room placement. The recorder forces decisions about *where you are* and *where the sound is* in a way that a software sampler does not.

The H5 is also a tool for practice-based research: documentation, listening, locating yourself in a sonic environment. Used as a research tool (not just a production tool), it is a way of attending to a space before you decide what to make there.

---

## The Inventory as Critical Practice

Here is the exercise this note is preparing you for:

**Do your own epistemic inventory.** Pick three tools you already use in your practice — any tools, not necessarily the ones listed here. For each one:

1. What does it amplify? (What becomes easy, visible, measurable?)
2. What does it reduce? (What disappears, becomes invisible, gets rounded off?)
3. What world does it assume exists? (What is the implicit model of activity, interaction, body, material that its design encodes?)
4. Who designed those assumptions, and for what context?

This exercise is the foundation of your ASN 2 (Critical Technical Journal). It begins this week.

---

## Key Terms

- **Signal chain** — the full sequence of transformations from physical world to digital output; each link is a reduction/amplification pair
- **OSC (Open Sound Control)** — a real-time messaging protocol that allows physical sensors and software to communicate; address-based, free-form namespace
- **Capacitive touch** — detection of electrical conductance changes; models touch as threshold-crossing events at discrete electrode points
- **Cooking system** — TouchDesigner's model of reactive computation; operators update only when inputs change
- **Default assumptions** — the inherited worldviews encoded in software's standard settings and built-in abstractions

---

## Setup Reference

For CircuitPython + MPR121 + OSC → TouchDesigner:

- [Adafruit CircuitPython documentation](https://docs.circuitpython.org/)
- [MPR121 CircuitPython library](https://github.com/adafruit/Adafruit_CircuitPython_MPR121)
- [TouchDesigner OSC In CHOP documentation](https://derivative.ca/UserGuide/OSC_In_CHOP)
- MicroOSC library for CircuitPython (see course repo)

---

---

## Practical Examples: This Exact Stack in Research Practice

The signal chain described above isn't hypothetical — it's the system running in ongoing research on physical-digital entanglement and Afrofuturist sonic sculpture. These examples show the same epistemic questions operating at research scale, which is also what the course is pointing toward.

### Example 1 — Don't Play in My Hair (Sonic Sculpture)

**The setup:** Capacitive touch electrodes embedded in a sculptural hair object. A QT Py RP2040 reads the MPR121, sends OSC messages over UDP to a Max/MSP patch, which triggers sound and visual responses based on which electrodes are touched and in what sequence.

**The epistemic problem:** The sensor models touch as 12 threshold events. But the sculpture is *about* touching Black hair — a gesture that carries enormous social, political, and intimate charge. The sensor cannot feel what that touch means. The gap between what the electrode reads (conductance shift at electrode 7) and what the audience experiences (touching something they were never supposed to touch) is not a technical failure. It's the piece.

**What this teaches:** The reduction is not a bug. Choosing what the system does and doesn't know is a design decision that carries epistemological and political weight. Agre: the computer is "about" the site in its design. This sculpture asks: what is a capacitive sensor *about* when the electrode is hair?

**The enabling constraint:** Because the MPR121 only reads 12 points, all gestural richness must be built at the audience and material level — through the choice of object, the installation context, the social meaning of the gesture. The hardware's reduction *enables* the cultural work.

---

### Example 2 — OSC Schema Design as Intermediation

**The setup:** When building the OSC namespace for the MPR121 → TouchDesigner pipeline, you have to decide what to *call* the data. Options:

- `/sensor/capacitive_threshold_event/channel/7` — too technical, reveals the measurement mechanism
- `/presence_of_hand/right/index` — too phenomenological, claims more than the sensor knows
- `/sensor/touch/7` — intermediate; legible to both the body and the system

**The lesson:** Every time you name a data stream, you are doing what Agre calls *intermediation* — choosing a level of abstraction that can bridge the phenomenological (what the interaction feels like) and the technical (what the hardware actually detects). Bad intermediation produces systems that are either uninterpretable (pure tech-speak) or dishonest (claiming the machine "knows" things it doesn't).

**For students:** Your first OSC schema is a philosophical document. What you choose to name your data channels reveals what you think the interaction *is*.

---

### Example 3 — Somax2 and Machine Agency

**The setup:** Somax2 (IRCAM) is an AI music improvisation system. It ingests musical input — typically MIDI or audio — models it as sequences of labeled events, and generates responsive output based on learned patterns. It "listens" and "responds," but it does so by reducing live performance to labeled categories it can reason about.

**The epistemic parallel:** Somax2 does at the level of musical grammar what the MPR121 does at the level of touch. It models the world reductively so that the machine can act within it. The quality of the musical interaction isn't determined by how "intelligent" the model is — it's determined by how well the reduction was designed relative to the human performer's practice.

**Agre's "computational improvisation" angle:** Agre mentioned a system operating as "an experiment in computational improvisation; rather than constructing a plan that it then executes wholesale." Somax2 is this literally. The question it raises: what does it mean to improvise *with* a system that knows your patterns but not your intentions?

**For students:** When you build a system that responds to sensor input — in TouchDesigner, Max, or anything else — you are building a Somax2. You are deciding what the system knows and doesn't know. That decision is compositional, not just technical.

---

### Example 4 — The Zoom H5 as Field Research Tool

**The setup:** Field recording before or alongside installation development. The H5 goes into a space — a barbershop, a kitchen, a corridor — and captures the sonic environment before any design decisions are made.

**The epistemic function:** The H5 forces you to solve problems in space and time *before* you can solve them in software. Bad mic placement can't be fixed with EQ. The recorder requires you to *attend* — to listen, to be in the space, to commit to a position. This is the embodied, pre-digital step of research-creation.

**Magnusson's hermeneutic → embodiment shift:** In the field, the H5 starts in an embodiment relation (you act through it, attending to what the mic hears). When you bring recordings back to the studio, it shifts to hermeneutic (you now interpret what was captured, what it means, what it missed). The shift is where research-creation happens: the difference between what the recorder heard and what you remember hearing is your first research question.

**For students:** What would it look like to do a listening session *in the space* where your project will live, before you touch any software? The H5 exercise (or any field listening practice) is the answer.

---

## Connected Threads

[[../../Threads/Physical-Digital Entanglement|Physical-Digital Entanglement]] &nbsp; [[../../Threads/Epistemic Tools|Epistemic Tools]] &nbsp; [[../../Threads/Enabling Constraints|Enabling Constraints]]
