import struct
import json

def read_chara_data(file_path, output_path):
    try:
        chara_data = []
        with open(file_path, "rb") as f:
            f.seek(0x14)  
            while True:
                data = f.read(0x8)  

                if len(data) != 0x8:
                    break  

                unpacked = struct.unpack("<HBBcBBB", data)

                chara = {
                    "index": unpacked[0],  
                    "height": unpacked[1],  
                    "width": unpacked[2],  
                    "byte_1": unpacked[3].hex(),  
                    "dummy0": unpacked[4],  
                    "dummy1": unpacked[5],  
                    "dummy2": unpacked[6],  
                }

                chara_data.append(chara)

        with open(output_path, "w") as f_output:
            json.dump(chara_data, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

file_path = "./LEVELDATA/dq5ds_chara_data.dat"
output_path = "./data/dq5ds_chara_data.json"
read_chara_data(file_path, output_path)