from machine import PWM, Pin
import network
import socket
from utime import sleep

buzzer = PWM(Pin(15))
buzzer.duty_u16(32767)
frequency = 1000

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
    global frequency
    request = conn.recv(1024)
    if b"GET /buzzer=up" in request:
        frequency += 50
    elif b"GET /buzzer=down" in request:
        frequency -= 50
    response = f"""HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n
<!DOCTYPE html>
<html>
    <head>
        <title>Raspberry Pi Pico W</title>
        <style>
            body {{
                text-align: center;
                background-color: darkcyan;
            }}
        </style>
    </head>
    <body>
        <h1>Buzzer control panel</h1>
        <h1>Current frequency: {frequency}</h1>
        <h1>The IP address is {ip} and the port is {port}</h1>
        <button onclick="location.href='/buzzer=up'">Frequency Up</button>
        <button onclick="location.href='/buzzer=down'">Frequency Down</button>
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
    buzzer.freq(frequency)
    conn, addr = s.accept()
    print("Connection from:", addr)
    handle_request(conn)
    sleep(0.1)