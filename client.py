from types import prepare_class
import pygame
from pygame.constants import QUIT
import socket

tcp_ip = '127.0.0.1'
port = 5005

speed = 0
direction = ""
full = False

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((tcp_ip, port))

#setting up requirements for pygame capture window
pygame.init()
screen = pygame.display.set_mode((100, 100))
pygame.display.set_caption('Client')
pygame.mouse.set_visible(1)


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
            if event.key == pygame.K_1:
                speed = 1
            if event.key == pygame.K_2:
                speed = 2
            if event.key == pygame.K_3:
                speed = 3
            if event.key == pygame.K_4:
                speed = 4
            if event.key == pygame.K_5:
                speed = 5
            
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
            
            if full == True:
                packet = direction + "," + str(speed)
                print("Sent: " + packet)
                s.send((bytes(packet, encoding='utf8')))
            
    
    