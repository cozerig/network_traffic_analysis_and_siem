# Network Traffic Analysis & Alerting System (tcpdump + Wazuh)

## Project Overview
This project captures network traffic using **tcpdump**, analyzes it with **Python (Scapy)**, and sends alerts to **Wazuh SIEM** when suspicious activity is detected. The system synchronizes time using **Chrony (NTP)** to ensure accurate log timestamps.

## 📌 Goals
- Capture network traffic in real-time.
- Identify anomalies (port scanning, excessive connections, unusual IPs).
- Send alerts to **Wazuh SIEM** for further investigation.
- Automate traffic analysis with cron.
- Ensure accurate timestamps with **Chrony (NTP)**.

## 🛠 Technologies Used
- **tcpdump** – Packet capture.
- **Python (Scapy)** – Traffic analysis.
- **Bash (cron)** – Automation.
- **Wazuh SIEM** – Log collection and alerting.
- **Chrony (NTP)** - Time synchronization


