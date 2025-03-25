import struct
import json

def read_event_flag(file_path, output_path):
    try:
        event_flag_data = []
        with open(file_path, "rb") as f:
            f.seek(0x14)  # Déplacement à l'offset spécifié
            while True:
                data = f.read(0x2C)  # Taille de la structure (44 octets)

                if len(data) != 0x2C:
                    break  # Fin du fichier ou lecture incorrecte

                # Déballage des données
                unpacked = struct.unpack("<19HBcccBB", data)

                event_flag_entry = {
                    "flag1": unpacked[0],
                    "flag2": unpacked[1],
                    "flag3": unpacked[2],
                    "flag4": unpacked[3],
                    "flag5": unpacked[4],
                    "flag6": unpacked[5],
                    "flag7": unpacked[6],
                    "flag8": unpacked[7],
                    "flag9": unpacked[8],
                    "flag10": unpacked[9],
                    "flag11": unpacked[10],
                    "flag12": unpacked[11],
                    "waitFlag1": unpacked[12],
                    "waitFlag2": unpacked[13],
                    "waitFlag3": unpacked[14],
                    "waitFlag4": unpacked[15],
                    "waitFlag5": unpacked[16],
                    "waitFlag6": unpacked[17],
                    "index": unpacked[18],
                    "NPC": unpacked[19],
                    "byte_1": unpacked[20].hex(),
                    "byte_2": unpacked[21].hex(),
                    "byte_3": unpacked[22].hex(),
                    "dummy0": unpacked[23],
                    "dummy1": unpacked[24]
                }

                event_flag_data.append(event_flag_entry)

        # Sauvegarde en JSON
        with open(output_path, "w") as f_output:
            json.dump(event_flag_data, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_event_flag.dat"
output_path = "./data/dq5ds_event_flag.json"
read_event_flag(file_path, output_path)
