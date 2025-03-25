import struct
import json

def read_sugoroku_stage(file_path, output_path):
    try:
        sugoroku_stage_list = []
        with open(file_path, "rb") as f:
            f.seek(0x14)
            while True:
                data = f.read(0x18)  # Taille de la structure (24 octets)

                if len(data) != 0x18:
                    break  # Fin du fichier ou lecture incorrecte

                # Déballage des données
                unpacked = struct.unpack("<11HBB", data)

                sugoroku_stage_entry = {
                    "mapNo": unpacked[0],
                    "placeNo": unpacked[1],
                    "panelNo": unpacked[2],
                    "link1": unpacked[3],
                    "link2": unpacked[4],
                    "link3": unpacked[5],
                    "reverse": unpacked[6],
                    "divergent": unpacked[7],
                    "warpMapNo": unpacked[8],
                    "warpPlaceNo": unpacked[9],
                    "index": unpacked[10],
                    "dummy0": unpacked[11],
                    "dummy1": unpacked[12],
                }

                sugoroku_stage_list.append(sugoroku_stage_entry)

        # Sauvegarde en JSON
        with open(output_path, "w") as f_output:
            json.dump(sugoroku_stage_list, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_sugoroku_stage.dat"
output_path = "./data/dq5ds_sugoroku_stage.json"
read_sugoroku_stage(file_path, output_path)
