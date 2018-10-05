from interface.interface import *
from recovery.recover import *
from config import recovery_times
from util.ats import screenshot

times = recovery_times

while times >= 0:
        time.sleep(0.2)
        screenshot()
        recognize()
        ap = recover_ap()
        if ap == 1 and times != 0:
            continue
        elif ap == 1 and times == 0:
            break
        elif ap == 2:
            times = times - 1
