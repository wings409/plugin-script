#!/usr/bin/env python
 
import requests
import time
import json
 
ts = int(time.time())
minute = int(time.strftime("%M", time.localtime()))
minute_is_even = (minute + 1) % 2
 
payload = [
    {
        "endpoint": "open-falcon-server-user-define",
        "metric": "minute-is-even",
        "timestamp": ts,
        "step": 60,
        "value": minute_is_even,
        "counterType": "GAUGE",
        "tags": "usage=stupid",
    },
]
 
# r = requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(payload))
print  json.dumps(payload)
