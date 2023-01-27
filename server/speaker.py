from playsound import playsound


def play(filename):
    playsound(f'./sounds/{filename}.wav')
