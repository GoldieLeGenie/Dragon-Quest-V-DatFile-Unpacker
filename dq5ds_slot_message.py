import struct
import json

def read_slot_message(file_path, output_path):
    try:
        slot_messages = []
        with open(file_path, "rb") as f:
            f.seek(0x14)
            while True:
                data = f.read(0x8)  # Taille de la structure (8 octets)

                if len(data) != 0x8:
                    break  # Fin du fichier ou lecture incorrecte

                # Déballage des données
                unpacked = struct.unpack("<Lc3B", data)

                slot_message_entry = {
                    "message": unpacked[0],  # uslong (8 octets)
                    "byte_1": unpacked[1].hex(),   # char
                    "dummy0": unpacked[2],   # u_char
                    "dummy1": unpacked[3],   # u_char
                    "dummy2": unpacked[4],   # u_char
                }

                slot_messages.append(slot_message_entry)

        # Sauvegarde en JSON
        with open(output_path, "w") as f_output:
            json.dump(slot_messages, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_slot_message.dat"
output_path = "./data/dq5ds_slot_message.json"
read_slot_message(file_path, output_path)
