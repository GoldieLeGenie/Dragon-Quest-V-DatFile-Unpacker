import struct
import json

def read_key_table_jk(file_path, output_path):
    try:
        key_table_jk_list = []
        with open(file_path, "rb") as f:
            f.seek(0x14)
            while True:
                data = f.read(0x8)  # Taille de la structure KeyTableJK (8 octets)

                if len(data) != 0x8:
                    break  # Fin du fichier ou lecture incorrecte

                # Déballage des données
                unpacked = struct.unpack("<8B", data)  # 8 u_char (1 octet chaque)

                key_table_entry = {
                    "position": unpacked[0],
                    "right": unpacked[1],
                    "up": unpacked[2],
                    "down": unpacked[3],
                    "left": unpacked[4],
                    "No": unpacked[5],
                    "command": unpacked[6],
                    "dummy0": unpacked[7]
                }

                key_table_jk_list.append(key_table_entry)

        # Sauvegarde en JSON
        with open(output_path, "w") as f_output:
            json.dump(key_table_jk_list, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_keytable_jk.dat"
output_path = "./data/dq5ds_keytable_jk.json"
read_key_table_jk(file_path, output_path)
