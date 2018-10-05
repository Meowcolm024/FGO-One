from interface.interface import *
from recovery.recover import *
from config import recovery_times, run_time
from util.ats import screenshot

times = recovery_times
play = run_time

while times >= 0:
    time.sleep(0.2)
    screenshot()
    end = recognize()
    if play == "inf":
        ap = recover_ap()
        if ap == 1 and times != 0:
            continue
        elif ap == 1 and times == 0:
            break
        elif ap == 2:
            times = times - 1
    elif end == "end":
        play = play - 1
        ap = recover_ap()
        if ap == 1 and times != 0:
            continue
        elif ap == 1 and times == 0:
            break
        elif ap == 2:
            times = times - 1
    if play == 0:
        break
