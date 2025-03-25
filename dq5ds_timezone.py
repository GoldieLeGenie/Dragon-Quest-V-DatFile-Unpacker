import struct
import json

def read_timezone_data(file_path, output_path):
    try:
        timezone_data_list = []
        with open(file_path, "rb") as f:
            f.seek(0x14)
            while True:
                data = f.read(0x4)  # Taille de la structure (4 octets)

                if len(data) != 0x4:
                    break  # Fin du fichier ou lecture incorrecte

                # Déballage des données
                unpacked = struct.unpack("<Hcc", data)

                timezone_data_entry = {
                    "frame": unpacked[0],
                    "byte_1": unpacked[1].hex(),
                    "byte_2": unpacked[2].hex(),
                }

                timezone_data_list.append(timezone_data_entry)

        # Sauvegarde en JSON
        with open(output_path, "w") as f_output:
            json.dump(timezone_data_list, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_timezone.dat"
output_path = "./data/dq5ds_timezone.json"
read_timezone_data(file_path, output_path)
