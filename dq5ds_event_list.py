import struct
import json
import re
def read_event_list(file_path, output_path):
    try:
        event_list_data = []
        with open(file_path, "rb") as f:
            f.seek(0x14)  # Déplacement à l'offset spécifié
            while True:
                data = f.read(0x9C)  # Taille de la structure (156 octets)

                if len(data) != 0x9C:
                    break  # Fin du fichier ou lecture incorrecte

                # Déballage des données
                unpacked = struct.unpack("<7HBB128s8ssBBB", data)

                event_entry = {
                    "index": unpacked[0],
                    "gold": unpacked[1],
                    "weapon": unpacked[2],
                    "armor": unpacked[3],
                    "shield": unpacked[4],
                    "helmet": unpacked[5],
                    "accessory": unpacked[6],
                    "level": unpacked[7],
                    "character": unpacked[8],
                    "caption": unpacked[9].decode("utf-8").strip('\x00'),  # Décodage UTF-16 pour caption
                    "floor": unpacked[10].decode("utf-8").strip('\x00'),     # Décodage UTF-8 pour floor
                    "byte_1": unpacked[11].hex(),
                    "dummy0": unpacked[12],
                    "dummy1": unpacked[13],
                    "dummy2": unpacked[14]
                }

                event_list_data.append(event_entry)

        # Sauvegarde en JSON
        with open(output_path, "w",encoding="utf-8") as f_output:
            json.dump(event_list_data, f_output, indent=4,ensure_ascii=False)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_event_list.dat"
output_path = "./data/dq5ds_event_list.json"
read_event_list(file_path, output_path)
