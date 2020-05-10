[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

<br />
<p align="center">
  <a href="https://github.com/hklchung/GettingStartedWithRaspberryPi">
    <img src="https://upload.wikimedia.org/wikipedia/commons/f/f1/Raspberry_Pi_4_Model_B_-_Side.jpg" height="100">
  </a>

  <h3 align="center">Getting Started with Raspberry Pi</h3>

  </p>
</p>

<p align="center">
  A comprehensive guide on setting up your Raspberry Pi model 4B+ for beginners.
    <br />
    <a href="https://github.com/hklchung/GettingStartedWithRaspberryPi"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/hklchung/GettingStartedWithRaspberryPi/issues">Report Error</a>
    ·
    <a href="https://github.com/hklchung/GettingStartedWithRaspberryPi/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About Raspberry Pi](#about-raspberry-pi)
* [Getting Started](#getting-started)
  * [Parts](#parts)
  * [Booting it up](#booting-it-up)
* [Usage](#usage)
  * [Install Software](#install-software)
  * [Remote Access to Raspberry Pi GUI](#remote-access-to-raspberry-pi-gui)
  * [Remote Access to Raspberry Pi via SSH](#remote-access-to-raspberry-pi-via-ssh)
  * [Building Your First Prototype](#building-your-first-prototype)
* [Contributing](#contributing)
* [Contact](#contact)
* [Known Issues](#known-issues)

<!-- ABOUT RASPBERRY PI -->

## About Raspberry Pi
Raspberry Pi is a small single-board computer that is commonly used for rapid prototyping, IoT smart home devices and even as a regular computer. The Raspberry Pi model 4B+ was released in 2019 and is the latest, most advanced model as of writing of this guide.

Raspberry Pi model 4B+ comes with a 1.5 GHz 64-bit quad core ARM Cortex-A72 processor, on-board 802.11ac Wi-Fi, Bluetooth 5.0, full gigabit Ethernet, two USB 2.0 ports, two USB 3.0 ports, and dual-monitor support via a pair of micro HDMI (HDMI Type D) ports for up to 4K resolution . The Pi 4 is also powered via a USB-C port, enabling additional power to be provided to downstream peripherals, when used with an appropriate PSU. A labelled diagram of the described model is available below. Please note that the MicroSD card insertion slot is on the underside of the board.
<br />
<p align="center">
  <a href="https://github.com/hklchung/GettingStartedWithRaspberryPi">
    <img src="https://github.com/hklchung/GettingStartedWithRaspberryPi/blob/master/Image/raspberrypi4b.PNG?raw=true" height="400">
    </a>
  </p>
</p>

Raspberry Pi supports both text-based interface (console) and a graphical user interface (GUI) which makes it easy for users to navigate and control functionalities in the system. User can also choose the Operating System (OS) on the Raspberry Pi, although Raspbian is strongly recommended for new users.

There are 40 GPIO pins on the Raspberry Pi model 4B+ with some doubling as multi-function pins that support UART, I2C and SPI communication protocols. You do not need to worry about the pins if you are simply using the board as a regular computer.

<!-- GETTING STARTED -->

## Getting Started

<!-- PARTS -->

### Parts
The easiest way to get started is to purchase a Raspberry Pi starter kit and these can be found on Amazon, eBay, or your local electronics store. However, these typically come with parts that are not needed for regular usage or that you may already have some of these parts and you do not want to purchase them again. Therefore below is a list of required components which you can indivdually source via the most convenient channel of your own choosing. 

#### Essential
- Raspberry Pi 4 Model B 2GB/4GB 
  - 4GB is preferred as 2GB can be a bit slow if you want to control your Raspberry Pi via the GUI
- Official Raspberry Pi 4 Power Supply
- HDMI cable
- MicroSD Card with NOOBS for all Raspberry Pi Boards <a href="https://core-electronics.com.au/32gb-microsd-card-with-noobs-for-all-raspberry-pi-boards.html"><strong>(example)</strong></a>
  - preferrably at least 16GB
  - get the ones with NOOBS pre-loaded, these allow you to directly boot up your machine without further fuss when you do it for the first time
- Mouse and keyboard
  - you cannot control the board if you do not have a mouse and a keyboard
  - ones with cable connection would be preferable

#### Optional
- An acrylic case compatible with Raspberry Pi 4B+ <a href="https://core-electronics.com.au/transparent-acrylic-case-with-cooling-fan-for-raspberry-pi-b-2b-3b.html?utm_source=google_shopping&gclid=Cj0KCQjw6_vzBRCIARIsAOs54z6sotg_ru8JCn2dvZ5tL83YbP5N_2ghLr-XbPhGCqAFV2PvPNbyJqgaAgOaEALw_wcB"><strong>(example)</strong></a>
- A cooling fan <a href="https://core-electronics.com.au/miniature-5v-cooling-fan-with-molex-picoblade-connector.html"><strong>(example)</strong></a>
- Heat sink <a href="https://core-electronics.com.au/3pc-heatsink-kit-for-raspberry-pi-4.html"><strong>(example)</strong></a>

#### For Developers
- Female/Female jumper wires
- Regular jumper wires
- Resistor 10k, 1K, 330 Ohm 1/4 Watt PTH
- Breadboard
- Extension board + colour ribbon cable <a href="https://www.ebay.com.au/itm/Sintron-40Pin-GPIO-Extension-Board-Color-Ribbon-Cable-for-Raspberry-Pi4-Model-B/151616956126?ssPageName=STRK%3AMEBIDX%3AIT&_trksid=p2060353.m2749.l2649"><strong>(example)</strong></a>
- Push buttons, potentiometers, photoresistors, LED 5mm (and whatever sensors/actuators you think you will need)

<!-- BOOTING IT UP -->

### Booting it up
Now assuming you have purchased the aforementioned components, you can go ahead and follow the below steps to boot up your Raspberry Pi for the first time!
1. Do not plug in your power!
2. Plug in your mouse and keyboard into the USB2.0 ports (black)
3. Plug in your HDMI cable to a TV or monitor, connect it to the HDMI0 port
4. Slot in your MicroSD card with NOOBS into the MicroSD card insertion slot
5. Ensure all the above have been connected to the board tightly and securely, then plug in the power
6. You should be able to see rainbow gradient background on your screen followed by prompt asking for username and password
  - you may have to wait up to 1-2 minutes to see something on the screen
  - if you do not see anything after 3 minutes, this is likely due to poor connection of the HDMI cable
  - there are known issues with video outputs from the Raspberry Pi, see the guide <a href="https://howtoraspberrypi.com/raspberry-pi-hdmi-not-working/"><strong>here</strong></a> for solution
7. Enter username "pi" and password "raspberry" and go through the OS update and installation process. This may take up to 20 minutes depending on internet speed.
8. Once the Raspberry Pi has been updated, your set up is complete
9. It is important to note that you should always shutdown your Raspberry Pi before removing power supply as this may corrupt your MicroSD card. To shutdown, simply select shutdown from the start up menu or enter the below code in the terminal.
```sh
sudo shutdown now
```

<!-- USAGE -->

## Usage
<!-- INSTALL SOFTWARE -->
### Install Software
You can use the Raspberry Pi as you would with any other computer. To download softwares onto your Raspberry Pi, open up Terminal from the start up menu and run the following command. (Scrot is a screen capturing application)
```sh
sudo apt-get install scrot
```
To see a list of softwares installed, run:
```sh
apt list --installed
```

<!-- REMOTE ACCESS TO RASPBERRY PI GUI -->
### Remote Access to Raspberry Pi GUI
1. Boot up Raspberry Pi
2. Connect the Raspberry Pi to your WiFi network
3. Open Termianl and run the below
```sh
sudo raspi-config
```
4. A window will pop up, go to Interfacing Options -> VNC -> enable VNC
5. Download VNCViewer from <a href="https://www.realvnc.com/en/connect/download/viewer/"><strong>here</strong></a>
6. Install VNC under standard configurations
7. While VNC is being installed, check the network IP of your WiFi by following <a href="https://nordvpn.com/blog/find-router-ip-address/"><strong>this guide</strong></a>
8. Once VNCViewer has installed successfully, open VNCViewer and paste your WiFi IP into the search bar
9. You should now be able to remote access your Raspberry Pi GUI

<!-- REMOTE ACCESS TO RASPBERRY PI VIA SSH -->
### Remote Access to Raspberry Pi via SSH
1. Boot up Raspberry Pi
2. Connect the Raspberry Pi to your WiFi network
3. Open Termianl and run the below
```sh
sudo raspi-config
```
4. A window will pop up, go to Interfacing Options -> SSH -> enable SSH
5. Download PuTTY from <a href="https://www.putty.org/"><strong>here</strong></a>
6. Install PuTTY under standard configurations
7. While PuTTY is being installed, check the network IP of your WiFi by following <a href="https://nordvpn.com/blog/find-router-ip-address/"><strong>this guide</strong></a> or run the command below if you have a screen and keyboard connected to your Raspberry Pi
```sh
ifconfig
```
* The number under wlan0
8. Once PuTTY has installed successfully, open PuTTY, paste your WiFi IP into the Host Name box and click Open
9. Enter your username (pi) and password
10. You should now be able to remote access your Raspberry Pi via SSH

<!-- BUILDING YOUR FIRST PROTOTYPE -->
### Building Your First Prototype
<i>Note: The below steps assume you have set up remote access to your RPi</i>
1. Boot up Raspberry Pi
2. SSH into your RPi via PuTTY
3. Install Cyberduck on your <b>PC</b> and use it to transfer <a href="https://github.com/hklchung/GettingStartedWithRaspberryPi/blob/master/Python/PWM.py"><strong>PWM.py</strong></a> from the /Python/ folder into your RPi. To transfer file, click on <i>Open Connection</i> -> select SFTP (SSH File Transfer Protocol) -> enter server, port, username and password details as per PuTTY login into RPi, then transfer the selected file.
4. Set up your pins and wires as per below
* GPIO018 (pin 12) <=====> one regular jumper wire <=====> F1 on breadboard 
* G1 on breadboard <=====> LED anode (+)/LED cathode (-) <=====> F4 on breadboard
* G4 on breadboard <=====> 330 Ohm resistor <=====> G10 on breadboard
* H10 on breadboard <=====> on regular jumper wire <=====> GND (pin 6)
5. Go back to PuTTY and execute the following command from the directory where the <b>PWM.py</b> file is located.
```sh
python3 PWM.py
```
6. You should be able to see brightness on the LED changes continuously. To end the program, simply press control + c on the PuTTY interface.

This repo also provides 2 other python scripts that have been tested to function correctly given the right set up on your hardware.
* BlinkLED.py allows user to control blinking of an LED through a pushbutton
* LiveServer.py allows user to set the RPi as a server and returns the message "Got a request!" upon receving any commands from a client.

To create and edit a Python script directly in RPi, you can:
1. Install vim (this helps your visualise your Python commands)
```sh
sudo apt-get install vim
```
2. Create your Python script
```sh
touch test.py
```
3. Edit your Python script
```sh
vi test.py
```
4. Run your Python script
```sh
python3 test.py
```

Raspberry Pi 4B+ does not make it easy for the user to distinguish the pins from one another. Therefore it is highly recommended to purchase an extension board to assist with wiring. A side benefit of the extension board is that you will then not require any female jumper wires to connect your RPi. Nonetheless, below is a labelled layout of the pins on your RPi 4B+.

<p align="center">
    <img src="https://github.com/hklchung/GettingStartedWithRaspberryPi/blob/master/Image/raspberrypi4b_gpio.jpg?raw=true" height="400">
  </p>
</p>
  
<!-- CONTRIBUTING -->

## Contributing
I welcome anyone to contribute to this guide so if you are interested, feel free to make updates.
Alternatively, if you are following this guide and found an error or missing information to assist your setup, please provide your feedback by clicking on the Report Error or Request Feature buttons at the top of the page.

<!-- CONTACT -->

## Contact
* [Leslie Chung](https://github.com/hklchung)

<!-- KNOWN ISSUES -->

## Known Issues
---

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/hklchung/GettingStartedWithRaspberryPi.svg?style=flat-square
[contributors-url]: https://github.com/hklchung/GettingStartedWithRaspberryPi/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/hklchung/GettingStartedWithRaspberryPi.svg?style=flat-square
[forks-url]: https://github.com/hklchung/GettingStartedWithRaspberryPi/network/members
[stars-shield]: https://img.shields.io/github/stars/hklchung/GettingStartedWithRaspberryPi.svg?style=flat-square
[stars-url]: https://github.com/hklchung/GettingStartedWithRaspberryPi/stargazers
[issues-shield]: https://img.shields.io/github/issues/hklchung/GettingStartedWithRaspberryPi.svg?style=flat-square
[issues-url]: https://github.com/hklchung/GettingStartedWithRaspberryPi/issues
