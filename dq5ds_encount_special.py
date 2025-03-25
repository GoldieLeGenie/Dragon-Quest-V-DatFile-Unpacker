import struct
import json

def read_encount_special(file_path, output_path):
    try:
        encount_special_list = []
        with open(file_path, "rb") as f:
            f.seek(0x14)  # Déplacement à l'offset spécifié
            while True:
                data = f.read(0x08)  # Taille de la structure (8 octets)

                if len(data) != 0x08:
                    break  # Fin du fichier ou lecture incorrecte

                # Déballage des données
                unpacked = struct.unpack("<4BccBB", data)

                encount_entry = {
                    "monsterID1": unpacked[0],
                    "monsterID2": unpacked[1],
                    "monsterID3": unpacked[2],
                    "monsterID4": unpacked[3],
                    "byte_1": unpacked[4].hex(),
                    "byte_2": unpacked[5].hex(),
                    "dummy0": unpacked[6],
                    "dummy1": unpacked[7]
                }

                encount_special_list.append(encount_entry)

        # Sauvegarde en JSON
        with open(output_path, "w") as f_output:
            json.dump(encount_special_list, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_encount_special.dat"
output_path = "./data/dq5ds_encount_special.json"
read_encount_special(file_path, output_path)
