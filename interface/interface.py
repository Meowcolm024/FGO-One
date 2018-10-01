from interface.Battle import *
from interface.scene import *
from interface.Basic import *
from interface.Support import *
from interface.Finish import *
from interface.Loading import *
from util.cvs import check
from config import screenshot_path


def recognize():
    # initialize parameters
    sh = screenshot_path
    threshold = 0.9
    # recognize normal interface
    for basic_scene in basic_scenes:
        basic_path = f"./assets/scene/{basic_scene}.png"
        if check(sh, basic_path, threshold) == 1:
            basic_interface = Basic()
            basic_interface.scene = basic_path
            basic_interface.sh = sh
            basic_interface.get_button()
            print("Buttons: ", basic_interface.btn_crd)
            return
    # recognize battle interface
    for battle_scene in battle_scenes:
        battle_path = f"./assets/battle/{battle_scene}.png"
        if check(sh, battle_path, threshold) == 1:
            battle_interface = Battle()
            battle_interface.get_cards()
            print("Cards: ", battle_interface.card_crd)
            return
    # recognize support servant interface
    support_path = f"./assets/scene/{support_scene}.png"
    if check(sh, support_path, threshold) == 1:
        support_interface = Support()
        support_interface.scene = sh
        support_interface.select_support()
        print("Position: ", support_interface.crd)
        return
    # recognize finish interface
    for finish_scene in finish_scenes:
        finish_path = f"./assets/scene/{finish_scene}.png"
        if check(sh, finish_path, threshold) == 1:
            finish_interface = Finish()
            finish_interface.scene = sh
            finish_interface.pass_finish()
            return
    # recognize loading/in-battle interface
    for loading_scene in loading_scenes:
        loading_path = f"./assets/scene/{loading_scene}.png"
        if check(sh, loading_path, threshold) == 1:
            loading_interface = Loading()
            loading_interface.scene = sh
            loading_interface.mark = loading_scene
            loading_interface.have_fun()
