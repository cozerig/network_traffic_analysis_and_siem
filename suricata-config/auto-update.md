# Suricata Auto-Update

This folder contains a script and setup instructions to automatically update Suricata rules daily and restart the Suricata service.

## Setup Instructions
### Edit the cron jobs:
```bash
crontab -e
```
### Add the following line to update Suricata rules every day at 3:00 AM:
```bash
0 3 * * * sudo suricata-update && sudo systemctl restart suricata
```
### Check if the cron job is set up correctly:
```bash
crontab -l
```
### Verify Execution
To check if the cron job is running, view logs:
```bash
sudo grep CRON /var/log/syslog
```
If successful, you will see an entry like:
```bash
Mar 31 03:00:01 hostname CRON[12345]: (user) CMD (sudo suricata-update && sudo systemctl restart suricata)
```
To check if Suricata restarted properly:
```bash
sudo journalctl -u suricata --since "3 hours ago"
```
### Ensure cron Service is Running
Check if cron is active:
```bash
sudo systemctl status cron
```
If it’s not running, start and enable it:
```bash
sudo systemctl start cron
sudo systemctl enable cron
```
