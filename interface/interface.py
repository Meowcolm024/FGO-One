from interface.Battle import *
from interface.scene import *
from interface.Basic import *
from interface.Support import *
from util.cvs import check
from config import screenshot_path


def recognize():

    sh = screenshot_path

    # recognize normal interface
    basic_scenes = [checkpoint_scene, standby_scene, attack_scene]
    for basic_scene in basic_scenes:
        basic_path = f"./assets/scene/{basic_scene}.png"
        if check(sh, basic_path, 0.9) == 1:
            basic_interface = Basic()
            basic_interface.scene = basic_path
            basic_interface.get_button(sh)
            print("Buttons: ", basic_interface.btn_crd)
    # recognize battle interface
    for battle_scene in battle_scenes:
        battle_path = f"./assets/battle/{battle_scene}.png"
        if check(sh, battle_path, 0.9) == 1:
            battle_interface = Battle()
            battle_interface.get_cards()
            print("Cards: ", battle_interface.card_crd)
            break
    # recognize support servant interface
    support_path = f"./assets/scene/{support_scene}.png"
    if check(sh, support_path, 0.9) == 1:
        support_interface = Support()
        support_interface.select_support(sh)
        print("Position: ", support_interface.crd)

