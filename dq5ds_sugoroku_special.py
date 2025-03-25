import struct
import json

def read_sugoroku_special_msg(file_path, output_path):
    try:
        sugoroku_special_msg_list = []
        with open(file_path, "rb") as f:
            f.seek(0x14)
            while True:
                data = f.read(0x20)  # Taille de la structure (32 octets)

                if len(data) != 0x20:
                    break  # Fin du fichier ou lecture incorrecte

                # Déballage des données
                unpacked = struct.unpack("<8L", data)

                sugoroku_special_msg_entry = {
                    "divergent": unpacked[0],
                    "msg1": unpacked[1],
                    "msg2": unpacked[2],
                    "msg3": unpacked[3],
                    "msg4": unpacked[4],
                    "msg5": unpacked[5],
                    "msg6": unpacked[6],
                    "msg7": unpacked[7],
                }

                sugoroku_special_msg_list.append(sugoroku_special_msg_entry)

        # Sauvegarde en JSON
        with open(output_path, "w") as f_output:
            json.dump(sugoroku_special_msg_list, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_sugoroku_special.dat"
output_path = "./data/dq5ds_sugoroku_special.json"
read_sugoroku_special_msg(file_path, output_path)
