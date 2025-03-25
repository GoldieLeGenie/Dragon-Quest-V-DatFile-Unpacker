import struct
import json

def read_effect_color_param(file_path, output_path):
    try:
        effect_color_data = []
        with open(file_path, "rb") as f:
            f.seek(0x14)
            while True:
                data = f.read(0x10)  # Taille de la structure (16 octets)

                if len(data) != 0x10:
                    break  # Fin du fichier ou lecture incorrecte

                # Déballage des données
                unpacked = struct.unpack("<fffHBB", data)

                effect_entry = {
                    "rPoint": unpacked[0],
                    "gPoint": unpacked[1],
                    "bPoint": unpacked[2],
                    "frame": unpacked[3],
                    "index": unpacked[4],
                    "dummy0": unpacked[5],
                }

                effect_color_data.append(effect_entry)

        # Sauvegarde en JSON
        with open(output_path, "w") as f_output:
            json.dump(effect_color_data, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_effect_color.dat"
output_path = "./data/dq5ds_effect_color.json"
read_effect_color_param(file_path, output_path)
