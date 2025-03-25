import struct
import json

def read_player_carriage(file_path, output_path):
    try:
        player_carriages = []
        with open(file_path, "rb") as f:
            f.seek(0x14)
            while True:
                data = f.read(0x4)  # Taille de la structure (4 octets)

                if len(data) != 0x4:
                    break  # Fin du fichier ou lecture incorrecte

                # Déballage des données
                unpacked = struct.unpack("<HBc", data)

                player_carriage_entry = {
                    "floor": unpacked[0],  # u_short (16 bits)
                    "area": unpacked[1],   # u_char (8 bits)
                    "byte_1": unpacked[2].hex()  # char (8 bits)
                }

                player_carriages.append(player_carriage_entry)

        # Sauvegarde en JSON
        with open(output_path, "w") as f_output:
            json.dump(player_carriages, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_player_carriage.dat"
output_path = "./data/dq5ds_player_carriage.json"
read_player_carriage(file_path, output_path)
