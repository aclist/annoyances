
#!/usr/bin/env python
import socket
import threading
import time

FROM_IP = "127.0.0.1"
FROM_PORT = 5998
REPLY_IP = ""
REPLY_PORT = 0
TO_IP = "login.eqemulator.net"
TO_PORT = 5998

from_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
from_sock.bind((FROM_IP, FROM_PORT))
to_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
to_sock.bind(('', 0))

def local():
    global REPLY_IP, REPLY_PORT
    while True:
        data, addr = from_sock.recvfrom(4096)
        REPLY_IP, REPLY_PORT = addr
        to_sock.sendto(data, (TO_IP, TO_PORT))
        print("Sending " + str(len(data)) + " bytes to " + TO_IP + ":" + str(TO_PORT))


def remote():
    global REPLY_IP, REPLY_PORT
    while True:
        data, addr = to_sock.recvfrom(4096)
        from_sock.sendto(data, (REPLY_IP, REPLY_PORT))
        print("Sending " + str(len(data)) + " bytes to " + REPLY_IP + ":" + str(REPLY_PORT))


print("Waiting for data on " + FROM_IP + ":" + str(FROM_PORT) + "...")
threading.Thread(target=local, args=()).start()
threading.Thread(target=remote, args=()).start()
while True:
    time.sleep(1)
