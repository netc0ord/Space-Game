import pygame
import pygame.font
import sys
from script.bullet import Bullet
from script.ino import Ino
import time
from script import play_sounds as music


def events(screen, gun, bullets):

    """Обработка событий"""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                gun.mright = True
            elif event.key == pygame.K_LEFT:
                gun.mleft = True
            elif event.key == pygame.K_UP:
                gun.mtop = True
            elif event.key == pygame.K_DOWN:
                gun.mbottom = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
                music.shoot.play()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                gun.mright = False
            elif event.key == pygame.K_LEFT:
                gun.mleft = False
            elif event.key == pygame.K_UP:
                gun.mtop = False
            elif event.key == pygame.K_DOWN:
                gun.mbottom = False


def update(bg_color, screen, sc, gun, inos, bullets):
    screen.fill(bg_color)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    inos.draw(screen)
    pygame.display.flip()


speed = 0


def update_bullets(inos, bullets, screen, stats, sc):
    """Обновление позиций пуль"""
    bullets.update()
    global speed
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, inos, True, True)
    if collisions:
        for inos in collisions.values():
            stats.score += 1 * len(inos)
            music.kill.play()
        sc.image_score()
        check_high_score(stats, sc)
        sc.image_guns()

    if len(inos) == 0:
        bullets.empty()
        speed += 0.008
        create_army(screen, inos, speed)


def gun_kill(stats, screen, sc, gun, inos, bullets):
    """Столкновение пушки и пришельцев"""
    global speed
    if stats.guns_left > 1:
        stats.guns_left -= 1
        music.death.play()
        sc.image_guns()
        inos.empty()
        bullets.empty()
        create_army(screen, inos, speed)
        gun.create_gun()
        time.sleep(0.5)
    else:
        stats.guns_left -= 1
        sc.image_guns()
        stats.run_game = False
        music.gameover.play()


flag_move = 0


def update_inos(stats, screen, sc, gun, inos, bullets):
    global flag_move
    flag_move += 0.001
    if flag_move <= 1.5:
        inos.update(True)
    elif (flag_move > 1.5) and (flag_move <= 3.0):
        inos.update(False)
    else:
        flag_move = 0
    if pygame.sprite.spritecollideany(gun, inos):
        gun_kill(stats, screen, sc, gun, inos, bullets)
    inos_check(stats, screen, sc, gun, inos, bullets)


def inos_check(stats, screen, sc, gun, inos, bullets):
    """Проверка пересечения границы пришельцами"""
    screen_rect = screen.get_rect()
    for ino in inos.sprites():
        if ino.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, sc, gun, inos, bullets)
            break


def create_army(screen, inos, speed):
    """Создание армии пришльцев"""
    ino = Ino(screen, speed)
    ino_width = ino.rect.width
    number_ino_x = int((700 - 2 * ino_width) / ino_width)
    ino_height = ino.rect.height
    number_ino_y = int((800 - 100 - 2 * ino_height) / ino_height)

    for row_number in range(number_ino_y - 5):
        for ino_number in range(number_ino_x):
            ino = Ino(screen, speed)
            ino.x = ino_width + (ino_width * ino_number) - 13
            ino.y = ino_height + (ino_height * row_number) + 10
            ino.rect.x = ino.x
            ino.rect.y = ino.y
            inos.add(ino)


def check_high_score(stats, sc):
    """Проверка новых рекордов"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open("script/high_score.txt", "w") as f:
            f.write(str(stats.high_score))


def restart(screen):
    gameover = pygame.image.load("image/gameover.png")
    screen.blit(gameover, (0, 0))
    font = pygame.font.SysFont(None, 36)
    restart_text = font.render("RESTART", True, (145, 142, 145), (0, 0, 0))
    restart_rect = restart_text.get_rect()
    x = screen.get_rect().centerx
    y = screen.get_rect().centery+80
    restart_rect.centerx = x
    restart_rect.centery = y
    screen.blit(restart_text, restart_rect)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and restart_rect.left <= event.pos[0] <= restart_rect.right and \
                    restart_rect.top <= event.pos[1] <= restart_rect.bottom:
                return True


