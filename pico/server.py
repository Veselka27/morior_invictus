import network
import socket
from time import sleep
from machine import Pin
led = Pin(0, Pin.OUT)

ssid = "roubenka_EXT"
password = "Karkulka.123"

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)

print("Waiting for connection...")
while not wifi.isconnected():
    pass

print("Succesfully connected!")
print(f"Connected to network: {ssid}")
print(f"The password is: {password}")
ip = wifi.ifconfig()[0]
print(f"The IP address is: {ip}")

def handle_request(conn):
    request = conn.recv(1024)
    if b"GET /led=on" in request:
        led.value(1)
    elif b"GET /led=off" in request:
        led.value(0)
        
    response = """HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n
            <!DOCTYPE html>
            <html>
                <head>
                    <title>Rapberry Pi Pico W</title>
                    <style>
                        body {{
                            background-color: darkgray;
                            text-align: center;
                            }}
                    </style>
                </head>
                <body>
                    <h1>LED Control Panel</h1>
                    <h1>The LED is currently {state}</h1>
                    <h2>The IP address is {ip} and the port is {port}</h2>
                    <button onclick="location.href='/led=on'">LED On</button>
                    <button onclick="location.href='/led=off'">LED Off</button>
                </body>
            </html>""".format(state="on" if led.value() else "off", ip=ip, port=port)

    conn.send(response)
    conn.close()
port = 80
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

