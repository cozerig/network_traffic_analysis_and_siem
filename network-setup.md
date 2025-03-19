# Network Configuration in VMware Workstation

## Setup in Virtual Network Editor
- **VMnet2(Host-only) for isolated traffic monitoring.**
- **VMnet8(NAT) for internet access.**

## Connection Scheme
| Machine       | Role         | Network Adapters  | IP Address     | 
|--------------|-------------|------------|----------------|
| Wazuh Server | SIEM        | VMnet8, VMnet2      | DHCP, Static     | 
| Wazuh Agent  | Traffic Analysis | VMnet8, VMnet2  |  DHCP, Static   | 
| Client       | Traffic Generator | VMnet8, VMnet2 |  DHCP, Static   | 
| Attacker     | Red Team    | VMnet8, VMnet2      |  DHCP, Static    | 

## Commands Used for Static IP Configuration
```bash
nmcli device status
nmcli con add type ethernet ifname <interface-id> con-name <connection-name> ipv4.method manual ipv4.addresses <ip/netmask>
ip a show
ping -c 5 <ip>

