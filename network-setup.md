# Network Configuration in VMware Workstation

## Setup in Virtual Network Editor
- **VMnet2(Host-only) for isolated traffic monitoring.**
- **VMnet8(NAT) for internet access.**

## Connection Scheme
| Machine       | Role         | Network Adapters  | IP Address     | Notes |
|--------------|-------------|------------|----------------|---------------|
| Wazuh Server | SIEM        | VMnet8, VMnet2      | DHCP, Static     | Collects, analyzes, and stores logs. Hosts **Wazuh Manager**, **Elasticsearch**, **Kibana**.|
| Wazuh Agent  | Traffic Analysis | VMnet8, VMnet2  |  DHCP, Static   | Runs **tcpdump** to capture traffic, analyzes packets using **Python (Scapy)**, and sends alerts to **Wazuh Server**.|
| Client       | Traffic Generator | VMnet8, VMnet2 |  DHCP, Static   | Generates normal network traffic.|
| Attacker     | Red Team    | VMnet8, VMnet2      |  DHCP, Static    | Simulates attacks|

## Commands Used for Static IP Configuration
```bash
nmcli device status
nmcli con add type ethernet ifname <interface-id> con-name <connection-name> ipv4.method manual ipv4.addresses <ip/netmask>
ping -c 5 <ip>
