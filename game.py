import time
import os
import keyboard

#Developing
#----------------------------------------------------------------
#Summon Pocket -- Gather resources -- Farming -- Craft -- Explore -- Battle -- Tower
#Player -- Pocket -- Monster -- Item -- Inventory
#Player = Name, List of Pockets
#Pocket = Name, Lvl, Exp, Exp_max, HP, HP_max, Damage, Skill
#Monster = Name, Lvl, Damage, HP, HP_max, Skill
#Item = Name, Effect, Quantity
#Inventory = Name, Equip, Quantity


def clear():
    os.system("cls" if os.name == "nt" else "clear")