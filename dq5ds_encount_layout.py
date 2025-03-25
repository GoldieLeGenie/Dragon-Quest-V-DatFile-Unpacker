import struct
import json

def read_encount_layout(file_path, output_path):
    try:
        encount_layout_list = []
        with open(file_path, "rb") as f:
            f.seek(0x14)  # Déplacement à l'offset spécifié
            while True:
                data = f.read(0x04)  # Taille de la structure (4 octets)

                if len(data) != 0x04:
                    break  # Fin du fichier ou lecture incorrecte

                # Déballage des données
                unpacked = struct.unpack("<HBB", data)

                encount_entry = {
                    "floorNum": unpacked[0],
                    "chapter": unpacked[1],
                    "tileID": unpacked[2]
                }

                encount_layout_list.append(encount_entry)

        # Sauvegarde en JSON
        with open(output_path, "w") as f_output:
            json.dump(encount_layout_list, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_encount_layout.dat"
output_path = "./data/dq5ds_encount_layout.json"
read_encount_layout(file_path, output_path)
