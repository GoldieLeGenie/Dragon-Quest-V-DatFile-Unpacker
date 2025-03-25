import struct
import json

def read_player_data1(file_path, output_path):
    try:
        player_data_list = []
        with open(file_path, "rb") as f:
            f.seek(0x14)
            while True:
                data = f.read(0x24)  # Taille de la structure (36 octets)

                if len(data) != 0x24:
                    break  # Fin du fichier ou lecture incorrecte

                # Déballage des données
                unpacked = struct.unpack("<L15HBB", data)

                player_entry = {
                    "exp": unpacked[0],
                    "strength": unpacked[1],
                    "agility": unpacked[2],
                    "intelligence": unpacked[3],
                    "luck": unpacked[4],
                    "HP": unpacked[5],
                    "MP": unpacked[6],
                    "battleAction1": unpacked[7],
                    "battleAction2": unpacked[8],
                    "battleAction3": unpacked[9],
                    "battleAction4": unpacked[10],
                    "normalAction1": unpacked[11],
                    "normalAction2": unpacked[12],
                    "normalAction3": unpacked[13],
                    "normalAction4": unpacked[14],
                    "vitality": unpacked[15],
                    "level": unpacked[16],
                    "dummy0": unpacked[17]
                }

                player_data_list.append(player_entry)

        # Sauvegarde en JSON
        with open(output_path, "w") as f_output:
            json.dump(player_data_list, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_player_level1.dat"
output_path = "./data/dq5ds_player_level1.json"
read_player_data1(file_path, output_path)
