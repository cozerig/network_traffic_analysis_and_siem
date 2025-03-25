# Wazuh Server Deployment in Docker 
## Use official documentation for deployment => ##
### Docker installation 
https://documentation.wazuh.com/current/deployment-options/docker/docker-installation.html
### Wazuh Docker deployment ###
https://documentation.wazuh.com/current/deployment-options/docker/wazuh-container.html
# Most used commands
```bash
docker exec -it single-node-wazuh.manager-1 /bin/bash
docker exec -it single-node-wazuh.manager-1 rm -f /var/ossec/logs/alerts/alerts.json
docker restart single-node-wazuh.manager-1
docker-compose up -d
docker-compose down
```
