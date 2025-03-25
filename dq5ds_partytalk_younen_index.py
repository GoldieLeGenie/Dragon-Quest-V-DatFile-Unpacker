import struct
import json

def read_partytalk_seinen_index(file_path, output_path):
    try:
        partytalk_list = []
        with open(file_path, "rb") as f:
            f.seek(0x14)
            while True:
                data = f.read(0xC)  # Taille de la structure (12 octets)

                if len(data) != 0xC:
                    break  # Fin du fichier ou lecture incorrecte

                # Déballage des données
                unpacked = struct.unpack("<LLHBB", data)

                partytalk_entry = {
                    "floor": unpacked[0],    # uslong (64 bits)
                    "offset": unpacked[1],   # uslong (64 bits)
                    "size": unpacked[2],     # u_short (16 bits)
                    "dummy0": unpacked[3],   # u_char (8 bits)
                    "dummy1": unpacked[4]    # u_char (8 bits)
                }

                partytalk_list.append(partytalk_entry)

        # Sauvegarde en JSON
        with open(output_path, "w") as f_output:
            json.dump(partytalk_list, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_partytalk_younen_index.dat"
output_path = "./data/dq5ds_partytalk_younen_index.json"
read_partytalk_seinen_index(file_path, output_path)
