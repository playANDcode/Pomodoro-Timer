# Pomodoro
from playsound import playsound
import time

def timer(t, state):
    print(f"{state} starting now :D")
    try:
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
        print("\n   ")
    except KeyboardInterrupt:
        print("\n   ")

def work(t=1500):
    # 25 Minute Timer
    timer(t, 'Work')
    sound_start =  'D:/Notification Sounds/Pomodoro/echoed-ding-459.mp3'
    playsound(sound_start, False)

def _break(t=300):
    # 5 Minute Timer
    timer(t, 'Break')
    sound_break =  'D:/Notification Sounds/Pomodoro/here-i-am-449.mp3'
    playsound(sound_break, False)


while True:
    work()
    _break()



