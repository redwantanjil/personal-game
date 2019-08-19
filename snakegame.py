import pygame
import random
pygame.init()

# creating game variables and function
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
clock = pygame.time.Clock()
fps = 10


window = pygame.display.set_mode((500, 250))
font = pygame.font.SysFont(None, 25)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    window.blit(screen_text, [x, y])


def snake(win, color, snake_list, hight):
    for x, y in snake_list:
        pygame.draw.rect(win, color, [x, y, hight, hight])


#creating home screen
def welcome():
    game_exite = False
    while not game_exite:
        window.fill(white)
        text_screen("snake game by REDWAN TANJIL",black,120,125)
        text_screen("press space to continue", black, 150, 145)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exite = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()

        pygame.display.update()
        clock.tick(fps)


#creating game loop
def game_loop():

    # creating food valiablera
    game_exite = False
    game_over = False
    food_hight = 10
    food_width = 10
    food_x = random.randint(1, 45) * 10
    food_y = random.randint(1, 22) * 10
    # creating snake variables
    snake_hight = 10
    snake_width = 10
    snake_x = random.randint(1, 49) * 10
    snake_y = random.randint(1, 24) * 10
    moson_x = 0
    moson_y = 0
    snake_list = []
    snake_len = 1
    score = 0

    while not game_exite:

        if game_over:
            window.fill(white)
            text_screen("GAME OVER!PLEASE ENTER TO CONTINUE", red, 100, 90)
            text_screen("score: " + str(score * 10), red, 180, 115)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    game_exite=True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop()

        else:
            #creating  food and displaying text
            pygame.display.set_caption("snake game")
            snake(window, red, snake_list, snake_hight)
            pygame.draw.rect(window,(white),(food_x,food_y,food_hight,food_width))


            #creating game crontroll
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    game_exite=True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        moson_x=10
                        moson_y=0
                    if event.key==pygame.K_LEFT:
                        moson_x=-10
                        moson_y=0
                    if event.key==pygame.K_UP:
                        moson_x=0
                        moson_y=-10
                    if event.key==pygame.K_DOWN:
                        moson_x=0
                        moson_y=+10

            #givig snake a motion
            snake_x+=moson_x
            snake_y+=moson_y

            #random food and score
            if food_x==snake_x and food_y==snake_y:
                score+=1
                food_x = random.randint(1, 45) * 10
                food_y = random.randint(1, 22) * 10
                snake_len+=1

            #creating snake
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            if len(snake_list)>snake_len:
                del snake_list[0]

            # creating game over rules
            if snake_list[-1] in snake_list[:-1] or snake_x<0 or snake_x>500 or snake_y<0 or snake_y>250:
                game_over = True

        pygame.display.update()
        clock.tick(fps)
        window.fill(black)

    pygame.quit()

welcome()