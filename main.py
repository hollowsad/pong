# Загрузка модуля pygame.
import pygame
import random


# Загрузка внутренних модулей Pygame
pygame.init()

# Разрешение окна СЦЕНЫ.
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Создание окна СЦЕНЫ:
SCENE = pygame.display.set_mode(
    [SCREEN_WIDTH, SCREEN_HEIGHT],     # Разрешение окна программы.
    flags=pygame.SCALED,               # Интрукция для вертикальной синхронизации.
    vsync=True                         # Вертикальная синхронизация.
)
# Заголовок окна СЦЕНА:
pygame.display.set_caption('pygame')
logo = pygame.image.load('7fc0364fbb9f319b5d4cb4bc104eb7d2.jpg')
pygame.display.set_icon(logo)
# Блок для загрузки объектов:

ball = pygame.Rect(SCREEN_WIDTH/2 -25, SCREEN_HEIGHT/2 - 25, 50, 50)
ball_speed_x = 5
ball_speed_y = 5
player = pygame.Rect(20, 300, 25, 100)

enemy = pygame.Rect(SCREEN_WIDTH - 45, 300, 25, 100)
pygame.mouse.set_visible(False)
# Шрифт
FONT = pygame.font.Font('SANYO-CYR_0.ttf', 100)
player_score = 0
enemy_score = 0


# Sound

bg_theme = pygame.mixer.Sound('main_theme.mp3')
bg_theme.set_volume(0.1)
bg_theme.play(-1)


ball_hit = pygame.mixer.Sound('ball_hit.wav')
ball_hit.set_volume(0.2)

# Настройки FPS:
FPS = 60
clock = pygame.time.Clock()



# СЦЕНА:
running = True
while running:
    clock.tick(FPS)

    # Заливка фона сцены RGB
    SCENE.fill([35, 35, 35])

    player_text = FONT.render(f'{player_score}', True, [65, 75, 90])
    SCENE.blit(player_text, [0 + 150, 0 + 150])

    enemy_text = FONT.render(f'{enemy_score}', True, [45, 175, 175])
    SCENE.blit(enemy_text, [0 + 550, 0 + 350])

    ball.x += ball_speed_x
    ball.y += ball_speed_y


    if ball.x > SCREEN_WIDTH - 50:
        player_score += 1
    if ball.x < 0 - 100:
        enemy_score += 1

    if ball.x > SCREEN_WIDTH - 50 or ball.x < 0 - 100:
        ball.center = SCREEN_WIDTH/2 -25, SCREEN_HEIGHT/2 - 25
        ball_speed_x = random.choice([-5, 5, 5])
        ball_speed_y = random.choice([-5, 5, 5])

    if ball.y > SCREEN_HEIGHT - 50 or ball.y < 0:
        ball_speed_y = ball_speed_y * -1

    pygame.draw.ellipse(SCENE, [230, 230, 230], ball)

    pygame.draw.rect(SCENE, [70, 70, 70], player)

    print('ball', ball.x, ball.y)
    print('enemy', enemy.x, enemy.y)
    enemy.y = ball.y
    pygame.draw.rect(SCENE, [150, 70, 70], enemy)

    if ball.colliderect(player):
        ball_speed_x *= -1.2
        ball_speed_y *= -1.2
        ball_hit.play()

    if ball.colliderect(enemy):
        ball_speed_x *= -1.2
        ball_speed_y *= -1.2
        ball_hit.play()

    if ball_speed_x > 90:
        ball_speed_x = 90

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        if player.top > 0:
            player.y -= 7

    if keys[pygame.K_s]:
        if player.bottom < SCREEN_HEIGHT:
            player.y += 7

    # Обработка событий в окне сцены:
    for event in pygame.event.get():

        # Нажатие на крестик окна завершит цикл СЦЕНЫ:
        if event.type == pygame.QUIT:
            running = False
            
    pygame.display.update()


# Выход из программы.
pygame.quit()










    
