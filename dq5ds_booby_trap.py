import struct
import json

def read_booby_trap(file_path, output_path):
    try:
        booby_data = []
        with open(file_path, "rb") as f:
            f.seek(0x14)  
            while True:
                data = f.read(0x8)  

                if len(data) != 0x8:
                    break  

                unpacked = struct.unpack("<4H", data)

                booby = {
                    "index": unpacked[0],  
                    "placeRight": unpacked[1],  
                    "placeLeft": unpacked[2],  
                    "floor": unpacked[3],  
                }

                booby_data.append(booby)

        with open(output_path, "w") as f_output:
            json.dump(booby_data, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

file_path = "./LEVELDATA/dq5ds_booby_trap.dat"
output_path = "./data/dq5ds_booby_trap.json"
read_booby_trap(file_path, output_path)