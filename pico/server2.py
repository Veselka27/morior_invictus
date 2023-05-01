# Import libraries

import network
import usocket as socket
from time import sleep
from machine import Pin, PWM

# Set LEDs

green = Pin(0, Pin.OUT)
red = Pin(1, Pin.OUT)
yellow = Pin(2, Pin.OUT)

green.off()
red.off()
yellow.off()

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
    global on
    global frequency
    request = conn.recv(1024)
    if b"GET /green=on" in request:
        green.value(1)
        red.off()
        yellow.off()
    elif b"GET /red=on" in request:
        red.value(1)
        green.off()
        yellow.off()
    elif b"GET /yellow=on" in request:
        yellow.value(1)
        green.off()
        red.off()
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
                background-color: {"#4CAF50" if green.value() else "#F44336" if red.value() else "#edb118" if yellow.value() else "#F0F2F5"};
            }}
            .led-label {{
                display: block;
                font-size: 1.5em;
                margin-bottom: 1em;
            }}
            .green {{
                display: inline-block;
                padding: 1em;
                border: none;
                border-radius: 5px;
                background-color: #4CAF50;
                color: #FFFFFF;
                font-size: 1em;
                cursor: pointer;
            }}
            .red {{
                display: inline-block;
                padding: 1em;
                border: none;
                border-radius: 5px;
                background-color: #F44336;
                color: #FFFFFF;
                font-size: 1em;
                cursor: pointer;
            }}
            .yellow {{
                display: inline-block;
                padding: 1em;
                border: none;
                border-radius: 5px;
                background-color: #edb118;
                color: #FFFFFF;
                font-size: 1em;
                cursor: pointer;
            }}
            .green:hover {{
                background-color: #309333;
            }}
            .red:hover {{
                background-color: #e52c1f;
            }}
            .yellow:hover {{
                background-color:  #ed9b18
            }}
        </style>
    </head>
    <body>
        <h1>LED Control Panel</h1>
        <div class="led"></div>
        <div class="led-label">{"Green" if green.value() else "Red" if red.value() else "Yellow" if yellow.value() else "No"} LED is currently on</div>
        <div>
            <button class="green" onclick="location.href='/green=on'">Green</button>
            <button class="red" onclick="location.href='/red=on'">Red</button>
            <button class="yellow" onclick="location.href='/yellow=on'">Yellow</button>
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
    

