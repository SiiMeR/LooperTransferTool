# LooperTransferTool

This tool was created to help me easily transfer files between the Boss RC-3 Looper and my PC. 

## Looper memory

The Boss RC-3 Looper comes with 99 memory slots that the user can use for storing the loops they make and for adding new loops/sounds via a USB connection. The looper has its own internal filesystem that represents each memory slot with a subfolder in the ROLAND/WAVE folder. The folders are named 001_1 through 099_1 and cannot be renamed. Each slot contains exactly one .wav file that has no naming restrictions. 

The .wav file must have the following format:
* Data format: WAV
* Bit rate: 16-bit linear, stereo
* Sampling frequency: 44.1 kHz

## The problem I am trying to solve

How I use the looper is for learning new songs part by part. I slice the songs into 10-15 pieces and add them one by one to each folder in continuously. This is really tedious and I would like to partly automate this process by letting a script take care of copying the .wav files to the looper with the correct structure. 

The other problem is managing already filled memory slots. I'd like to empty out a range of slots at once and easily list what is in them.
