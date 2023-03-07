import pygame
import random
import math
pygame.init()
screen = pygame.display.set_mode()


screen_size = (500, 500);
screen = pygame.display.set_mode(screen_size)

pygame.draw.circle(screen, "blue",(0,0), 100 )

background_color = ("blue")
board_color = ("pink")
line_color = ("black")
miss_color = ("red")
hit_color = ("green")

screen_size_variable = pygame.display.get_window_size();
screen_width = screen_size_variable[0];
screen_height = screen_size_variable[1];
board_center = (screen_width/2, screen_height/2 );
board_radius = screen_width/2;
running = True;
while running:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

  
    screen.fill(background_color)


    pygame.draw.circle(screen, board_color, board_center, board_radius)  
    pygame.draw.line(screen, line_color, (screen_width / 2, 0), (screen_width / 2, 1000), 5)
    pygame.draw.line(screen, line_color, (0, screen_height / 2), (1000, screen_height / 2), 5)

    for i in range(10):
        x1 = random.randrange(0, screen_width)
        x2 = screen_width/2
        y1 = random.randrange(0, screen_height)
        y2 = screen_height/2
        distance_from_center = math.hypot(x1-x2, y1-y2) 
        is_in_circle = distance_from_center <= screen_width / 2

        if is_in_circle:
            pygame.draw.circle(screen, hit_color, (x1, y1), 5)
        else:
            pygame.draw.circle(screen, miss_color, (x1, y1), 5) 
         
 
    pygame.display.flip()


pygame.quit() 