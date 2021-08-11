from playsound import playsound
import time
import os
import random as rndm

"""
Todo:
- Add an exception error in soundfile_directories() when soundfile isn't discovered
    - Notify the user about the error
- It would be nice to let the program scan for sound files first
    - If sound files exists then :D
    - If not, then the timer will go into silent mode
- Compact the name of soundfile_directories()
- Add a restart in menu/pause to restart the cycle of pomodoro
    - Notify the user how many left before long break
    - Make the user confirm the restart of cycle
"""

def soundfile_directories(filename: str):
    # Automatically adapts whatever operating system or folder directory;
    # ; As long as files are in 'Sounds' directory and you're running cmd in pomodoro folder

        path = os.path.join(os.getcwd(),'Sounds',filename + '.mp3')
        return path
def seconds_to_minutes(s: int) -> str:
    mins = s // 60
    secs = s % 60
    return '{:02d}:{:02d}'.format(mins, secs)
                        
def timer_with_menu(t: int):
    # Inputs must be in seconds format
    while t: # while t > 0 for clarity 
        try:
            timer = seconds_to_minutes(t)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
            # Bug:
            # Description: While these timer specifically try block is running, inputs gets recorded;
            # ;The recorded inputs then transfers to the "except block"
            # Replicate: While timer is running, press keys in the keyboard randomly
        except KeyboardInterrupt:
            # Menu, also acts to PAUSE the timer
            print()  # so that timer text won't get removed 
            playsound(soundfile_directories('menu'), False)
            response = input("-- Press 'enter' to unpause \
                            \n-- Type s to skip timer \
                            \n-- Type e to close program \
                            \n-- Type r to restart pomodoro\
                            \nYour Response Here: ").lower()
            if response == '':
                playsound(soundfile_directories('unpause'), False)
                continue # Unpause the timer
            elif response == 's':
                break # Skip to next timer
            elif response == 'r':
                print("These feature will be available soon...")
            elif response == 'e':
                exit()

def manual_or_not(v):
    # Waits for user response before continuing to next timer
    if v == 'm':
        playsound(soundfile_directories('manual'), False)
        input("This is manual pomodoro mode" \
            "\nPress enter to continue the timer...")

def tomato_start(mode, default_time=1500): # 1500sec is 25min
    playsound(soundfile_directories('start'), False)
    print("!! 25 Minute Timer !!".center(50))
    msg = [ "Let's go!!!", \
            "Focus time :D"]
    print(rndm.choice(msg))
    timer_with_menu(default_time)
    manual_or_not(mode)

def tomato_break(mode, default_time=300): # 300sec is 5min
    playsound(soundfile_directories('break'), False)
    print("!! 5 Minute Timer !!".center(50))
    msg = [ "Break Time! Rest your eyes or drink some water", \
            "Well done! Go standup and do some streching"]
    print(rndm.choice(msg))
    timer_with_menu(default_time)
    manual_or_not(mode)

def tomato_longbreak(mode, default_time=900): # 900sec is 15min
    playsound(soundfile_directories('longbreak'), False)
    print("!! 15 Minute Timer !!".center(50))
    msg = [ "Wow! You made it!!! Go take a rest champ"]
    print(rndm.choice(msg))
    timer_with_menu(default_time)
    manual_or_not(mode)


i = 0  # Set the increment

print("--POMODORO--".center(50))
response = input("-- a for auto pomodoro" \
               "\n-- m for manual pomodoro" \
               "\n-- h for help" \
               "\nYour Response Here: ")
if response == 'h':
    print("These feature will be available soon...")
while True:
    tomato_start(response)
    i += 1
    if i <= 3:
        tomato_break(response)
    else:
        # After 3 breaks, initiate a long break. 
        i = 0 # reset countdown
        tomato_longbreak(response)