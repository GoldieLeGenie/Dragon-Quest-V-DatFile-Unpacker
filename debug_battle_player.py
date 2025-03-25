import struct
import json


def read_debug_battle_player(file_path,output_path):
    try:
        player_data = []
        with open(file_path, "rb") as f:
            f.seek(0x14)  
            while True:
                data = f.read(0x24)  

                if len(data) != 0x24:
                    break  

                unpacked = struct.unpack("<13H9Bc", data)

                player = {
                    "accessary3": unpacked[0],
                    "item2": unpacked[1],
                    "item3": unpacked[2],
                    "item4": unpacked[3],
                    "item5": unpacked[4],
                    "item1": unpacked[5],
                    "weapon": unpacked[6],
                    "armor": unpacked[7],
                    "shield": unpacked[8],
                    "helm": unpacked[9],
                    "accessary1": unpacked[10],
                    "plusAction": unpacked[11],
                    "accessary2": unpacked[12],
                    "playerID": unpacked[13],
                    "level": unpacked[14],
                    "hp": unpacked[15],
                    "mp": unpacked[16],
                    "condition": unpacked[17],
                    "tactics": unpacked[18],
                    "byte_1": unpacked[19],
                    "dummy0": unpacked[20],
                    "dummy1": unpacked[21],
                    "dummy2": unpacked[22].hex(),
                }

                player_data.append(player) 

        with open(output_path, "w") as f_output:
            json.dump(player_data, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

file_path = "./LEVELDATA/debug_battle_player.dat"
output_path = "./data/debug_battle_player.json"
read_debug_battle_player(file_path,output_path)
