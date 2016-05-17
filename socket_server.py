import pygame, sys
from socket import socket, AF_INET, SOCK_DGRAM
from time import gmtime, strftime
from pygame.locals import *

SERVER_IP   = '127.0.0.1'
PORT_NUMBER = 5000
SCREEN_X = 400
SCREEN_Y = 400
SIZE = 1024
PIC_PATH = "picture/path/goes/here.bmp"
print ("Test client sending packets to IP {0}, via port {1}\n".format(SERVER_IP, PORT_NUMBER))

mySocket = socket( AF_INET, SOCK_DGRAM )
x = y = 0
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y)) #Make the screen
ending = False
word = "True"
clock = pygame.time.Clock() #tick-tock
grid = pygame.image.load(PIC_PATH) #Load the sheet
gridRect = grid.get_rect()
screen.blit(grid, gridRect)
pygame.display.flip()
while ending==False:
    for event in pygame.event.get():
        if event.type == KEYDOWN: # key down or up?
            if event.key == K_RIGHT: x+=1
            elif event.key == K_LEFT: x-=1
            elif event.key == K_UP: y-=1
            elif event.key == K_DOWN: y+=1
            if event.key == K_ESCAPE:
                ending=True # Time to leave
                print("Stopped Early by user")
    if ending==True: word="False"
    localTime = strftime( "%H:%M:%S", gmtime() )
    mySocket.sendto( bytes(str(x), 'UTF-8') , (SERVER_IP, PORT_NUMBER) )
    mySocket.sendto( bytes(str(y), 'UTF-8') , (SERVER_IP, PORT_NUMBER) )
    mySocket.sendto( bytes(word, 'UTF-8') , (SERVER_IP, PORT_NUMBER) )
    print ("Sending packet... " + localTime)
    clock.tick(10)
    try:
        (data, addr) = mySocket.recvfrom( SIZE )
        print ("Received packet from: " + str(addr))
        print ("Received: " + data.decode('UTF-8'))
    except: ending=False
    if ending==True:
        pygame.quit()
        sys.exit()