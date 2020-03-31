# LightNet
## Requirements
* Linux: 
    * `sudo apt install pigpiod python3 python3-flask python3-gpiozero python3-paho-mqtt`
    * `sudo systemctl start pigpiod`

## Run WEB
### Start Server
* `python3 api.py`
* Open `http://0.0.0.0:5000` on same device

### Access on Local Network
* Find the IP of the device running LightNet
    * Terminal (Linux/Mac): `ifconfig`
    * Your WLAN access point/router
* Open `http://[IP]:5000` on devices in local network

## Run MQTT
* Configure in `lgtt.py`
* `python3 lgtt.py`

## Install Linux Autostart Service
* Open `lightnet.service` and change `WorkingDirectory` in relation to your working directory
* Copy service to service directory: `sudo cp lightnet.service /etc/systemd/system/lightnet.service`
* Enable service to run on boot: `sudo systemctl enable lightnet.service`

## Manual Service Usage
* Start: `sudo service lightnet start`
* Stop: `sudo service lightnet stop`