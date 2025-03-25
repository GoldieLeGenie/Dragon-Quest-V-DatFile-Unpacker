import struct
import json

def read_furniture_list(file_path, output_path):
    try:
        furniture_list_data = []
        with open(file_path, "rb") as f:
            f.seek(0x14)
            while True:
                data = f.read(0x4)  

                if len(data) != 0x4:
                    break  #

                unpacked = struct.unpack("<L", data)  

                furniture_entry = {
                    "floor": unpacked[0]
                }

                furniture_list_data.append(furniture_entry)

        with open(output_path, "w") as f_output:
            json.dump(furniture_list_data, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

file_path = "./LEVELDATA/dq5ds_furniture_list.dat"
output_path = "./data/dq5ds_furniture_list.json"
read_furniture_list(file_path, output_path)
