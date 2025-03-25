import struct
import json


def read_action_type(file_path,output_path):
    try:
        action_data = []
        with open(file_path, "rb") as f:
            f.seek(0x14)  
            while True:
                data = f.read(0x8)  

                if len(data) != 0x8:
                    break  

                unpacked = struct.unpack("<BBBccBBB", data)

                action = {
                    "turn": unpacked[0],
                    "typeID": unpacked[1],
                    "pattern": unpacked[2],
                    "byte_1": unpacked[3].hex(),
                    "byte_2": unpacked[4].hex(),
                    "dummy0": unpacked[5],
                    "dummy1": unpacked[6],
                    "dummy2": unpacked[7],
                   
                }

                action_data.append(action) 

        with open(output_path, "w") as f_output:
            json.dump(action_data, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_action_type.dat"
output_path = "./data/dq5ds_action_type.json"
read_action_type(file_path,output_path)
