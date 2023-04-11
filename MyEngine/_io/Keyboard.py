from pygame import key as pykey
import pygame as pg

from .._utils.BaseModule.LogError import logerror

logerror.load_core("Engine")

class Keyboard:
    
    def on_press(self, key: str, function = None, *args, **kwargs) -> bool:
        keys = pykey.get_pressed()
        key = key.lower()

        data_simbls = { 
            8:   "backspace",
            9:   "tab",
            13:  "return",
            27:  "escape",
            32:  "space",
            33:  "!",
            34:  "\"",
            35:  "#",
            36:  "$",
            37:  "%",
            38:  "&",
            39:  "'",
            40:  "(",
            41:  ")",
            42:  "*",
            43:  "+",
            44:  ",",
            45:  "-",
            46:  ".",
            47:  "/",
            48:  "0",
            49:  "1",
            50:  "2",
            51:  "3",
            52:  "4",
            53:  "5",
            54:  "6",
            55:  "7",
            56:  "8",
            57:  "9",
            58:  ":",
            59:  ";",
            60:  "<",
            61:  "=",
            62:  ">",
            63:  "?",
            64:  "@",
            91:  "[",
            92:  "\\",
            93:  "]",
            94:  "^",
            95:  "_",
            96:  "`",
            97:  "a",
            98:  "b",
            99:  "c",
            100: "d",
            101: "e",
            102: "f",
            103: "g",
            104: "h",
            105: "i",
            106: "j",
            107: "k",
            108: "l",
            109: "m",
            110: "n",
            111: "o",
            112: "p",
            113: "q",
            114: "r",
            115: "s",
            116: "t",
            117: "u",
            118: "v",
            119: "w",
            120: "x",
            121: "y",
            122: "z",
            127: "delete",
            1073741882: "f1",
            1073741883: "f2",
            1073741884: "f3",
            1073741885: "f4",
            1073741886: "f5",
            1073741887: "f6",
            1073741888: "f7",
            1073741889: "f8",
            1073741890: "f9",
            1073741891: "f10",
            1073741892: "f11",
            1073741893: "f12",
            1073741903: "right",
            1073741904: "left",
            1073741905: "down",
            1073741906: "up",

            1073742048: "left ctrl",
            1073742049: "left shift",
            1073742050: "left alt",
            1073742052: "right ctrl",
            1073742053: "right shift",
            1073742054: "right alt",
        }
        data_simbls_encode = {data_simbls[x]: x for x in data_simbls}

        if key not in data_simbls_encode:
            meen_keys = []
            for key_ in data_simbls_encode:
                for _, simble in enumerate(key):
                    if key_.find(simble) != -1:
                        meen_keys.append(key_)
            meen_keys = list(set(meen_keys))
            logerror.crit(f"Don't find key '{key}' do you meen {' or '.join(meen_keys)}?")


        if keys[data_simbls_encode[key]]:
            if function is not None:
                function(*args, **kwargs)
            return True
        
        return False