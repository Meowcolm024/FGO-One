from config import screenshot_path
from recovery.Recovery import Recovery
from recovery.panel import *
from util.cvs import check


def recover_ap():
    # initialize parameters
    sh = screenshot_path
    threshold = 0.9
    recover_scenes = [apple, decide]
    for recover_scene in recover_scenes:
        recover_path = f"./assets/scene/{recover_scene}.png"
        if check(sh, recover_path, threshold) == 1:
            recovery_interface = Recovery()
            recovery_interface.scene = sh
            recovery_interface.recover()
            return recovery_interface.done
