---
title: "Music + Audio Production in Logic Pro X (Udemy) Notes"
tags: music notes
---

## Intro
I like taking notes in markdown and this website is an easy way to render markdown :)

## Audio Production for Beginners

### Sample Rate and Bit Depth
* Bit depth is how many 'bits' the computer uses to record the audio. Higher the bit depth means larger dynamic range. Lower bit depth means more noise.
* Sample rate is how many times your computer takes a snapshot of the audio. High sample rate is important if you need to slow down music.
* Here is a good summary: [link](https://www.musicianonamission.com/daw-setup-bit-depth-sample-rate-buffer-size/)

### Acoustics and the Frequency Spectrum
* [eq match](https://trainer.thetamusic.com/en/content/eq-match)
* [frequency quiz](https://www.puremix.net/ear-training.html)
* Hard surfaces reflect so vocals should be recorded in rooms with soft surfaces.

### Decibels, Distortion and Volume
* dBSPL. Used to measure the sound levels in the environment. 120 dBSPL is the threshold of discomfort
* dBVU. Used to measure analogue equipment. 0 dBVU is the sweet spot, occasionally going to +3 dBVU.
* dBFS. Is used in digital equipment. 0 DBFS is where clipping occurs. STAY AWAY.
* **-18 dBFS = 0dBVU**

### Basic Mixing Tools
* *Main job is just to balance the volume.*
* Panning (placing sounds in the stereo field), gives it a sense of space. However, be careful that many things are mono (like phone and laptop speakers) so do this at the end.
* EQ. Allow you to adust the VOLUME of different frequencies.
* Compression. Lowers dynamic range in a track. "Compress the loud parts and then bring up overall volume"

### Glossary
* *Amplifier*: A device which increases the amplitude of a signal.
* *Balanced* Audio: A type of audio signal which uses two inverted voltages as a way to prevent unwanted noise being picked up by cables.
* *Bus*: The pathway along which an electrical signal flows. For example, the output of a sound mixer is referred to as the master stereo bus.
* *Channel*: Similar to a bus, a pathway through an audio device. For example, sound mixers have multiple input channels.
* *Compression*: A method of "evening out" the dynamic range of a signal.
* *DAW*: Digital Audio Workstation (like Logic, Pro Tools, Studio one etc.)
* *Decibel* (dB): Logarithmic measurement of signal strength.
* *Equalization*: The process of adjusting various audio frequencies to correct or enhance the sound.
* *Fade*: A transition to or from silence.
* *Frequency* Response: The sensitivity of an audio device to various frequencies, i.e. the amount each frequency is boosted, attenuated or reproduced.
* *Gain*: The amplification level of an audio signal.
* *Hertz*: Unit of frequency, cycles per second.
* *Headroom*: In a cable or audio device, the difference between the maximum level of the signal being carried and the maximum level the device is capable of carrying without distortion. Headroom is safety room.
* *MIDI*: Musical Instrument Digital Interface. A standard of communication between musical instruments, controllers and computers.
* *Mixer*: A device which accepts two or more audio inputs and provides one or more audio outputs.
* *Peak*: The highest level of strength of an audio signal. Often refers to an unacceptably high level, where the signal begins distorting.
* *Phantom* Power: A DC current which is sent through audio cables to provide power for devices such as microphones.
* *Reverb*: Reverberation, the effect of sound waves bouncing off walls and other objects.
* *Sample*: In digital audio recording, thousands of individual "samples" are recorded every second. Added together these make up the digital audio signal.
* *Stereo*: Audio which is made up of two channels — left and right.
* *Wavelength*: The length of a wave, measured from any point on a wave to the corresponding point on the next phase of the wave.
* *XLR*: A lockable connector, available with various numbers of pins. The most common XLR in audio work is the 3-pin XLR. Most microphones use XLR.

### Navigation
* Look for the blue square: this indicates the key area. Tab to toggle.
* Option-K to look a the keyboard shortcuts.
* , . to move forward and back.
* Ctrl arrow keys to zoom horizontally and vertically.
* Scroll sideways with shift.
* U to make the cycle match the selected track.
* Hold Option to drag and copy regions.

## Recording Basics
* In the setting for recording use a small buffer size for low latency. Use high buffer size for mixing.
* Organize with colors :)
* Record near -18 peaking no higher than 6 (this yields low distortion)
* Check monitor settings

### Techniques
* Experiment with mic positions (one of the biggest factors in the tone!)
    * Closer: bassy
    * Farther: more room / less bass
* Find the sound first (don't fix it later)
* Consider the instrument in the context of the song (is it a main instrument? or providing support do we want it to be prominent?).
* Shift-Space goes back to the start of the region.
* Takes
    * To do another take just record over the top of another region
    * Or do use cycle mode (just record with the cycle on!)
* Punch in
    * Only re-record parts!
    * Auto punch
        * Record toggle in settings.

## Editing Basics
* Use the tools
    * Use command to use the secondary tool
* Hold alt and drag to zoom into sections
* Use cross fades to suppress pops
    * The comping thing will automatically generate cross fades for you.
* e to show the edit window.
* Anchor points can be convenient for aligning tracks.
* X and click to analyze flex so you can move the transient.
* Grove track
    * Right a channel and set the grove track
    * Tick another channel to make it conform to the grove track

## Software Instruments
* The library is really good. Explore using the musical typing editor.
* ES2 synth
    * This thing is really complicated. Start with a preset.
* Sampler
    * Take some audio and create a sample from it!
    * You can then extend the range and play the sample at different pitches.
