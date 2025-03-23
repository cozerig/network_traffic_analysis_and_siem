# Integration Suricata to the Wazuh Agent machine #
### To integrate follow documentation https://documentation.wazuh.com/current/proof-of-concept-guide/integrate-network-ids-suricata.html
# To ensure that everything works fine follow these steps:
1. Create custom rule in **/etc/suricata/rules** directory
   ```bash
   nano /etc/suricata/rules/custom.rules
   alert icmp any any -> any any (msg:"ICMP Test Alert"; sid:1000001; rev:1;)
   ```
2. Modify Suricata settings in the /etc/suricata/suricata.yaml file and set the following variables:
   ```bash
   rule-files:
     - "custom.rules"
   ```
3. Restart suricata service
   ```bash
   systemctl restart suricata
   ```
4. ping your machine with Suricata 
5. Go to the Wazuh dashboard, choose in the Menu tab **Threat Hunting** under Threat intelligence option
6. Smth like this you should have in the Event tab:
   
