from playsound import playsound

# This function plays a sound file from the sounds folder


def play(filename):
    playsound(f'sounds/{filename}.wav')
