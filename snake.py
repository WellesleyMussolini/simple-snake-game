import pygame; 
import random; 

pygame.init(); 


blue = (50, 100, 213); 
orange = (205, 102, 0); 
green = (0, 255, 0);
yellow = (255, 255, 102);   

dimensions = (600, 600);   # screen size

x = 300; 
y = 300; 

d = 20; 

snake_list = [[x, y]]; 

dx = 0; 
dy = 0; 

x_food = round(random.randrange(0, 600 - d) / 20) * 20; 
y_food = round(random.randrange(0, 600 - d) / 20) * 20; 

source = pygame.font.SysFont("hack", 35); 

screen = pygame.display.set_mode((dimensions)); 
pygame.display.set_caption("Snake from Wellesley"); 

screen.fill(blue); 

clock = pygame.time.Clock(); 


def draw_snake(snake_list):
    screen.fill(blue); 
    for unity in snake_list:
        pygame.draw.rect(screen, orange, [unity[0], unity[1], d, d]); 


def move_snake(dx, dy, snake_list):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -d; 
                dy = 0; 
            elif event.key == pygame.K_RIGHT:
                dx = d; 
                dy = 0; 
            elif event.key == pygame.K_UP:
                dx = 0; 
                dy = -d; 
            elif event.key == pygame.K_DOWN:
                dx = 0; 
                dy = d; 

    x_new = snake_list[-1][0] + dx; 
    y_new = snake_list[-1][1] + dy; 

    snake_list.append([x_new, y_new]); 

    del snake_list[0]; 

    return dx, dy, snake_list; 

def check_the_food(dx, dy, x_food, y_food, snake_list):

    head = snake_list[-1]; 

    x_new = head[0] + dx; 
    y_new = head[1] + dy; 

    if head[0] == x_food and head[1] == y_food:
        snake_list.append([x_new, y_new]); 
        x_food = round(random.randrange(0, 600 - d) / 20) * 20; 
        y_food = round(random.randrange(0, 600 - d) / 20) * 20; 

    pygame.draw.rect(screen, green, [x_food, y_food, d, d]); 

    return x_food, y_food, snake_list;  

def check_the_wall(snake_list):
    head = snake_list[-1]; 
    x = head[0]; 
    y = head[1]; 

    if x not in range(600) or y not in range(600):
        raise Exception;  

def check_the_bite(snake_list):
    head = snake_list[-1]; 
    body = snake_list.copy(); 

    del body[-1]; 
    for x,y in body:
        if x == head[0] and y == head[1]:
            raise Exception; 

def update_score(snake_list):
    points = str(len(snake_list));   
    score = source.render("Score: " + points, True, yellow); 
    screen.blit(score, [0, 0]); 



while True:
    pygame.display.update(); 
    draw_snake(snake_list); 
    dx, dy, snake_list = move_snake(dx, dy, snake_list); 
    x_food, y_food, snake_list = check_the_food(dx, dy, x_food, y_food, snake_list); 
    check_the_wall(snake_list); 
    check_the_bite(snake_list);  
    update_score(snake_list);  

    clock.tick(10); 
