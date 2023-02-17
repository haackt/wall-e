import pygame

pygame.mixer.init()

# This function plays a sound file from the sounds folder


def play(filename):
    pygame.mixer.music.load(f'./sounds/{filename}.wav')
    pygame.mixer.music.play()
