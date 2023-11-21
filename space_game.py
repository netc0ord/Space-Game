import pygame
from script import play_sounds as music
from script import controls
from script.gun import Gun
from pygame.sprite import Group
from script.stats import Stats
from script.scores import Scores


def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Star guardians")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    stats = Stats()
    controls.create_army(screen, inos, 0)
    sc = Scores(screen, stats)
    music.play.play()

    while True:
        controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            controls.update(bg_color, screen, sc, gun, inos, bullets)
            controls.update_bullets(inos, bullets, screen, stats, sc)
            controls.update_inos(stats, screen, sc, gun, inos, bullets)
        else:
            if controls.restart(screen):
                run()


run()

