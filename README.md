# x728v2.2
Scripts for X728 V2.1 & V2.2 shield

Documentation: http://www.suptronics.com/miniPCkits/x728_v2.2-software.html

tldr;
`sudo raspi-config` 
enable i2c

```bash
sudo apt-update
sudo apt install -y python3-smbus i2c-tools

sudo bash pld.sh
sudo cp plsd.service /etc/systemd/system/
sudo systemctl enable plsd.service

sudo reboot
```
