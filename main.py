import pygame
from things import Circle
from factories import ParticleFactory
from systems import CollisionManager
import numpy as np
import time


# 设置
WIDTH = 800
HEIGHT = 600
DT = 1
BLACK = (0, 0, 0)
COLD_GREY = (202,235,216)
N_PARTICLES = 100
INIT_V_MU = [0, 0]
INIT_V_SIGMA = np.eye(2) * 10
FPS = 60
BACKGROUND_COLOR = COLD_GREY

# 初始设置
pygame.init() # 初始化pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Pygame窗口
pygame.display.set_caption("粒子碰撞系统") # 标题
keep_going = True
clock = pygame.time.Clock()
t = time.time()

# 游戏循环
circles = [ParticleFactory.random_circle(0, WIDTH, 0, HEIGHT, INIT_V_MU, INIT_V_SIGMA) \
           for i in range(N_PARTICLES)]

while keep_going:
    for event in pygame.event.get():  # 遍历事件
        if event.type == pygame.QUIT:  # 退出事件
            keep_going = False

    # 绘制
    screen.fill(BACKGROUND_COLOR)
    for c in circles:
        c.draw(screen)

    # 更新
    CollisionManager.collide(circles, WIDTH, HEIGHT)
    for c in circles:
        c.update(DT)

    # 刷新屏幕
    pygame.display.update()

    clock.tick(FPS)
    # print(time.time() - t)
    # t = time.time()

# 退出程序
pygame.quit()