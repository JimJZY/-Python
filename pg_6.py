import pygame
import sys
from pygame.locals import *

#初始化Pygame
pygame.init()

size = width,height = 800,800
bg = (255,255,255)

fullscreen = False

#创建指定大小的窗口 Surface
screen = pygame.display.set_mode(size,RESIZABLE)
#设置窗口标题
pygame.display.set_caption("初次见面，请大家多多关照!")

#设置放大缩小的比率
ratio = 1.0


#加载图片
oturtle = pygame.image.load("比卡丘.jfif")
turtle = oturtle
#获得图像的位置矩形
oturtle_rect = oturtle.get_rect()
position = turtle_rect = oturtle_rect

speed = [5,0]
turtle_right = pygame.transform.rotate(turtle,90)
turtle_top = pygame.transform.rotate(turtle,180)
turtle_left = pygame.transform.rotate(turtle,270)
turtle_bottom = turtle
turtle = turtle_top

l_head = turtle
r_head = pygame.transform.flip(turtle,True,False)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == KEYDOWN:
            #全屏（F11）
            if event.key == K_F11:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((1024,768),FULLSCREEN|HWSURFACE)
                    width,height = 1024,768
                else:
                    screen = pygame.display.set_mode(size)

            #放大、缩小比卡丘(=、-),空格键恢复原始尺寸
            if event.key == K_EQUALS or event.key == K_MINUS or event.key == K_SPACE:
                #最大只能放大一倍，缩小50%
                if event.key == K_EQUALS and ratio < 2:
                    ratio += 0.1
                if event.key == K_MINUS and ratio > 0.5:
                    ratio -= 0.1
                if event.key == K_SPACE:
                    ratio = 1.0

                turtle = pygame.transform.smoothscale(oturtle,\
                                             (int(oturtle_rect.width * ratio),\
                                             int(oturtle_rect.height * ratio)))

                l_head = turtle
                r_head = pygame.transform.flip(turtle,True,False)

        #用户调整窗口尺寸
        if event.type == VIDEORESIZE:
            size = event.size
            width,height = size
            print(size)
            screen = pygame.display.set_mode(size,RESIZABLE)
            

    #移动图像
    position = position.move(speed)
    if position.right > width:
        turtle = turtle_right
        position = turtle_rect = turtle.get_rect()
        position.left = width - turtle_rect.width
        speed = [0,5]
    if position.bottom > height:
        turtle = turtle_bottom
        position = turtle_rect = turtle.get_rect()
        position.left = width - turtle_rect.width
        position.top = height - turtle_rect.height
        speed = [-5,0]

    if position.left < 0:
        turtle = turtle_left
        position = turtle_rect = turtle.get_rect()
        position.top = height - turtle_rect.height
        speed = [0,-5]

    if position.top < 0:
        turtle = turtle_top
        position = turtle_rect = turtle.get_rect()
        speed = [5,0]
        
    #填充背景
    screen.fill(bg)
    #更新图像
    screen.blit(turtle,position)
    #更新界面
    pygame.display.flip()
    #延迟10ms
    pygame.time.delay(10)
            
