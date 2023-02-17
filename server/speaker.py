import pygame

pygame.mixer.init()

# This function plays a sound file from the sounds folder


def play(filename):
    pygame.mixer.music.load(f'/home/wall-e/wall-e/server/sounds/{filename}.wav')
    pygame.mixer.music.play()
