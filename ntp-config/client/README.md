# NTP Client Configuration
## Installation
```bash
sudo apt update && sudo apt install chrony -y
```
## Configuration
**Copy from chrony.conf then paste and edit in your chrony.conf**
```bash
sudo nano /etc/chrony/chrony.conf
```
## Restart
```bash
sytemctl restart chrony
```
## Check
```bash
chronyc sources -v
timedatectl status
```
