<h1 align="center">
  <br>
  <a href="https://github.com/Frankenstein-byte/FireFly"><img src="https://github.com/Frankenstein-byte/FireFly/blob/main/Hardware/image.png" width = "400" height="200" alt="FireFly"></a>
  <br>
  FireFly
  <br>
</h1>

<h4 align="center">Vulnerability Analysis and Testing of Wireless Networks through War-storming</h4>


UAS(Unmanned Aircraft System), also known as drones have recently been incorporated in various military operations due to its high technology features and inexpensive integrants. Initially, the purpose was achieved by wardriving which means data capturing was pulled off by road which limits range. While the core application is same, UAS can cover more wider area to capture data while being swift in moving from one target to another. UAS can be remotely operated with the help of visuals we get through sensors incorporated on drone. 

It also consist of features i.e. 5 Attack Vectors that can manipulate any network for defense operations

* De-authentication attack
* Packet injection (forging packets or spoofing packets)
* Beacon attack
* Captive portal (Rogue Access Point)
* Probe attack


## List of Hardware materials used :-

1. RaspberryPi-4 (Linux)
2. Panda PAU-06
3. TP-Link WN722N
4. Node MCU ESP-8266 (X2)
5. Android Phone (Wireless GPS)
6. PowerBank
7. Tagrus Multi USB-Port

<img src=https://github.com/Frankenstein-byte/FireFly/blob/main/Hardware/1.png width = "420" height="500" >

## Using Smartphone as your GPS 

Install the below mentioned app on your smartphone for accurate data to be received

<http://max.kellermann.name/projects/blue-nmea/>

## Checking incoming GPS data using NMEA

The phone will work as a simple web server that will send a data stream in plain text

```python
curl --http0.9 192.168.1.3:50000
```

If the data stream appears, then everything works.
On the phone, the status has changed to Connected.


## How to run gpsd to get GPS from your phone

In Debain, Kali Linux, Linux Mint, Ubuntu and their derivatives, the installation is done with the following command:

```python
sudo apt install gpsd gpsd-clients
gpsd -N tcp://192.168.1.3:50000
gpsd -N -D 10 tcp://192.168.1.3:50000

gpsmon
```


## Output

Drone path with heat map

<h4 align="center"><img src=https://github.com/Frankenstein-byte/FireFly/blob/main/Hardware/2.png width ="500" height="350"></h4>

Vendors(Users connected to AP) resolved after processing dataset

<h4 align="center"><img src=https://github.com/Frankenstein-byte/FireFly/blob/main/User%20Analysis/vendor%20stats.PNG width ="400" height="400"></h4>

Vendors(Access points) 

<h4 align="center"><img src=https://github.com/Frankenstein-byte/FireFly/blob/main/WiFi%20-%20Analysis/vendor2.png width ="400" height="400"></h4>


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

