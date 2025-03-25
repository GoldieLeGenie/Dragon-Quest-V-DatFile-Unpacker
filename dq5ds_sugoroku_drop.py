import struct
import json

def read_sugoroku_drop(file_path, output_path):
    try:
        sugoroku_drop_list = []
        with open(file_path, "rb") as f:
            f.seek(0x14)
            while True:
                data = f.read(0x10)  # Taille de la structure (16 octets)

                if len(data) != 0x10:
                    break  # Fin du fichier ou lecture incorrecte

                # Déballage des données
                unpacked = struct.unpack("<fffHH", data)

                sugoroku_drop_entry = {
                    "x": unpacked[0],
                    "y": unpacked[1],
                    "z": unpacked[2],
                    "before": unpacked[3],
                    "after": unpacked[4]
                }

                sugoroku_drop_list.append(sugoroku_drop_entry)

        # Sauvegarde en JSON
        with open(output_path, "w") as f_output:
            json.dump(sugoroku_drop_list, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_sugoroku_drop.dat"
output_path = "./data/dq5ds_sugoroku_drop.json"
read_sugoroku_drop(file_path, output_path)
