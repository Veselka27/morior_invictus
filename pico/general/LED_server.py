# Import libraries

import network
import socket
from time import sleep
from machine import Pin

# Set LEDs

green = Pin(1, Pin.OUT)
red = Pin(15, Pin.OUT)
led = Pin("LED", Pin.OUT)
yellow = Pin(13, Pin.OUT)

# Set Wi-Fi, Password and connect to it

ssid = input("ssid: ")
password = input("Password: ")
port = int(input("Port to serve on: "))

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)

print("Waiting for connection...")
while not wifi.isconnected():
    pass

ip = wifi.ifconfig()[0]
print("Successfully connected!")
print(f"Connected to network: {ssid}")
print(f"The password is: {password}")
print(f"The IP address is: {ip}")

def handle_request(conn):
    request = conn.recv(1024)
    if b"GET /led=on" in request:
        green.value(1)
        red.on()
        yellow.on()
        led.on()
    elif b"GET /led=off" in request:
        green.value(0)
        red.off()
        yellow.off()
        led.off()
    response = f"""HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n
<!DOCTYPE html>
<html>
    <head>
        <title>Raspberry Pi Pico W</title>
        <style>
            body {{
                text-align: center;
                background-color: #F0F2F5;
                font-family: Arial, sans-serif;
                font-size: 16px;
                line-height: 1.5;
                padding: 1em;
            }}
            h1 {{
                margin-top: 0;
            }}
            .led {{
                display: inline-block;
                width: 50px;
                height: 50px;
                margin: 1em;
                border-radius: 50%;
                background-color: {"#4CAF50" if green.value() else "#F44336"};
            }}
            .led-label {{
                display: block;
                font-size: 1.5em;
                margin-bottom: 1em;
            }}
            .button {{
                display: inline-block;
                padding: 1em;
                border: none;
                border-radius: 5px;
                background-color: #2196F3;
                color: #FFFFFF;
                font-size: 1em;
                cursor: pointer;
            }}
            .button:hover {{
                background-color: #0D47A1;
            }}
        </style>
    </head>
    <body>
        <h1>LED Control Panel</h1>
        <div class="led"></div>
        <div class="led-label">The LED is currently {"on" if green.value() else "off"}</div>
        <div>
            <button class="button" onclick="location.href='/led=on'">LED On</button>
            <button class="button" onclick="location.href='/led=off'">LED Off</button>
        </div>
        <br>
        <div>The IP address is {ip} and the port is {port}</div>
    </body>
</html>"""

    conn.send(response)
    conn.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip, port))
s.listen(5)

if port == 80:
    print("Web server is running:")
    print(f"http://{ip}")
else:
    print(f"Web server is running on port {port}:")
    print(f"http://{ip}:{port}")

while True:
    conn, addr = s.accept()
    print("Connection from:", addr)
    handle_request(conn)
    sleep(0.1)
