import ast
import json
import os

from winreg import *

class UnlockerRegistryHandler:
    def __init__(self):
        self.parent     = r"SOFTWARE\\Cognosphere\\Star Rail"
        self.path       = ""
        self.patched    = False
        self.patchable  = True
        self.config     = {
            "FPS": 120,
            "EnableVSync": False,
            "RenderScale":  1.0,
            "ResolutionQuality": 1,
            "ShadowQuality": 0,
            "LightQuality": 1,
            "CharacterQuality": 1,
            "EnvDetailQuality": 1,
            "ReflectionQuality": 1,
            "BloomQuality": 0,
            "AAMode": 0,
        }
        self.registry   = ("", b'')
        self.hKey       = None

    def find_data(self):
        self.hKey = OpenKeyEx(HKEY_CURRENT_USER, self.parent, 0, KEY_ALL_ACCESS)

        index = 0

        while 'graphicssettings_model' not in self.registry[0].lower():
            self.registry = EnumValue(self.hKey, index)

            index += 1

    def patch_game(self):
        organised = str(self.config)\
                        .replace("\t", "")\
                        .replace(" ", "")\
                        .replace("'", '"')\
                        .replace("False", "false")\
                        .replace("True", "true")

        binary = bytes(organised, 'utf-8') + b'\x00'

        SetValueEx (
            self.hKey, 
            self.registry[0], 
            0, 
            REG_BINARY,
            binary
        )

        print("--> [UNLOCKER]: SUCCESSFULLY UNLOCKED 60FPS CAP --> 120FPS !!!")
        
        if input("\nPRESS [ENTER] TO CLOSE WINDOW...") is not None:
            exit(0)

    def start(self):
        self.find_data()

        if self.registry == ("", b''):
            self.patchable = False
            
            return

        dictionary = json.loads(self.registry[1].rstrip(b"\x00").decode())

        for key in dictionary.keys():
            if key == "FPS":
                continue

            self.config[key] = dictionary[key]

        self.patch_game()


