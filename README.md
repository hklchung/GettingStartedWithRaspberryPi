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
  A comprehensive guide on setting up your Raspberry Pi model 4B+.
    <br />
    <a href="https://github.com/hklchung/TravelPlanner"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/hklchung/TravelPlanner/issues">Report Error</a>
    ·
    <a href="https://github.com/hklchung/TravelPlanner/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About Raspberry Pi](#about-raspberry-pi)
* [Getting Started](#getting-started)
  * [Parts](#parts)
  * [Booting it up](#booting-it-up)
* [Usage](#usage)
* [Contributing](#contributing)
* [Contact](#contact)
* [Known Issues](#known-issues)

<!-- ABOUT RASPBERRY PI -->

## About the Project
---

<!-- GETTING STARTED -->

## Getting Started
---

<!-- PARTS -->

### Parts
The easiest way to get started is to purchase a Raspberry Pi starter kit and these can be found on Amazon, eBay, or your local electronics store. However, these typically come with parts that are not needed for regular usage or that you may already have some of these parts and you do not want to purchase them again. Therefore below is a list of required components which you can indivdually source via the most channel of your own choosing. 

#### Essential
- Raspberry Pi 4 Model B 2GB/4GB 
  - 4GB is preferred as 2GB can be a bit slow if you want to control your Raspberry Pi via the GUI
- Official Raspberry Pi 4 Power Supply
- HDMI cable
- MicroSD Card with NOOBS for all Raspberry Pi Boards <a href="https://core-electronics.com.au/32gb-microsd-card-with-noobs-for-all-raspberry-pi-boards.html"><strong>(example)</strong></a>
  - preferrably at least 16GB
  - get the ones with NOOBS pre-loaded, these allow you to directly boot up your machine without further fuss when you do it for the first time

#### Optional
- An acrylic case compatible with Raspberry Pi 4B+ <a href="https://core-electronics.com.au/transparent-acrylic-case-with-cooling-fan-for-raspberry-pi-b-2b-3b.html?utm_source=google_shopping&gclid=Cj0KCQjw6_vzBRCIARIsAOs54z6sotg_ru8JCn2dvZ5tL83YbP5N_2ghLr-XbPhGCqAFV2PvPNbyJqgaAgOaEALw_wcB"><strong>(example)</strong></a>
- A cooling fan <a href="https://core-electronics.com.au/miniature-5v-cooling-fan-with-molex-picoblade-connector.html"><strong>(example)</strong></a>
- Heat sink <a href="https://core-electronics.com.au/3pc-heatsink-kit-for-raspberry-pi-4.html"><strong>(example)</strong></a>

#### For Developers
- Female/Female jumper wires
- Regular jumper wires
- Resistor 10k, 1K, 330 Ohm 1/4 Watt PTH
- Breadboard
- Push buttons, potentiometers, photoresistors, LED 5mm (and whatever sensors/actuators you think you will need)

<!-- BOOTING IT UP -->

### Booting it up
---

<!-- USAGE -->

## Usage
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

### Remote Access to Raspberry Pi via SSH (text interface)
1. Boot up Raspberry Pi
2. Connect the Raspberry Pi to your WiFi network
3. Open Termianl and run the below
```sh
sudo raspi-config
```
4. A window will pop up, go to Interfacing Options -> SSH -> enable SSH
5. Download PuTTY from <a href="https://www.putty.org/"><strong>here</strong></a>
6. Install PuTTY under standard configurations
7. While PuTTY is being installed, check the network IP of your WiFi by following <a href="https://nordvpn.com/blog/find-router-ip-address/"><strong>this guide</strong></a>
8. Once PuTTY has installed successfully, open PuTTY, paste your WiFi IP into the Host Name box and click Open
9. Enter your username (pi) and password
10. You should now be able to remote access your Raspberry Pi via SSH
  
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
