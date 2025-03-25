import struct
import json

def read_shop_message(file_path, output_path):
    try:
        shop_messages = []
        with open(file_path, "rb") as f:
            f.seek(0x14)
            while True:
                data = f.read(0x14)  # Taille de la structure (20 octets)

                if len(data) != 0x14:
                    break  # Fin du fichier ou lecture incorrecte

                # Déballage des données
                unpacked = struct.unpack("<4LcBBB", data)

                shop_message_entry = {
                    "message1": unpacked[0],  # uslong (64 bits)
                    "message2": unpacked[1],  # uslong (64 bits)
                    "message3": unpacked[2],  # uslong (64 bits)
                    "message4": unpacked[3],  # uslong (64 bits)
                    "byte_1": unpacked[4].hex(),    # char (8 bits signé)
                    "dummy0": unpacked[5],    # u_char (8 bits non signé)
                    "dummy1": unpacked[6],    # u_char (8 bits non signé)
                    "dummy2": unpacked[7],    # u_char (8 bits non signé)
                }

                shop_messages.append(shop_message_entry)

        # Sauvegarde en JSON
        with open(output_path, "w") as f_output:
            json.dump(shop_messages, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_shop_message.dat"
output_path = "./data/dq5ds_shop_message.json"
read_shop_message(file_path, output_path)
