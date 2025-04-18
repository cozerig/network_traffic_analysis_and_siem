#!/usr/bin/env python3
import sys
import json
import requests

CHAT_ID = ""
hook_url = sys.argv[3]

with open(sys.argv[1]) as alert_file:
  for line in alert_file:
    try:
      alert_json = json.loads(line)
      alert_level = alert_json.get('rule', {}).get('level', "N/A")
      description = alert_json.get('rule', {}).get('description', "N/A")
      agent = alert_json.get('agent', {}).get('name', "N/A")
      src_ip = alert_json.get('data', {}).get('src_ip', "N/A")
      dest_ip = alert_json.get('data', {}).get('dest_ip', "N/A")
      timestamp = alert_json.get('data', {}).get('timestamp', "N/A")

      message = f"Alert from Wazuh:\nAgent: {agent}\nLevel: {alert_level}\nDescription: {description}\nSource IP: {src_ip}\nDestination IP: {dest_ip}\nTimestamp: {timestamp}"

      msg_data = {
          'chat_id': CHAT_ID,
          'text': message,
          'parse_mode': 'Markdown'
      }

      headers = {'Content-Type': 'application/json'}
      response = requests.post(hook_url, headers=headers, data=json.dumps(msg_data))

      print("Status code:", response.status_code)
      print("Response:", response.text)
 
  except json.JSONDecodeError as e:
      print("JSON decode error:", e)
      continue

sys.exit(0)
