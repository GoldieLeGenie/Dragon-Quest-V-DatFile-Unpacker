import struct
import json

def read_shop_index3(file_path, output_path):
    try:
        shop_indexes = []
        with open(file_path, "rb") as f:
            f.seek(0x14)
            while True:
                data = f.read(0x4)  # Taille de la structure (4 octets)

                if len(data) != 0x4:
                    break  # Fin du fichier ou lecture incorrecte

                # Déballage des données
                unpacked = struct.unpack("<HcB", data)

                shop_index_entry = {
                    "area": unpacked[0],   # u_short (16 bits)
                    "byte_1": unpacked[1].hex(),  # char (8 bits)
                    "dummy0": unpacked[2]   # u_char (8 bits)
                }

                shop_indexes.append(shop_index_entry)

        # Sauvegarde en JSON
        with open(output_path, "w") as f_output:
            json.dump(shop_indexes, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_shop_index_3.dat"
output_path = "./data/dq5ds_shop_index_3.json"
read_shop_index3(file_path, output_path)
