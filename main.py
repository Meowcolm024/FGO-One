from interface.interface import *
from recovery.recover import *
from config import recovery_times, run_time
from util.ats import screenshot

times = recovery_times
play = run_time

f = open('log.txt', 'w')
st = '[MAIN] MAX APPLES: ' + str(times) + '\r' + '[MAIN] MAX TIMES: ' + str(play) + '\r'
f.write(st)
f.close()

while times >= 0:

    time.sleep(0.2)
    screenshot()
    end = recognize()

    if play == "inf":

        ap = recover_ap()
        if ap == 1 and times != 0:
            continue
        elif ap == 1 and times == 0:
            apa = '[MAIN] Out of AP!'
            output_log(apa)
            break
        elif ap == 2:
            times = times - 1
            out = '[MAIN] Apples left: ' + str(times)
            output_log(out)
            time.sleep(2)

    elif play != "inf":

        if end == "end":
            play = play - 1
            pl = '[MAIN] Times left: ' + str(play)
            output_log(pl)

        ap = recover_ap()
        if ap == 1 and times != 0:
            continue
        elif ap == 1 and times == 0:
            apb = '[MAIN] Out of AP!'
            output_log(apb)
            break
        elif ap == 2:
            times = times - 1
            out = '[MAIN] Apples left: ' + str(times)
            output_log(out)
            time.sleep(2)

    if play == 0:
        break

endnote = '[MAIN] FINISHED'
output_log(endnote)
