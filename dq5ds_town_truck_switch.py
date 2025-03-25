import struct
import json

def read_truck_switch_data(file_path, output_path):
    try:
        truck_switch_data_list = []
        with open(file_path, "rb") as f:
            f.seek(0x14)
            while True:
                data = f.read(0xC)  # Taille de la structure (12 octets)

                if len(data) != 0xC:
                    break  # Fin du fichier ou lecture incorrecte

                # Déballage des données
                unpacked = struct.unpack("<5HcB", data)

                truck_switch_data_entry = {
                    "railUid": unpacked[0],
                    "floor": unpacked[1],
                    "split": unpacked[2],
                    "next": unpacked[3],
                    "switchUid": unpacked[4],
                    "byte_1": unpacked[5].hex(),
                    "dummy0": unpacked[6],
                }

                truck_switch_data_list.append(truck_switch_data_entry)

        # Sauvegarde en JSON
        with open(output_path, "w") as f_output:
            json.dump(truck_switch_data_list, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_town_truck_switch.dat"
output_path = "./data/dq5ds_town_truck_switch.json"
read_truck_switch_data(file_path, output_path)
