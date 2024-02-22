# AgroBot

## Requirements:

1. The robot should navigate from one point to another while avoiding obstacles.
2. The robot should operate continuously for at least half an hour.
3. The robot should execute smooth maneuvers.

## Software Installations:

1. **Raspberry Pi Imager:** Used to flash the Raspberry OS onto a memory card, which is then used to connect the Raspberry Pi to a laptop/desktop remotely.
   Download Link: [Raspberry Pi Imager](https://www.raspberrypi.com/software/)
   
2. **MobaXterm:** Used to push code from the laptop/device to the Raspberry Pi remotely.
   Download Link: [MobaXterm Installer Edition](https://mobaxterm.mobatek.net/download-home-edition.html)
   
3. **Python:** Required for writing code.
   Download Link: [Python](https://www.python.org/downloads/)
   
4. **VS Code:** Integrated development environment used to write code, which is then transferred via MobaXterm to the Raspberry Pi.
   Download Link: [VS Code](https://code.visualstudio.com/download)

## Getting Started with Raspberry Pi

To understand how Raspberry Pi works, let's build a simple project to control a servo motor with Raspberry Pi as demo shown below :

![Untitled video - Made with Clipchamp](https://github.com/MdSadiqMd/AgroBot/assets/104257708/231edade-c5b3-481d-a082-e93b0f29bc51)

**Step 1:** Insert the SD Card into the Pendrive and connect it to the CPU.

   **Step 2:** Open Raspberry Pi Imager and follow these steps:
   - Select "RASPBERRY PI 4" as the Raspberry Pi Device.
   - Choose "RASPBERRY PI OS (32-BIT)" as the Operating System.
   - Select your inserted pendrive as the Storage.
   - Press `Shift` + `Ctrl` + `X` on your keyboard and perform the following:
     - Optionally, change the hostname.
     - Set a username and password; avoid using College Wifi as it may have username hurdles, use your mobile hotspot wifi instead. Ensure that the laptop and Raspberry Pi are connected to the same Wifi.
     - Enable SSH and select "Use password Authentication" under services.
     - Check "Eject Media when finished" and "Enable telemetry" under Options.
     - Click on Save and then Write. Wait until it writes and verifies.
     - Close the Raspberry Pi Imager, remove the Memory Card from the Pendrive, and insert it into the Raspberry Pi (Hardware Board).

   **Step 3:** Open VS Code or any Code Editor, create a file with the extension `.py`, save the file, and close the Editor.

   **Step 4:** Open the Settings of your Laptop, go to Settings > Network & Internet > Mobile Hotspot, turn on the Mobile Hotspot of Laptop, and set the Properties to the username and password you provided in Raspberry Pi Imager. Copy the IP Address displayed in the connected devices section. This step ensures that your laptop and Raspberry Pi are connected to the same wifi.

![network](https://github.com/MdSadiqMd/AgroBot/assets/104257708/3f4086c2-6cba-46c8-8d5c-ed6dd45c4ffe)

   **Step 5:** Now open MobaXterm, click on `Session` in the top right corner, then click on `SSH`. Paste the IP Address copied earlier into the Remote host input, and provide the username you set in Raspberry Pi Imager. Click on "ok" and "accept".

![Screenshot (732)](https://github.com/MdSadiqMd/AgroBot/assets/104257708/ac9960cf-d08a-409c-9fa6-c494212cb776)

   **Step 6:** Your laptop and the Raspberry Pi are now connected. To control the Raspberry Pi with your laptop, push the code from your laptop to the Raspberry Pi. As they are connected to the same internet, you don't need any manual connection. Simply transfer the code via the internet to make the Raspberry Pi work. 
   - To do this, click on Upload file, select the Python file you wrote and open it

![Screenshot (734)](https://github.com/MdSadiqMd/AgroBot/assets/104257708/b79b6fec-6951-40ec-b6c2-26a5cf9e2de1)

   - Make sure that the opened file is visible in the left sidebar and run the file in the terminal using the command:

```bash
python3 filename.py
````

![Screenshot (739)](https://github.com/MdSadiqMd/AgroBot/assets/104257708/a29854ea-9153-4534-b522-bdd167712f55)

   - To stop the code execution or the hardware operation, press `Ctrl` + `C` in the terminal. This action will terminate the code execution and stop the Raspberry Pi.

