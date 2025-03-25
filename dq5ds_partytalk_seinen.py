import struct
import json

def read_partytalk_ending(file_path, output_path):
    try:
        partytalk_list = []
        with open(file_path, "rb") as f:
            f.seek(0x14)
            while True:
                data = f.read(0x2C)  # Taille de la structure (44 octets)

                if len(data) != 0x2C:
                    break  # Fin du fichier ou lecture incorrecte

                # Déballage des données
                unpacked = struct.unpack("<7L3H7c3B", data)

                partytalk_entry = {
                    "preMessage": unpacked[0],  # uslong (64 bits)
                    "message": unpacked[1],     # uslong (64 bits)
                    "no": unpacked[2],          # uslong (64 bits)
                    "value1": unpacked[3],      # uslong (64 bits)
                    "value2": unpacked[4],      # uslong (64 bits)
                    "value4": unpacked[5],      # uslong (64 bits)
                    "format": unpacked[6],      # uslong (64 bits)
                    "start": unpacked[7],       # u_short (16 bits)
                    "end": unpacked[8],         # u_short (16 bits)
                    "floor": unpacked[9],       # u_short (16 bits)
                    "timezone": unpacked[10].hex(),   # char (8 bits)
                    "priority": unpacked[11].hex(),   # char (8 bits)
                    "condition1": unpacked[12].hex(), # char (8 bits)
                    "condition2": unpacked[13].hex(), # char (8 bits)
                    "alivePC": unpacked[14].hex(),    # char (8 bits)
                    "conduct": unpacked[15].hex(),    # char (8 bits)
                    "byte_1": unpacked[16].hex(),     # char (8 bits)
                    "dummy0": unpacked[17],     # u_char (8 bits)
                    "dummy1": unpacked[18],     # u_char (8 bits)
                    "dummy2": unpacked[19]      # u_char (8 bits)
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
file_path = "./LEVELDATA/dq5ds_partytalk_seinen.dat"
output_path = "./data/dq5ds_partytalk_seinen.json"
read_partytalk_ending(file_path, output_path)
