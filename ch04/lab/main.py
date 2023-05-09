import pygame
import random
import math
pygame.init()
screen = pygame.display.set_mode()


screen_size = (750, 750);
screen = pygame.display.set_mode(screen_size)

pygame.draw.circle(screen, "blue",(0,0), 100 )

background_color = ("blue")
board_color = ("pink")
line_color = ("black")
player1_hit_color = ("red")
player1_miss_color = ("yellow")
player2_hit_color = ("navy")
player2_miss_color = ("green")
player1_score = 0
player2_score = 0

screen_size_variable = pygame.display.get_window_size();
screen_width = screen_size_variable[0];
screen_height = screen_size_variable[1];
board_center = (screen_width/2, screen_height/2 );
board_radius = screen_width/2;

  
screen.fill(background_color)


pygame.draw.circle(screen, board_color, board_center, board_radius)  
pygame.draw.line(screen, line_color, (screen_width / 2, 0), (screen_width / 2, 1000), 5)
pygame.draw.line(screen, line_color, (0, screen_height / 2), (1000, screen_height / 2), 5)

player1_box = pygame.Rect(150, 100, 100, 100)
player2_box = pygame.Rect(500, 100, 100, 100)

pygame.draw.rect(screen, player1_hit_color, player1_box)
pygame.draw.rect(screen, player2_hit_color, player2_box)

# Add text to the boxes
font = pygame.font.Font(None, 32)
text = font.render("Player 1", True, "white")
screen.blit(text, (150, 100))

text = font.render("Player 2", True, "white")
screen.blit(text, (500, 100))

pygame.display.flip()


player_guess = None
while player_guess is None:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if player1_box.collidepoint(mouse_pos):
                player_guess = 1
            elif player2_box.collidepoint(mouse_pos):
                player_guess = 2


    
for i in range(10):
    x1 = random.randrange(0, screen_width)
    x2 = screen_width/2
    y1 = random.randrange(0, screen_height)
    y2 = screen_height/2
    distance_from_center = math.hypot(x1-x2, y1-y2) 
    is_in_circle = distance_from_center <= screen_width / 2

    if is_in_circle:
        pygame.draw.circle(screen, player1_hit_color, (x1, y1), 5)
        player1_score +=1
    else:
        pygame.draw.circle(screen, player1_miss_color, (x1, y1), 5) 

for i in range(10):
    x1 = random.randrange(0, screen_width)
    x2 = screen_width/2
    x1 = random.randrange(0, screen_height)
    y2 = screen_height/2
    distance_from_center = math.hypot(x1-x2, y1-y2) 
    is_in_circle = distance_from_center <= screen_width / 2

    if is_in_circle:
        pygame.draw.circle(screen, player2_hit_color, (x1, y1), 5)
        player2_score +=1
    else:
        pygame.draw.circle(screen, player2_miss_color, (x1, y1), 5) 

if player1_score > player2_score:
    font = pygame.font.Font(None, 48)
    text = font.render("Player 1 wins", True, "white")
    screen.blit(text, (250, 250))
    if player_guess == 1:
        font = pygame.font.Font(None, 48)
        text = font.render("User guesssed correctly", True, "white")
        screen.blit(text, (250, 300))
    else:
        font = pygame.font.Font(None, 48)
        text = font.render("User did not guess correctly", True, "white")
        screen.blit(text, (250, 300))
                
if player2_score > player1_score:
    font = pygame.font.Font(None, 48)
    text = font.render("Player 2 wins", True, "white")
    screen.blit(text, (250, 250))
    if player_guess == 2:
        font = pygame.font.Font(None, 48)
        text = font.render("User guesssed correctly", True, "white")
        screen.blit(text, (250, 300))
    else:
        font = pygame.font.Font(None, 48)
        text = font.render("User did not guess correctly", True, "white")
        screen.blit(text, (250, 300))
                
if player1_score == player2_score:
    font = pygame.font.Font(None, 48)
    text = font.render("Tie!", True, "white")
    screen.blit(text, (250, 250))



pygame.display.flip()                
pygame.time.delay(5000);

