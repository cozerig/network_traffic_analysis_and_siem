# Wazuh Server Deployment in Docker 
## Use official documentation for deployment => ##
### Docker installation 
https://documentation.wazuh.com/current/deployment-options/docker/docker-installation.html
### Wazuh Docker deployment ###
https://documentation.wazuh.com/current/deployment-options/docker/wazuh-container.html
# Before configuring local_rules.xml
Before configuration of SIEM rules for detect attack watch the if_sid variable especially for alert event type. Because this variable will be used in local_rules.xml.
![if_sid](/images/if_sid.png)

In Wazuh custom rules, if_sid is used to link your custom rule to an existing rule (from Suricata, OSSEC, or another source). If an alert matches the rule with that sid, your custom rule will also trigger.
This is useful for adding extra conditions or changing the severity level of a detected event.
# Most used commands
```bash
docker exec -it single-node-wazuh.manager-1 /bin/bash
docker exec -it single-node-wazuh.manager-1 rm -f /var/ossec/logs/alerts/alerts.json
docker restart single-node-wazuh.manager-1
docker-compose up -d
docker-compose down
```
