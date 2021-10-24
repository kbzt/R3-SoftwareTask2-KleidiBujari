from socket import *

port = 5005
s = socket(AF_INET, SOCK_STREAM)
s.bind(('', port))
s.listen(10)

while 1:
    #connecting to client
    client_socket, address = s.accept()
    print("Client connected!")

    #recieving packet and decoding into string for analysis
    packet = client_socket.recv(1024)
    message = packet.decode('utf-8')
    direction = message.partition(",")[0]
    speed = message.partition(",")[2]

    #output from server/rover
    if direction == "straight":
        print("[f" + speed + "][f" + speed + "][f" + speed + "][f" + speed + "]")
    if direction == "left":
        print("[r" + speed + "][r" + speed + "][f" + speed + "][f" + speed + "]")
    if direction == "right":
        print("[f" + speed + "][f" + speed + "][r" + speed + "][r" + speed + "]")
    if direction == "back":
        print("[r" + speed + "][r" + speed + "][r" + speed + "][r" + speed + "]")
