import struct
import json

def read_coin_message(file_path, output_path):
    try:
        coin_data = []
        with open(file_path, "rb") as f:
            f.seek(0x14)
            while True:
                data = f.read(0x8)  # Taille de la structure (8 octets)

                if len(data) != 0x8:
                    break  # Fin du fichier ou lecture incorrecte

                # Déballage des données
                unpacked = struct.unpack("<LcBBB", data)

                coin_entry = {
                    "message1": unpacked[0],
                    "byte_1": unpacked[1].hex(),
                    "dummy0": unpacked[2],
                    "dummy1": unpacked[3],
                    "dummy2": unpacked[4],
                }

                coin_data.append(coin_entry)

        # Sauvegarde en JSON
        with open(output_path, "w") as f_output:
            json.dump(coin_data, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_coin_message.dat"
output_path = "./data/dq5ds_coin_message.json"
read_coin_message(file_path, output_path)
