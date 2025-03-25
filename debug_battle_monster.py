import struct
import json

def read_debug_battle_monster(file_path,output_path):
    try:
        with open(file_path, "rb") as f:
            f.seek(0x14)  
            monster_data = []
            while True:
                data = f.read(0x20)  
                if len(data) != 0x20:
                    break  

                unpacked = struct.unpack(
                    "<LLHHHHHHH"  
                    + "BBBBBBcBBB",  
                    data
                )
                
                monster = {
                    "maxHp": unpacked[0],
                    "maxMp": unpacked[1],
                    "monsterID": unpacked[2],
                    "action1": unpacked[3],
                    "action2": unpacked[4],
                    "action3": unpacked[5],
                    "action4": unpacked[6],
                    "action5": unpacked[7],
                    "action6": unpacked[8],
                    "brain": unpacked[9],
                    "member": unpacked[10],
                    "hp": unpacked[11],
                    "mp": unpacked[12],
                    "pattern": unpacked[13],
                    "condition": unpacked[14],
                    "byte_1": unpacked[15].hex(),
                    "dummy0": unpacked[16],
                    "dummy1": unpacked[17],
                    "dummy2": unpacked[18],
                }

                monster_data.append(monster)
        
        with open(output_path, "w") as f_output:
            json.dump(monster_data, f_output, indent=4)

    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

file_path = "./LEVELDATA/debug_battle_monster.dat"
output_path = "./data/debug_battle_monster.json"

read_debug_battle_monster(file_path,output_path)
