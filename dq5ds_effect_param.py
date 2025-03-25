import struct
import json

def read_effect_param(file_path, output_path):
    try:
        effect_param_data = []
        with open(file_path, "rb") as f:
            f.seek(0x14)
            while True:
                data = f.read(0x18)  # Taille de la structure (24 octets)

                if len(data) != 0x18:
                    break  # Fin du fichier ou lecture incorrecte

                # Déballage des données
                unpacked = struct.unpack("<f6H4B2c2B", data)

                effect_entry = {
                    "scale": unpacked[0],
                    "index": unpacked[1],
                    "frame": unpacked[2],
                    "homing": unpacked[3],
                    "sound": unpacked[4],
                    "camera": unpacked[5],
                    "camera2": unpacked[6],
                    "interval": unpacked[7],
                    "color": unpacked[8],
                    "hold": unpacked[9],
                    "wait": unpacked[10],
                    "byte_1": unpacked[11].hex(),
                    "byte_2": unpacked[12].hex(),
                    "dummy0": unpacked[13],
                    "dummy1": unpacked[14],
                }

                effect_param_data.append(effect_entry)

        # Sauvegarde en JSON
        with open(output_path, "w") as f_output:
            json.dump(effect_param_data, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_effect_param.dat"
output_path = "./data/dq5ds_effect_param.json"
read_effect_param(file_path, output_path)
