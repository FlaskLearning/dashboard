import requests
import os
import time

token = os.environ.get("INFLUXDB_TOKEN")
print(token)
url = "https://127.0.0.1:8086/api/v2/write"
params = {
    "org": "myorg",
    "bucket": "mydata",
    "precision": "ns"
}
headers = {
    "Authorization": f"Token {token}",
    "Content-Type": "text/plain; charset=utf-8"
}

for value in range(5):
    data = f"measurement1,tagname1=tagvalue1 field1={value} {time.time_ns()}"
    try:
        r = requests.post(url, params=params, headers=headers, data=data)
        r.raise_for_status()
        print(f"Successfully wrote point: {value}")
        time.sleep(1)
    except Exception as e:
        print(f"Error writing point {value}: {e}")
        print(f"Response: {r.text if 'r' in locals() else ''}")
        break