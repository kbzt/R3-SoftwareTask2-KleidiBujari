from types import prepare_class
import pygame
from pygame.constants import QUIT
import socket

tcp_ip = '127.0.0.1'
port = 5005

#variables used to track speed, direction, and if packet is ready to be sent
speed = 0
direction = ""
full = False

#initializing socket for transferring data at localhost with port 5005
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((tcp_ip, port))

#setting up requirements for pygame capture window
pygame.init()
screen = pygame.display.set_mode((250, 250))
pygame.display.set_caption('Client Keyboard Capture')
pygame.mouse.set_visible(1)

#loop for pygame to collect input
active = True
while active:
    for event in pygame.event.get():
        if event.type == QUIT:
            active = False
            s.close()
        if event.type == pygame.KEYDOWN:
            #speed control
            if event.key == pygame.K_0:
                speed = 0
                print("Speed set to:", speed)
            if event.key == pygame.K_1:
                speed = 1
                print("Speed set to:", speed)
            if event.key == pygame.K_2:
                speed = 2
                print("Speed set to:", speed)
            if event.key == pygame.K_3:
                speed = 3
                print("Speed set to:", speed)
            if event.key == pygame.K_4:
                speed = 4
                print("Speed set to:", speed)
            if event.key == pygame.K_5:
                speed = 5
                print("Speed set to:", speed)

            
            
            #wasd keys
            if event.key == pygame.K_w:
                direction = "straight"
                full = True
            if event.key == pygame.K_a:
                direction = "left"
                full = True
            if event.key == pygame.K_s:
                direction = "back"
                full = True
            if event.key == pygame.K_d:
                direction = "right"
                full = True
            
            #if packet is full/ready, send and print what was sent
            if full == True:
                packet = direction + "," + str(speed)
                print("Sent: " + packet)
                s.send((bytes(packet, encoding='utf8')))
            
    
    