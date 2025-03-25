import struct
import json


def read_action(file_path,output_path):
    try:
        action_data = []
        with open(file_path, "rb") as f:
            f.seek(0x14)  
            while True:
                data = f.read(0x40)  

                if len(data) != 0x40:
                    break  

                unpacked = struct.unpack("<7L10H8B7cB", data)

                action = {
                    "actionMes": unpacked[0],
                    "playerSuccess": unpacked[1],
                    "monsterSuccess": unpacked[2],
                    "playerFailed": unpacked[3],
                    "monsterFailed": unpacked[4],
                    "endMes": unpacked[5],
                    "menuMes": unpacked[6],
                    "index": unpacked[7],
                    "effectFriend": unpacked[8],
                    "effectEnemy": unpacked[9],
                    "effectLap": unpacked[10],
                    "MonsterMin": unpacked[11],
                    "MonsterMax": unpacked[12],
                    "PlayerMin": unpacked[13],
                    "PlayerMax": unpacked[14],
                    "actionSE": unpacked[15],
                    "startSE": unpacked[16],
                    "type": unpacked[17],
                    "magictype2": unpacked[18],
                    "useMP": unpacked[19],
                    "fool": unpacked[20],
                    "human": unpacked[21],
                    "god": unpacked[22],
                    "typeID": unpacked[23],
                    "magictype": unpacked[24],
                    "byte_1": unpacked[25].hex(),
                    "byte_2": unpacked[26].hex(),
                    "byte_3": unpacked[27].hex(),
                    "byte_4": unpacked[28].hex(),
                    "byte_5": unpacked[29].hex(),
                    "byte_6": unpacked[30].hex(),
                    "byte_7": unpacked[31].hex(),
                    "dummy0": unpacked[32],
                   
                }

                action_data.append(action) 

        with open(output_path, "w") as f_output:
            json.dump(action_data, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

file_path = "./LEVELDATA/dq5ds_action.dat"
output_path = "./data/dq5ds_action.json"
read_action(file_path,output_path)
