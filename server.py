from socket import *

port = 5005
s = socket(AF_INET, SOCK_STREAM)
s.bind(('', port))
s.listen(10)

while 1:
    client_socket, address = s.accept()
    print("Client connected!")
    packet = client_socket.recv(1024)
    message = packet.decode('utf-8')
    direction = message.partition(",")[0]
    speed = message.partition(",")[2]

    if direction == "straight":
        print("[f" + speed + "][f"+ speed + "][f"+ speed +"][f"+ speed+ "]")
    if direction == "left":
        print("[r%d][r%d][f%d][f%d]", speed)
    if direction == "right":
        print("[f%d][f%d][r%d][r%d]", speed)
    if direction == "back":
        print("[r%d][r%d][r%d][r%d]", speed)
