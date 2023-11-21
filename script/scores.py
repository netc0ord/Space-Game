import pygame.font
from script.gun import Gun
from pygame.sprite import Group


class Scores():
    """Вывод очков игрока"""
    def __init__(self, screen, stats):
        """Инициализируем подсчет очков"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (145, 142, 145)
        self.font = pygame.font.SysFont(None, 36)
        self.image_score()
        self.image_high_score()
        self.image_guns()

    def image_guns(self):
        """Отображение жизней"""
        self.guns = Group()
        for gun_number in range(self.stats.guns_left):
            gun = Gun(self.screen)
            gun.image = pygame.image.load("image/health.png")
            gun.rect = gun.image.get_rect()
            gun.rect.x = 50 + gun_number * gun.rect.width
            gun.rect.y = 19
            self.guns.add(gun)


    def image_score(self):
        """Преобразовывает текст счета в граф. изображение"""
        self.score_img = self.font.render(str(f"SCORE {self.stats.score}"), True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 65
        self.score_rect.top = self.screen_rect.top + 22

    def image_high_score(self):
        """Преобразует рекор в граф. изображение"""
        self.high_score_im = self.font.render(str(f"HIGH SCORE {self.stats.high_score}"), True, self.text_color, (0, 0, 0))
        self.high_score_rect = self.high_score_im.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx + 20
        self.high_score_rect.top = self.screen_rect.top + 22

    def show_score(self):
        """Вывод счета на экран"""
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_im, self.high_score_rect)
        self.guns.draw(self.screen)

