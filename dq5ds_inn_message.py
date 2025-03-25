import struct
import json

def read_inn_message(file_path, output_path):
    try:
        inn_message_data = []
        with open(file_path, "rb") as f:
            f.seek(0x14)
            while True:
                data = f.read(0x10)  # Taille de la structure InnMessage (16 octets)

                if len(data) != 0x10:
                    break  # Fin du fichier ou lecture incorrecte

                # Déballage des données
                unpacked = struct.unpack("<LLLcBBB", data)  # uslong = I (4 octets), char = b (1 octet), u_char = B (1 octet)

                inn_message_entry = {
                    "message1": unpacked[0],
                    "message2": unpacked[1],
                    "message3": unpacked[2],
                    "byte_1": unpacked[3].hex(),
                    "dummy0": unpacked[4],
                    "dummy1": unpacked[5],
                    "dummy2": unpacked[6]
                }

                inn_message_data.append(inn_message_entry)

        # Sauvegarde en JSON
        with open(output_path, "w") as f_output:
            json.dump(inn_message_data, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_inn_message.dat"
output_path = "./data/dq5ds_inn_message.json"
read_inn_message(file_path, output_path)
