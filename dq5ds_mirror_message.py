import struct
import json

def read_mirror_message(file_path, output_path):
    try:
        mirror_message_list = []
        with open(file_path, "rb") as f:
            f.seek(0x14)
            while True:
                data = f.read(0x8)  # Taille de la structure (8 octets)

                if len(data) != 0x8:
                    break  # Fin du fichier ou lecture incorrecte

                # Déballage des données
                unpacked = struct.unpack("<LBccB", data)

                mirror_message_entry = {
                    "message": unpacked[0],   # uslong (32 bits)
                    "leader": unpacked[1],    # u_char (8 bits)
                    "byte_1": unpacked[2].hex(),    # char (8 bits signé)
                    "byte_2": unpacked[3].hex(),    # char (8 bits signé)
                    "dummy0": unpacked[4]     # u_char (8 bits)
                }

                mirror_message_list.append(mirror_message_entry)

        # Sauvegarde en JSON
        with open(output_path, "w") as f_output:
            json.dump(mirror_message_list, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_mirror_message.dat"
output_path = "./data/dq5ds_mirror_message.json"
read_mirror_message(file_path, output_path)
