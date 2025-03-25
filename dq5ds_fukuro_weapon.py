import struct
import json

def read_fukuro_weapon(file_path, output_path):
    try:
        fukuro_weapon_data = []
        with open(file_path, "rb") as f:
            f.seek(0x14)
            while True:
                data = f.read(0x4)  # Taille de la structure FukuroWeapon (4 octets)

                if len(data) != 0x4:
                    break  # Fin du fichier ou lecture incorrecte

                # Déballage des données
                unpacked = struct.unpack("<HBB", data)

                fukuro_weapon_entry = {
                    "fukuroNum": unpacked[0],
                    "itemID": unpacked[1],
                    "dummy0": unpacked[2]
                }

                fukuro_weapon_data.append(fukuro_weapon_entry)

        # Sauvegarde en JSON
        with open(output_path, "w") as f_output:
            json.dump(fukuro_weapon_data, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_fukuro_weapon.dat"
output_path = "./data/dq5ds_fukuro_weapon.json"
read_fukuro_weapon(file_path, output_path)
