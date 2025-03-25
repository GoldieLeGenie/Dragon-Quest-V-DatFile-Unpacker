import struct
import json

def read_petal_data(file_path, output_path):
    try:
        petal_data_list = []
        with open(file_path, "rb") as f:
            f.seek(0x14)  # Déplacement à l'offset spécifié
            while True:
                data = f.read(0x04)  # Taille de la structure (4 octets)

                if len(data) != 0x04:
                    break  # Fin du fichier ou lecture incorrecte

                # Déballage des données
                unpacked = struct.unpack("<BBcB", data)

                petal_entry = {
                    "position": unpacked[0],
                    "index": unpacked[1],
                    "byte_1": unpacked[2].hex(),
                    "dummy0": unpacked[3]
                }

                petal_data_list.append(petal_entry)

        # Sauvegarde en JSON
        with open(output_path, "w") as f_output:
            json.dump(petal_data_list, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_endhanabira.dat"
output_path = "./data/dq5ds_endhanabira.json"
read_petal_data(file_path, output_path)
