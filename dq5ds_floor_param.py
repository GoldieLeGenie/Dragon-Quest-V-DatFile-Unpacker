import struct
import json

def read_floor_param(file_path, output_path):
    try:
        floor_param_data = []
        with open(file_path, "rb") as f:
            f.seek(0x14)
            while True:
                data = f.read(0xC)  # Taille de la structure FloorParam (12 octets)

                if len(data) != 0xC:
                    break  # Fin du fichier ou lecture incorrecte

                # Déballage des données
                unpacked = struct.unpack("<BB9cB", data)

                floor_param_entry = {
                    "bgmDaytime": unpacked[0],
                    "bgmNight": unpacked[1],
                    "battlefloor": unpacked[2].hex(),
                    "eventfloor": unpacked[3].hex(),
                    "byte_1": unpacked[4].hex(),
                    "byte_2": unpacked[5].hex(),
                    "byte_3": unpacked[6].hex(),
                    "byte_4": unpacked[7].hex(),
                    "byte_5": unpacked[8].hex(),
                    "byte_6": unpacked[9].hex(),
                    "byte_7": unpacked[10].hex(),
                    "dummy0": unpacked[11]
                }

                floor_param_data.append(floor_param_entry)

        # Sauvegarde en JSON
        with open(output_path, "w") as f_output:
            json.dump(floor_param_data, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_floor_param.dat"
output_path = "./data/dq5ds_floor_param.json"
read_floor_param(file_path, output_path)
