# @Time:2023/5/13 12:26
# @Author: 一只流浪的蚊子
# @File:settings.py

class Settings():
    """存储所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_speed_factor = 1
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed_factor = 3
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # 外星人设置
        self.alien_speed_factor = 0.08
        self.fleet_drop_speed = 50
        self.fleet_direction = 1  # 1表示向右移动，-1表示向左移动
        