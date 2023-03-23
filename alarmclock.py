from playsound import playsound

import time

CLEAR ="\033[2J]"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elapsed = 0
    
    print(CLEAR)
    
    while time_elapsed< seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left=seconds-time_elapsed
        minutes_left=time_left//60
        seconds_left=time_left%60
        
        print(f"{CLEAR_AND_RETURN}Time left: {minutes_left:02d} minutes and {seconds_left:02d} seconds")
        
    playsound("alarm.mp3")    
    
    
minutes=int(input("Enter minutes to wait: "))
seconds=int(input("Enter seconds to wait: "))

total_seconds=minutes*60+seconds

alarm(total_seconds)