"""initialize different scenes of interfaces"""
from config import checkpoint

# basic interface, which requires tapping ONE button
basic_scenes = [checkpoint, "standby", "attack", "win", "mistake"]

# the support interface, which requires random tapping
support_scene = "support"

# the battle interface, which needs to select cards
battle_scenes = ["quick", "arts", "buster"]

# the post-battle interface, which needs to tap on special location
finish_scenes = ["bond", "master"]

# the loading/fighting interface, random tap and swipe to avoid being ban
loading_scenes = ["loading", "fighting"]
