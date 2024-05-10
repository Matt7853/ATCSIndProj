# Code to check if left or right mouse buttons were pressed
import win32api
import time
import pygame

# https://stackoverflow.com/a/41930485

state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
state_right = win32api.GetKeyState(0x02)  # Right button down = 0 or 1. Button up = -127 or -128

time_start = time.time()
clicks = 0

while time.time() - time_start <= 10:
    a = win32api.GetKeyState(0x01)
    b = win32api.GetKeyState(0x02)

    if a != state_left:  # Button state changed
        state_left = a
        if a < 0:
            clicks+=1

    if b != state_right:  # Button state changed
        state_right = b
        if b < 0:
            print("that's a right click bozo")

print(str(clicks) + " clicks | " + str(clicks/10) + " clicks per second!")


# https://www.geeksforgeeks.org/how-to-make-a-pygame-window/
# Define the background colour 
# using RGB color coding. 
background_colour = (0,0,0)
  
# Define the dimensions of 
# screen object(width,height) 
screen = pygame.display.set_mode((800, 600)) 
  
# Set the caption of the screen 
pygame.display.set_caption('Geeksforgeeks') 
  
# Fill the background colour to the screen 
screen.fill(background_colour) 
  
# Update the display using flip 
pygame.display.flip() 
  
# Variable to keep our game loop running 
running = True
  
# game loop 
while running: 
    
# for loop through the event queue   
    for event in pygame.event.get(): 
      
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False
