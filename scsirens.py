from playsound import playsound

Siren_01 = './Sirens/Siren-01.wav'
Siren_02 = './Sirens/Siren-02.mp3'
Siren_03 = './Sirens/Siren-03.mp3'
Siren_04 = './Sirens/Siren-04.mp3'


def alarm(magnitude):
    print('Earthquake magnitude:', magnitude)
    if magnitude < 3:
        playsound(Siren_01)
    elif 3 <= magnitude < 5:
        playsound(Siren_02)
    elif 5 <= magnitude < 7:
        playsound(Siren_04)
    elif 7 <= magnitude:
        playsound(Siren_03)

if __name__=='__main__':
    alarm(2)
    alarm(4)
    alarm(6)
    alarm(8)