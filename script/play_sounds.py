import pygame

pygame.init()

pygame.mixer.music.set_volume(0.1)
shoot = pygame.mixer.Sound("music/shoot.wav")
kill = pygame.mixer.Sound("music/kill.wav")
death = pygame.mixer.Sound("music/death.wav")
gameover = pygame.mixer.Sound("music/gameover.mp3")
play = pygame.mixer.Sound("music/play.mp3")

