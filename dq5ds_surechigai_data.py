import struct
import json

def read_surechigai_data(file_path, output_path):
    try:
        surechigai_data_list = []
        with open(file_path, "rb") as f:
            f.seek(0x14)
            while True:
                data = f.read(0x8)  # Taille de la structure (8 octets)

                if len(data) != 0x8:
                    break  # Fin du fichier ou lecture incorrecte

                # Déballage des données
                unpacked = struct.unpack("<HHBcBB", data)

                surechigai_data_entry = {
                    "cgicon": unpacked[0],
                    "itemid": unpacked[1],
                    "index": unpacked[2],
                    "byte_1": unpacked[3].hex(),
                    "dummy0": unpacked[4],
                    "dummy1": unpacked[5],
                }

                surechigai_data_list.append(surechigai_data_entry)

        # Sauvegarde en JSON
        with open(output_path, "w") as f_output:
            json.dump(surechigai_data_list, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_surechigai_data.dat"
output_path = "./data/dq5ds_surechigai_data.json"
read_surechigai_data(file_path, output_path)
