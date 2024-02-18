# AgroBot

## Requirements:

1. The robot should navigate from one point to another point by avoiding obstacles.
2. The robot should work for at least half an hour of continuous use.
3. The robot should perform smooth maneuvers.

## Software Installations:

1. **Raspberry Pi Imager:** Used to flash the Raspberry OS into a memory card, which is further used to connect the Raspberry Pi with the laptop/desktop remotely.  
   Download Link: [Raspberry Pi Imager](https://www.raspberrypi.com/software/)
   
2. **MobaXterm:** Used to push the code from the laptop/device to Raspberry Pi remotely.  
   Download Link: [MobaXterm Installer Edition](https://mobaxterm.mobatek.net/download-home-edition.html)
   
3. **Python:** Required for writing code.  
   Download Link: [Python](https://www.python.org/downloads/)
   
4. **VS Code:** Integrated development environment used to write the code, which is then transferred via MobaXterm to Raspberry Pi.  
   Download Link: [VS Code](https://code.visualstudio.com/download)

## Getting Started with Raspberry Pi

To understand the Working of the Raspberry Pi, let us Build an Atomic Project on Controlling the Servo Motor with Raspberry Pi as Shown Below:

**Step 1:** Take the SD Card in Pendrive and connect it to CPU.
   
**Step 2:** Open Raspberry Pi Imager and perform the following selections:
   - Select "RASPBERRY PI 4" in Raspberry Pi Device.
   - Select "RASPBERRY PI OS (32-BIT)" in Operating System.
   - Select your injected pendrive in Storage.
   - Press `Shift` + `Ctrl` + `X` on your keyboard and do the following steps:
     - Change the hostname if you want; otherwise, keep it intact.
     - Set username and password.
     - Go to services and enable SSH and tick "Use password Authentication".
     - Go to Options and check "Eject Media when finished" and "Enable telemetry".
     - Click on Save and then click on Write. Wait until it writes and verifies.
   
**Step 3:** Open VS Code and create a file with the extension of `.py` and save the file.
