import pygame
from pygame.locals import *
import random

size = width, height = (800, 800)
road_w = int(width/1.6)
roadmark_w = int(width/80)
# location paramethers
right_lane = width/2 - road_w/4
left_lane = width/2 - road_w/4
# animation parameters
speed = 1

# initialize the app
pygame.init()
running = True

# set window size
screen = pygame.display.set_mode(size)

# set window title
pygame.display.set_caption("Patrice's car game")

# set background color
screen.fill((60, 220, 0))
# apply changes
pygame.display.update()

# load player vehicle
car1 = pygame.image.load("car1.png")
# resize image
car1_loc = car1.get_rect()
car1_loc.center = right_lane, height*0.8 

# load player#2 vehicle
car2 = pygame.image.load("car2.png")
car2_loc = car2.get_rect()
car2_loc.center = left_lane, height*0.2

counter = 0
# game loop
while running:
    counter += 1
    
    # increase game difficulty overtime
    if counter == 5000:
        speed += 0.15
        counter = 0 
        print("Level up ", "%.2f" % speed)
        
    # animate enemy vehicle
    car2_loc[1] += speed
    if car2_loc[1] > height:
        # randomly select lane
        if random.randint(0,1) == 0:
            car2_loc.center = right_lane, -200
        else:
            car2_loc.center = left_lane, -200
    # end game
    if car1_loc[0] == car2_loc[0] and car2_loc[1] > car1_loc[1] - 250:
        print("GAME OVER! YOU LOST!") 
        break
          
    # event listeners
    for event in pygame.event.get():
        if event.type == QUIT:
            # collapse the app
            running = False            
        if event.type == KEYDOWN:
            # move user car to the left
            if event.key in[K_a, K_LEFT]:
                car1_loc = car1_loc.move([-int(road_w/2),0 ])
            # move user car to the right
            if event.key in[K_d, K_RIGHT]:
                car1_loc = car1_loc.move([int(road_w/2),0 ])
    
    # draw road            
    pygame.draw.rect(screen,(50, 50,50),(width/2-road_w/2, 0,road_w, height ))

    # draw center line
    pygame.draw.rect(screen,(255,240,60),(width/2-roadmark_w/2, 0, roadmark_w, height))
    # draw left road marking
    pygame.draw.rect(screen,(255,255,255),(width/2-road_w/2 + roadmark_w*2, 0, roadmark_w, height))
    # draw right road marking
    pygame.draw.rect(screen,(255,255,255),(width/2 + road_w/2 - roadmark_w*3, 0, roadmark_w, height))

    # place car images on the screen
    screen.blit(car1, car1_loc)
    screen.blit(car2, car2_loc)
    # apply changes
    pygame.display.update()

# collapse application window
pygame.quit()
