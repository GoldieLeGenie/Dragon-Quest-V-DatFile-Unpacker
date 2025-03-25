import struct
import json

def read_sugoroku_data(file_path, output_path):
    try:
        sugoroku_data_list = []
        with open(file_path, "rb") as f:
            f.seek(0x14)
            while True:
                data = f.read(0x10)  # Taille de la structure (16 octets)

                if len(data) != 0x10:
                    break  # Fin du fichier ou lecture incorrecte

                # Déballage des données
                unpacked = struct.unpack("<4H8B", data)

                sugoroku_data_entry = {
                    "moneyMin": unpacked[0],
                    "moneyMax": unpacked[1],
                    "item": unpacked[2],
                    "ratio256": unpacked[3],
                    "index": unpacked[4],
                    "times": unpacked[5],
                    "ratio32": unpacked[6],
                    "encount1": unpacked[7],
                    "encount2": unpacked[8],
                    "encount3": unpacked[9],
                    "encount4": unpacked[10],
                    "dummy0": unpacked[11]
                }

                sugoroku_data_list.append(sugoroku_data_entry)

        # Sauvegarde en JSON
        with open(output_path, "w") as f_output:
            json.dump(sugoroku_data_list, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_sugoroku_data.dat"
output_path = "./data/dq5ds_sugoroku_data.json"
read_sugoroku_data(file_path, output_path)
