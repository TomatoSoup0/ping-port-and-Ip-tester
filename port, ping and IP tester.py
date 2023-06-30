import socket
import time
import os
import requests

L = open("C:\\Users\\User\\Desktop\\links.txt", "r")

ports = {20, 21, 22, 23, 25, 53, 80, 443}

for link in L.readlines():

    link = link.strip()  

    L_ip = socket.gethostbyname(link)

    print(f"Link: {link}")

    print(f"IP: {L_ip}")
    
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((L_ip, port))
        if result == 0:
            print(f"Port {port} is open")

        else:
            print(f"Port {port} is closed")
        sock.close()

    L_ping = os.system("ping -c 1 " + link)

    if L_ping == 0:
        print("network active")
    else:
        print("network error")

    response = requests.get(link)

    print(response.elapsed)

    print("-" * 30)

L.close()
