import requests
import time

URL = "http://127.0.0.1:5001"

print("BOT STARTED")

while True:
    try:
        r = requests.get(URL, timeout=1)
        print("Status:", r.status_code)
    except Exception as e:
        print("Error:", e)
    time.sleep(0.2)