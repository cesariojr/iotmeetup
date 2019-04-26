import signal
import time
import sys
import json
import ibmiotf.application

def myEventCallback(myEvent):
  print("%-33s%-32s%s: %s" % (myEvent.timestamp.isoformat(), myEvent.device, myEvent.event, json.dumps(myEvent.data)))

def interruptHandler(signal, frame):
  client.disconnect()
  sys.exit(0)

options = {
  "org": "sua org",
  "id": "seu id",
  "auth-method": "apikey",
  "auth-key": "sua auth key",
  "auth-token": "seu auth token"
}

try:
  client = ibmiotf.application.Client(options)
  client.connect()

except Exception as e:
  print(str(e))
  sys.exit()

print("(Press Ctrl+C to disconnect)")
client.deviceEventCallback = myEventCallback
client.subscribeToDeviceEvents()

while True:
    time.sleep(1)