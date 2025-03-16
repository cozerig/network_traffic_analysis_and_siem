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

## 📂 Project Structure
- 📦 network-traffic-monitor
- ┣ 📂 scripts  *(Contains scripts for traffic analysis and alerting)*
- ┃ ┣ analyze_traffic.py  *(Parses and analyzes network traffic captured by tcpdump)*
- ┃ ┗ send_alerts.py  *(Sends alerts to Wazuh SIEM based on detected anomalies)*
-  ┣ 📂 logs  *(Stores captured network traffic logs)*
-  ┃ ┗ network_traffic.pcap  *(Packet capture file generated by tcpdump)*
-  ┣ 📂 config   *(Configuration files for different components)*
-  ┃ ┣ wazuh_agent.conf  *(Wazuh Agent configuration for log forwarding)*
- ┗ wazuh_server.conf  *(Wazuh Server configuration for log collection and processing)*
- ┣ .gitignore
- ┣ README.md
- ┣ requirements.txt  *(List of Python dependencies required for the project)*
- ┗ crontab.txt  *(Cron job schedule for automating traffic analysis and alerting tasks)*
