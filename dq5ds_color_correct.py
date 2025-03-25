import struct
import json

def read_color_correct(file_path, output_path):
    try:
        color_data = []
        with open(file_path, "rb") as f:
            f.seek(0x14)
            while True:
                data = f.read(0x8)  # Taille de la structure (8 octets)

                if len(data) != 0x8:
                    break  # Fin du fichier ou lecture incorrecte

                # Déballage des données
                unpacked = struct.unpack("<HBccBBB", data)

                color_entry = {
                    "floor": unpacked[0],
                    "backcolor": unpacked[1],
                    "byte_1": unpacked[2].hex(),
                    "byte_2": unpacked[3].hex(),
                    "dummy0": unpacked[4],
                    "dummy1": unpacked[5],
                    "dummy2": unpacked[6],
                }

                color_data.append(color_entry)

        # Sauvegarde en JSON
        with open(output_path, "w") as f_output:
            json.dump(color_data, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_color_correct.dat"
output_path = "./data/dq5ds_color_correct.json"
read_color_correct(file_path, output_path)
