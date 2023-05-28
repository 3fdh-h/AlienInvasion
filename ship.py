# @Time:2023/5/13 12:51
# @Author: 一只流浪的蚊子
# @File:yt.py
import pygame
from settings import Settings

class Ship():

    def __init__(self, ai_settings, screen):
        """初始化飞船并初始化其位置"""
        self.screen = screen

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.image = pygame.transform.scale(self.image, (50, 60))   # 将图片缩小
        self.rect = self.image.get_rect()  # 将元素看作矩形，直接对矩形进行操作
        self.screen_rect = screen.get_rect()  # 同上将屏幕看作矩形

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx  # 将飞船的x中心设为屏幕的中心
        self.rect.bottom = self.screen_rect.bottom  # 将飞船的底设为屏幕的底
        # 移动标志
        self.moving_right = False
        self.moving_left = False
        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)
        # 引入默认设置
        self.ai_settings = ai_settings

    def update(self):
        """根据移动标志和是否在窗口中调整飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.centerx -= self.ai_settings.ship_speed_factor

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
        # 定位用元素的外接矩形，绘制时使用元素本身

    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.center = self.screen_rect.centerx
