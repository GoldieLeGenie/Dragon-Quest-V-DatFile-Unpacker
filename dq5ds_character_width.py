import struct
import json

def read_character_width(file_path, output_path):
    try:
        character_width_data = []
        with open(file_path, "rb") as f:
            f.seek(0x14)  
            while True:
                data = f.read(0x1C)  

                if len(data) != 0x1C:
                    break  

                unpacked = struct.unpack("<6iHBB", data)

                fx32_to_float = lambda x: x / (1 << 20)

                char_width = {
                    "fieldRight": fx32_to_float(unpacked[0]),
                    "townFront": fx32_to_float(unpacked[1]),
                    "townBack": fx32_to_float(unpacked[2]),
                    "fieldBack": fx32_to_float(unpacked[3]),
                    "fieldFront": fx32_to_float(unpacked[4]),
                    "fieldLeft": fx32_to_float(unpacked[5]),
                    "index": unpacked[6],
                    "dummy0": unpacked[7],
                    "dummy1": unpacked[8],
                }

                character_width_data.append(char_width)

        with open(output_path, "w") as f_output:
            json.dump(character_width_data, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

file_path = "./LEVELDATA/dq5ds_character_width.dat"
output_path = "./data/dq5ds_character_width.json"
read_character_width(file_path, output_path)
