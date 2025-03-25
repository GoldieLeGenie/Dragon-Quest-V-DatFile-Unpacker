import struct
import json

def read_sugoroku_change_msg(file_path, output_path):
    try:
        change_msgs = []
        with open(file_path, "rb") as f:
            f.seek(0x14)
            while True:
                data = f.read(0xC)  # Taille de la structure (12 octets)

                if len(data) != 0xC:
                    break  # Fin du fichier ou lecture incorrecte

                # Déballage des données
                unpacked = struct.unpack("<LLL", data)

                change_msg_entry = {
                    "divergent": unpacked[0],
                    "msg1": unpacked[1],
                    "msg2": unpacked[2]
                }

                change_msgs.append(change_msg_entry)

        # Sauvegarde en JSON
        with open(output_path, "w") as f_output:
            json.dump(change_msgs, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_sugoroku_change.dat"
output_path = "./data/dq5ds_sugoroku_change.json"
read_sugoroku_change_msg(file_path, output_path)
