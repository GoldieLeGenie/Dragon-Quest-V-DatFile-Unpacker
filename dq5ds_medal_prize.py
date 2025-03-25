import struct
import json

def read_medal_prize(file_path, output_path):
    try:
        medal_prize_list = []
        with open(file_path, "rb") as f:
            f.seek(0x14)
            while True:
                data = f.read(0x4)  # Taille de la structure (4 octets)

                if len(data) != 0x4:
                    break  # Fin du fichier ou lecture incorrecte

                # Déballage des données
                unpacked = struct.unpack("<HBc", data)

                medal_prize_entry = {
                    "item": unpacked[0],
                    "medal": unpacked[1],
                    "byte_1": unpacked[2].hex()
                }

                medal_prize_list.append(medal_prize_entry)

        # Sauvegarde en JSON
        with open(output_path, "w") as f_output:
            json.dump(medal_prize_list, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_medal_prize.dat"
output_path = "./data/dq5ds_medal_prize.json"
read_medal_prize(file_path, output_path)
