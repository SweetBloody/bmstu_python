import pygame
from pygame.locals import *
import sys
import random as rnd

# Константы
WIDTH = 900
HEIGHT = 600
FPS = 60

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (160, 160, 160)
BLUE = (0, 0, 255)
LIGHT_BLUE = (80, 150, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
RED = (255, 40, 0)
VENERA = (121, 210, 230)
HOLE_V = (80, 167, 182)
MARS = (161, 37, 27)
HOLE_M = (140, 25, 18)
URAN = (20, 148, 20)
HOLE_U = (10, 123, 10)

# Константы рисунка
delta_y = 0
rocket_width = 40
rocket_X = WIDTH // 2 - rocket_width // 2
earth_y = 0
speed = 0

delta_r = 0
delta_g = 0
delta_b = 0

planet_r = 30

planet1_x = WIDTH + planet_r
planet1_y = -planet_r
planet1_dx = 0
planet1_dy = 0
k1 = 1
dx1 = 1
dy1 = 0.7

planet2_x = -planet_r
planet2_y = -planet_r
planet2_dx = 0
planet2_dy = 0
k2 = 1
dx2 = 0.8
dy2 = 1

planet3_x = WIDTH // 2 + 5 * planet_r
planet3_y = -planet_r
planet3_dx = 0
planet3_dy = 0
k3 = 1
dx3 = 0.2
dy3 = 1.4

flame1_x1 = flame2_x1 = rocket_X + rocket_width // 8
flame1_x2 = flame2_x2 = rocket_X + rocket_width // 4
flame1_x3 = flame2_x3 = rocket_X + 3 * rocket_width // 8
flame1_x4 = flame2_x4 = rocket_X + rocket_width // 2
flame1_x5 = flame2_x5 = rocket_X + 5 * rocket_width // 8
flame1_x6 = flame2_x6 = rocket_X + 3 * rocket_width // 4
flame1_x7 = flame2_x7 = rocket_X + 7 * rocket_width // 8

flame1_dy1 = 5
flame1_dy2 = 3
flame1_dy3 = 4
flame1_dy4 = 3

flame2_dy1 = 3
flame2_dy2 = 0
flame2_dy3 = 1
flame2_dy4 = 1

ufo_width = 100
ufo_height = 40
ufo_r = 25
ufo_x = WIDTH
ufo_y = 0
ufo_dx = 0
ufo_dy = 0
dxu = -1.5
dyu = 1

# Основная инициализация
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


# Главный цикл
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    # Фон
    screen.fill((80 - delta_r, 150 - delta_g, 255 - delta_b))

    # Земля
    pygame.draw.rect(screen, GREEN,
                     (0, 460 + earth_y, WIDTH, HEIGHT - 460))

    #### Планеты

    if delta_b > 165:

        # 1
        pygame.draw.circle(screen, VENERA,
                           (planet1_x + planet1_dx, planet1_y + planet1_dy),
                           planet_r * k1)
        pygame.draw.circle(screen, HOLE_V,
                           (planet1_x + planet_r * k1 // 3 + planet1_dx,
                            planet1_y - planet_r * k1 // 4 + planet1_dy),
                           planet_r * k1 // 2)
        pygame.draw.circle(screen, BLACK,
                           (planet1_x - planet_r * k1 // 2 + planet1_dx,
                            planet1_y - planet_r * k1 // 3 + planet1_dy),
                           planet_r * k1 // 5)
        pygame.draw.circle(screen, HOLE_V,
                           (planet1_x - planet_r * k1 // 6 + planet1_dx,
                            planet1_y + planet_r * k1 // 2 + planet1_dy),
                           planet_r * k1 // 3.5)

        # 2
        pygame.draw.circle(screen, MARS,
                           (planet2_x + planet2_dx, planet2_y + planet2_dy),
                           planet_r * k2)
        pygame.draw.circle(screen, HOLE_M,
                           (planet2_x - planet_r * k2 // 2 + planet2_dx,
                            planet2_y + planet_r * k2 // 3 + planet2_dy),
                           planet_r * k2 // 3)

        # 3
        pygame.draw.circle(screen, URAN,
                           (planet3_x + planet3_dx, planet3_y + planet3_dy),
                           planet_r * k3)
        pygame.draw.circle(screen, HOLE_U,
                           (planet3_x - planet_r * k3 // 2 + planet3_dx,
                            planet3_y + planet_r * k3 // 3 + planet3_dy),
                           planet_r * k3 // 3)
        pygame.draw.circle(screen, HOLE_U,
                           (planet3_x + planet_r * k3 // 4 + planet3_dx,
                            planet3_y - planet_r * k3 // 2 + planet3_dy),
                           planet_r * k3 // 6)

    #### НЛО

    if delta_b > 165:

        # Верхняя часть НЛО
        pygame.draw.circle(screen, LIGHT_BLUE,
                           (ufo_x + ufo_dx + ufo_width // 2,
                            ufo_y + ufo_dy - 0.02 * ufo_r), ufo_r)

        # Инопланетянин
        pygame.draw.ellipse(screen, GREEN,
                            (ufo_x + ufo_dx + ufo_width // 2 - 10,
                             ufo_y + ufo_dy - 0.5 * ufo_r, 20, 30))
        pygame.draw.circle(screen, BLACK,
                           (ufo_x + ufo_dx + ufo_width // 2 - 4,
                            ufo_y + ufo_dy - 0.2 * ufo_r), 2)
        pygame.draw.circle(screen, BLACK,
                           (ufo_x + ufo_dx + ufo_width // 2 + 4,
                            ufo_y + ufo_dy - 0.2 * ufo_r), 2)

        # Корпус
        pygame.draw.ellipse(screen, GRAY,
                            (ufo_x + ufo_dx, ufo_y + ufo_dy,
                             ufo_width, ufo_height))

        # Кружки
        pygame.draw.circle(screen, BLACK,
                           (ufo_x + ufo_dx + ufo_width // 4,
                            ufo_y + ufo_dy + ufo_height // 2), 5)
        pygame.draw.circle(screen, BLACK,
                           (ufo_x + ufo_dx + ufo_width // 2,
                            ufo_y + ufo_dy + ufo_height // 2), 5)
        pygame.draw.circle(screen, BLACK,
                           (ufo_x + ufo_dx + 3 * ufo_width // 4,
                            ufo_y + ufo_dy + ufo_height // 2), 5)

    #### Ракета

    # Корпус
    pygame.draw.rect(screen, GRAY,
                     (rocket_X, 380 - delta_y, rocket_width, 80))
    # Левое крыло
    pygame.draw.polygon(screen, RED,
                        [[rocket_X - 20, 460 - delta_y],
                         [rocket_X, 460 - delta_y],
                         [rocket_X, 425 - delta_y]])
    # Правое крыло
    pygame.draw.polygon(screen, RED,
                        [[rocket_X + rocket_width + 20, 460 - delta_y],
                         [rocket_X + rocket_width, 460 - delta_y],
                         [rocket_X + rocket_width, 425 - delta_y]])

    # Верхняя часть
    pygame.draw.polygon(screen, RED,
                        [[rocket_X, 380 - delta_y],
                         [rocket_X + rocket_width, 380 - delta_y],
                         [WIDTH // 2, 330 - delta_y]])

    # Иллюминаторы
    pygame.draw.circle(screen, BLUE,
                       (WIDTH // 2, 395 - delta_y), 10)
    pygame.draw.circle(screen, BLUE,
                       (WIDTH // 2, 425 - delta_y), 10)

    # Пламя
    pygame.draw.polygon(screen, RED,
                        [[rocket_X, 460 - delta_y],
                         [flame1_x1, 460 - delta_y + flame1_dy1],
                         [flame1_x2, 460 - delta_y + 5],
                         [flame1_x3, 460 - delta_y + flame1_dy2],
                         [flame1_x4, 460 - delta_y + 3],
                         [flame1_x5, 460 - delta_y + flame1_dy3],
                         [flame1_x6, 460 - delta_y + 4],
                         [flame1_x7, 460 - delta_y + flame1_dy4],
                         [rocket_X + rocket_width, 460 - delta_y]])

    pygame.draw.polygon(screen, YELLOW,
                        [[rocket_X, 460 - delta_y],
                         [flame2_x1, 460 - delta_y + flame2_dy1],
                         [flame2_x2, 460 - delta_y + 2],
                         [flame2_x3, 460 - delta_y + flame2_dy2],
                         [flame2_x4, 460 - delta_y + 1],
                         [flame2_x5, 460 - delta_y + flame2_dy3],
                         [flame2_x6, 460 - delta_y + 1],
                         [flame2_x7, 460 - delta_y + flame2_dy4],
                         [rocket_X + rocket_width, 460 - delta_y]])


    #### Анимация

    # Звезды
    if delta_b > 155:
        for i in range(15):
            x = rocket_X + rocket_width // 2
            y = 200

            while (x > rocket_X - 20) and (x < rocket_X + rocket_width + 20)\
                    and (y > 150) and (y < 280):
                x = rnd.randint(0, WIDTH)
                y = rnd.randint(0, HEIGHT)

            pygame.draw.circle(screen, WHITE, (x, y), 2)

    # На определенной высоте земля уходит вниз
    if delta_y >= 180:
        earth_y += 2 + speed
    # Иначе продолжаем полет
    else:
        delta_y += 2 + speed

    speed += 0.18

    # Градиент
    if delta_y >= 180:
        if delta_r < 43:
            delta_r += 0.2

        if delta_g < 110:
            delta_g += 0.5

        if delta_b < 175:
            delta_b += 1

    # Планеты
    if delta_b > 165:
        planet1_dx += dx1
        planet1_dy += dy1

        planet2_dx += dx2
        planet2_dy += dy2

        planet3_dx += dx3
        planet3_dy += dy3

        if (planet1_y + planet1_dy - planet_r * k1 >= HEIGHT or
                planet1_x + planet1_dx - planet_r * k1 >= WIDTH or
                planet1_x + planet1_dx + planet_r * k1 <= 0):
            planet1_x = rnd.randint(-planet_r, WIDTH + planet_r)
            planet1_y = - planet_r
            k1 = rnd.uniform(0.7, 1.5)
            planet1_dx = 0
            planet1_dy = 0
            dx1 = rnd.uniform(-1.5, 1.5)
            dy1 = rnd.uniform(0.4, 2)

        if (planet2_y + planet2_dy - planet_r * k2 >= HEIGHT or
                planet2_x + planet2_dx - planet_r * k2 >= WIDTH or
                planet2_x + planet2_dx + planet_r * k2 <= 0):
            planet2_x = rnd.randint(-planet_r, WIDTH + planet_r)
            planet2_y = - planet_r
            k2 = rnd.uniform(0.7, 1.5)
            planet2_dx = 0
            planet2_dy = 0
            dx2 = rnd.uniform(-1.5, 1.5)
            dy2 = rnd.uniform(0.4, 2)

        if (planet3_y + planet3_dy - planet_r * k3 >= HEIGHT or
                planet3_x + planet3_dx - planet_r * k3 >= WIDTH or
                planet3_x + planet3_dx + planet_r * k3 <= 0):
            planet3_x = rnd.randint(-planet_r, WIDTH + planet_r)
            planet3_y = - planet_r
            k3 = rnd.uniform(0.7, 1.5)
            planet3_dx = 0
            planet3_dy = 0
            dx3 = rnd.uniform(-1.5, 1.5)
            dy3 = rnd.uniform(0.4, 2)

    # Пламя
    flame1_dy1 = rnd.randint(15, 30)
    flame1_dy2 = rnd.randint(8, 25)
    flame1_dy3 = rnd.randint(8, 20)
    flame1_dy4 = rnd.randint(15, 35)

    flame2_dy1 = flame1_dy1 - rnd.randint(5, 10)
    flame2_dy2 = flame1_dy2 - rnd.randint(5, 10)
    flame2_dy3 = flame1_dy3 - rnd.randint(5, 10)
    flame2_dy4 = flame1_dy4 - rnd.randint(5, 10)

    # НЛО
    if delta_b > 165:
        ufo_dx += dxu
        ufo_dy += dyu

        if ufo_x + ufo_dx >= WIDTH or ufo_x + ufo_dx + ufo_width <= 0 or\
            ufo_y + ufo_dy - ufo_r>= HEIGHT or ufo_y + ufo_dy + ufo_height<= 0:
            ufo_x = rnd.randint(0, WIDTH)
            flag = rnd.randint(0, 2)
            if flag == 0:
                ufo_y = - ufo_height
            else:
                ufo_y = HEIGHT + ufo_r
            ufo_dx = 0
            ufo_dy = 0
            dxu = rnd.uniform(-1.5, 1.5)
            dyu = rnd.uniform(-2, 2)

    # Обновляем окно
    pygame.display.update()

    # Задержка
    clock.tick(FPS)

