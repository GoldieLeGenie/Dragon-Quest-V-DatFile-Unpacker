import struct
import json

def read_battle_map(file_path, output_path):
    try:
        battle_map_data = []
        with open(file_path, "rb") as f:
            f.seek(0x14)  
            while True:
                data = f.read(0x14)  

                if len(data) != 0x14:
                    break  
                unpacked = struct.unpack("<BBBB12sBBBB", data)

                maps = {
                    "R": unpacked[0],  # u_char R
                    "G": unpacked[1],  # u_char G
                    "B": unpacked[2],  # u_char B
                    "mapIndex": unpacked[3],  # u_char mapIndex
                    "map": unpacked[4].decode('utf-8').strip('\x00'),  
                    "byte_1": unpacked[5],  # char byte_1
                    "dummy0": unpacked[6],  # u_char dummy0
                    "dummy1": unpacked[7],  # u_char dummy1
                    "dummy2": unpacked[8],  # u_char dummy2
                }

                battle_map_data.append(maps)

        with open(output_path, "w") as f_output:
            json.dump(battle_map_data, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

file_path = "./LEVELDATA/dq5ds_battle_map.dat"
output_path = "./data/dq5ds_battle_map.json"
read_battle_map(file_path, output_path)