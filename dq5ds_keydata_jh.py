import struct
import json

def read_key_data_jh(file_path, output_path):
    try:
        key_data_jh_list = []
        with open(file_path, "rb") as f:
            f.seek(0x14)
            while True:
                data = f.read(0x8)  # Taille de la structure KeyDataJH (8 octets)

                if len(data) != 0x8:
                    break  # Fin du fichier ou lecture incorrecte

                # Déballage des données
                unpacked = struct.unpack("<LHBB", data)  # uslong = I (4 octets), u_short = H (2 octets), u_char = B (1 octet)

                key_data_entry = {
                    "Data": unpacked[0],
                    "No": unpacked[1],
                    "dummy0": unpacked[2],
                    "dummy1": unpacked[3]
                }

                key_data_jh_list.append(key_data_entry)

        # Sauvegarde en JSON
        with open(output_path, "w") as f_output:
            json.dump(key_data_jh_list, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_keydata_jh.dat"
output_path = "./data/dq5ds_keydata_jh.json"
read_key_data_jh(file_path, output_path)
