# bananapi-radiation-monitor

**This is inspired by https://github.com/chrisys/background-radiation-monitor raspberry PI project.

A simple Python application to measure and record background radiation in your area. Radiation is detected with a cheaply available board, and connected to a Banana Pi M2 ZERO SBC (BPI-M2) to provide InfluxDB for datalogging and Grafana for pretty charts. Measured data are stored localy to BPI-M2.

![grafana.jpg](https://github.com/lubomirkarlik/bananapi-radiation-monitor/blob/84982dac9634d71a96588a1a0aa980fe15ad04c2/grafana.jpg)


## Hardware requirements

* A Banana Pi M2 ZERO SBC (BPI-M2) (any model should be suitable, I have used one of simplest BPI-M2 ZERO)
* An 8GB (or larger) SD card 
* A power supply (PSU)
* A radiation detector [Banggood](https://www.banggood.com/sk/DIY-Geiger-Counter-Kit-Open-Source-Miller-Tube-GM-Tube-Module-Radiation-Parts-p-1937604.html?rmmds=myorder&cur_warehouse=CN) , as kit for more skils users, or on  [AliExpress](https://www.aliexpress.com/item/32884861168.html?spm=a2g0o.productlist.0.0.5faf6aa9OuQXsc)
* Some [Dupont cables/jumper jerky](https://shop.pimoroni.com/products/jumper-jerky?variant=348491271) (you’ll need 3 female-female cables)


## Hardware connection

There are 3 connections we need to make from the radiation detector board to the BPI-M2 ZERO. They are +5V and Ground (GND) for power, and the output pulse line to detect the count. Note that this is called `VIN` which can be a bit confusing as this usually means ‘voltage input’ or something similar, but on this board, it’s the output.



In this configuration you only need to provide 5 volt power to one of the two boards; if you’re powering the Banana Pi with a standard micro-USB power supply, that will power the detector board via the connections we’ve just made, as well.

## Software setup

You have two possibilities. First one (preffered) is download prepared image with presetted values. Or install some debian based image to Your BPI-M2 zero , install needed software components and run my python application. First option is easyest way.
