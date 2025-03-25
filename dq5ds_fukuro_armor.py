import struct
import json

def read_fukuro_armor(file_path, output_path):
    try:
        fukuro_armor_data = []
        with open(file_path, "rb") as f:
            f.seek(0x14)
            while True:
                data = f.read(0x8)  # Taille de la structure FukuroArmor (8 octets)

                if len(data) != 0x8:
                    break  # Fin du fichier ou lecture incorrecte

                # Déballage des données
                unpacked = struct.unpack("<H6B", data)

                fukuro_armor_entry = {
                    "fukuroNum": unpacked[0],
                    "itemID1": unpacked[1],
                    "itemID3": unpacked[2],
                    "itemID2": unpacked[3],
                    "dummy0": unpacked[4],
                    "dummy1": unpacked[5],
                    "dummy2": unpacked[6]
                }

                fukuro_armor_data.append(fukuro_armor_entry)

        # Sauvegarde en JSON
        with open(output_path, "w") as f_output:
            json.dump(fukuro_armor_data, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_fukuro_armor.dat"
output_path = "./data/dq5ds_fukuro_armor.json"
read_fukuro_armor(file_path, output_path)
