import struct
import json

def read_medal_message(file_path, output_path):
    try:
        medal_message_list = []
        with open(file_path, "rb") as f:
            f.seek(0x14)
            while True:
                data = f.read(0x8)  # Taille de la structure (8 octets)

                if len(data) != 0x8:
                    break  # Fin du fichier ou lecture incorrecte

                # Déballage des données
                unpacked = struct.unpack("<LcBBB", data)

                medal_message_entry = {
                    "message1": unpacked[0],  # uslong (32 bits)
                    "byte_1": unpacked[1].hex(),    # char (8 bits signé)
                    "dummy0": unpacked[2],    # u_char (8 bits)
                    "dummy1": unpacked[3],    # u_char (8 bits)
                    "dummy2": unpacked[4]     # u_char (8 bits)
                }

                medal_message_list.append(medal_message_entry)

        # Sauvegarde en JSON
        with open(output_path, "w") as f_output:
            json.dump(medal_message_list, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_medal_message.dat"
output_path = "./data/dq5ds_medal_message.json"
read_medal_message(file_path, output_path)
