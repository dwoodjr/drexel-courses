---
title: "Tool Audit — Template + Guide"
tags: [DIGM553, template, workshop]
---
# Tool Audit — Template + Guide

**Journal Entry 1 — Epistemic Tool Audit**
Part of [[../Assignments/ASN 2 — Critical Technical Journal|ASN 2: Critical Technical Journal]], Installment 1

---

## What This Is

The Epistemic Tool Audit (ETA) is a structured anatomy of your project's apparatus. You are going to be asking what your tools *think*, where *you* are inside the apparatus, and where the tools *break* (or impasse).

Building on Agre and Magnusson, this exercise rejects the idea of tools as neutral intermediaries. The hardware, software, and protocol that make up your signal chain encode worldviews, prescribe behaviors, and quietly marginalize alternative ways of knowing. This audit is one way in which we can that invisible visible.

**Core inquiry:** *What does my tool think? Where am I inside it? Where does it break?*

---

## Step 1 — Identify Your Loop

Before you audit anything, map your primary signal chain:

> `[Input Hardware]` → `[Protocol]` → `[Output Software]`

Document it physically (a photo) and virtually (a screenshot). This is the apparatus you're auditing, the entire whole loop.

---

## Step 2 — The Integrative Audit Matrix

Map your loop against four research lenses. For each cell, write **one analytic sentence**. Don't aim for completeness — aim for honesty. Blanks are data too.

| Research Domain | Hardware Site | Protocol Site | Software Site |
|---|---|---|---|
| **Sensory Worlding** | What does touching/holding/using this hardware *feel* like? What does it make visceral or signal through its form? | What's the sensory reality of this connection — the clunk of a cord, the noise of a port, the heat of a running device? | What does the GUI *want* you to notice? What aesthetic does the interface enforce before you've made a single decision? |
| **Material Memory** | What embedded physics or prior assumptions are locked into this device's capsules, thresholds, or form factor? | What historical ghosts live in this protocol? (OSC carries 80s hardware logic; MIDI carries keyboard-and-note-number logic.) | What style presets, hard-coded standards, or defaults encode a designer's choices you've absorbed without examining? |
| **Fugitive Speculation** | What is the "potential state" of this hardware — what is it capable of that it's never asked to do in your practice? | Where does the handshake break down? What jitter, latency, or data loss might carry *meaning* rather than just noise? | What latent behaviors or edge-case functions exist outside normal use? What does the tool do when you do something unexpected? |
| **Intimate Witnessing** | What errors, peaks, or failures have you had with this hardware? What did those moments reveal about what the tool assumes? | Where have you stayed with the trouble — kept the bad connection, the dropped packet, the lag — rather than immediately fixing it? | What crashes or error messages have you ignored? Read one as a "manifesto of the machine." What is it actually saying? |

---

## Step 3 — Worldview Statement

After completing the matrix, write **one paragraph** answering: *what does this apparatus — as a whole — believe the world is?*

- What behavior is it incentivizing?
- Who does it want you to be: a conductor, a coder, a consumer?
- What part of your artistic intent doesn't fit its parameters — what gets tossed to make a clean signal?

---

## Step 4 — Deeper Audit (optional, or for the written submission)

If the matrix opens something you want to follow further, these questions can extend the work:

**On worldview** (Magnusson): What behavior is the tool incentivizing? Does it want me to be a conductor, a coder, or a consumer?

**On marginalization** (Agre): What part of my intent doesn't "fit" into the parameters of this tool? What gets discarded in the service of a clean, functional signal?

**On entanglement** (Barad/Loveless): Where do my habits blend into the gain-knob or the slider? Since I cannot measure something without changing it; how is my touch *changing* the signal?

**On translation** (Magnusson): What is happening when "sound" becomes "math," when gesture becomes data, when touch becomes a threshold value? What dies in the handshake? IN other words, what gets lost/reduced?

---

## Synthesis: Where the Worldviews Meet

Once you've worked through the matrix, write a short synthesis (it could be a paragraph or a mapped diagram) on where the tools' worldviews converge, conflict, or compound:

- Where do they *align*? Do they share a cosmology?
- Where do they *conflict*? Do they pull in different directions?
- Where do they *compound*? Do they reinforce each other's reductions in ways that are easy to miss?
- What does the friction open up?

---

## Prompts (to unstick yourself)

- "The moment I realized this tool had a worldview was when..."
- "The default that surprised me most was..."
- "This tool was designed for someone who..."
- "When I try to do ___, I have to fight the tool because..."
- "These two tools agree that the world is... but I'm not sure I agree."
- "What escapes the signal chain entirely is..."

---

## Submission

Part of ASN 2, Installment 1. Due: beginning of Week 4.
Format is flexible: written, annotated diagram, voice memo, video log. Whatever lets you think. **However, the submitted document needs to be a PDF to Blackboard.**

---

## Quick-Reference Matrix

Use this to map both tools side by side at a glance. Fill in what you can.

| Dimension              | Software Tool: ___                  | Hardware Tool: ___                               |     |
| ---------------------- | ----------------------------------- | ------------------------------------------------ | --- |
| **Model of the world** | What cosmology does it assume?      | What physical phenomena does it register?        |     |
| **Amplifies**          | What becomes easy or fast?          | What aspects of reality does it make legible?    |     |
| **Reduces**            | What gets hidden or rounded off?    | What falls outside its range or resolution?      |     |
| **Designed for**       | Who was imagined as the user?       | What body/environment was assumed?               |     |
| **Wall**               | Where does it resist you?           | Where does it fail or break down?                |     |
| **Black box**          | What have you stopped questioning?  | What quirks do you work around without thinking? |     |
| **Ihde modality**      | Embodiment / Hermeneutic / Alterity | Embodiment / Hermeneutic / Alterity              |     |

### Example (filled in)

| Dimension              | TouchDesigner                                                                                                 | MPR121 Capacitive Sensor                                                                         |
| ---------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| **Model of the world** | A cooking network where data flows reactively between operators in real time                                  | 12 discrete threshold-crossing contact points with a capacitance value at each                   |
| **Amplifies**          | Real-time visual logic, GPU-native rendering, rapid signal routing                                            | Electrical conductance at designated points; works with skin, water, foil, conductive thread     |
| **Reduces**            | Sequential/procedural thinking; text-based logic; anything that needs to "wait"                               | Pressure, velocity, texture, gesture trajectory — anything that isn't threshold-crossing contact |
| **Designed for**       | VJ and live visual performance culture; assumes GPU access and spatial thinking                               | Breakout-board prototyping; keyboard/button replacement; discrete, intentional touch             |
| **Wall**               | When you need branching logic or conditionals, the node graphs tend to resists                                | When you need continuous gesture data or touch that varies in intensity                          |
| **Black box**          | Default 1280×720 resolution (free/non-commercial) and 60fps cook rate — assumptions about what "smooth" means | The “baseline” on startup;  invisible, not easily overridden                                     |
| **Ihde modality**      | Shifts hermeneutic → embodiment with fluency                                                                  | Primarily hermeneutic until the hardware recedes                                                 |

---

*See also: [[../Threads/Epistemic Tools|Epistemic Tools thread]] · [[../Threads/Entanglement|Entanglement thread]]*
