import network
import time

ap_essid = "MyCustomESSID"
ap_password = "MyCustomPassword"

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ap_essid, password=ap_password)

print("AP started with ESSID:", ap_essid)

while not ap.active():
    time.sleep(1)

print("AP interface is active")
print("AP IP address:", ap.ifconfig()[0])
