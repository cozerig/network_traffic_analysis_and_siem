# Integration Suricata to the Wazuh Agent machine #
### To integrate follow documentation https://documentation.wazuh.com/current/proof-of-concept-guide/integrate-network-ids-suricata.html
### Security Considerations https://docs.suricata.io/en/latest/security.html
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
6. Smth like this you should have in the Events tab:
   ![test-suricata](/images/test-suricata.png)
# classification.config in Suricata
The classification.config file in Suricata defines how classtype values used in detection rules are mapped to a textual description and a numeric severity level (1 to 3). Each line follows the format: config classification: <classtype> <description> <severity>. For example, config classification: attempted-admin Attempted Administrator Privilege Gain 1 means that any rule using classtype:attempted-admin will be treated with severity level 1 (high). When a Suricata rule doesn't explicitly include a severity, Suricata uses the classtype and refers to this file to determine the severity shown in logs like eve.json. By editing this file, you can adjust how specific classtype values are interpreted in terms of severity across your Suricata deployment.
   ![test-suricata](/images/classification.config.png)
# Most used commands 
 ```bash
   sudo suricata-update
   sudo systemctl restart suricata
   sudo truncate -s 0 /var/log/suricata/eve.json
   suricata-update list-sources
   getent group suricata
   getent passwd suricata
   curl http://testmynids.org/uid/index.html
   ```
