# @Time:2023/5/13 11:24
# @Author: 一只流浪的蚊子
# @File:alien_invasion.py
# 第三方库
import pygame
from pygame.sprite import Group
# 自写库
from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien
from game_stats import GameStats
from button import Button


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))  # 创建一个窗口
    pygame.display.set_caption("Alien Invasion")  # 设置窗口标题

    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建一个外星人编组
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings, ship, screen, aliens)

    # 开始游戏的主循环
    while True:
        # 监控键盘和鼠标事件
        gf.check_events(ai_settings, aliens, bullets, screen, ship, stats, play_button)
        # 更新游戏元素的移动
        if stats.game_active:
            ship.update()
            gf.update_bullets(aliens, ai_settings, screen, ship, bullets)
            gf.update_aliens(ai_settings, ship, stats, screen, bullets, aliens)

        # 更新屏幕
        gf.update_screen(ai_settings, screen, stats, ship, bullets, aliens, play_button)


if __name__ == '__main__':
    run_game()
