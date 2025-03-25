import struct
import json

def read_truck_goal_data(file_path, output_path):
    try:
        truck_goal_data_list = []
        with open(file_path, "rb") as f:
            f.seek(0x14)
            while True:
                data = f.read(0x14)  # Taille de la structure (20 octets)

                if len(data) != 0x14:
                    break  # Fin du fichier ou lecture incorrecte

                # Déballage des données
                unpacked = struct.unpack("<3IHHhBB", data)

                truck_goal_data_entry = {
                    "X": unpacked[0],
                    "Y": unpacked[1],
                    "Z": unpacked[2],
                    "floor": unpacked[3],
                    "uid": unpacked[4],
                    "dir": unpacked[5],
                    "dummy0": unpacked[6],
                    "dummy1": unpacked[7],
                }

                truck_goal_data_list.append(truck_goal_data_entry)

        # Sauvegarde en JSON
        with open(output_path, "w") as f_output:
            json.dump(truck_goal_data_list, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_truck_goal.dat"
output_path = "./data/dq5ds_truck_goal.json"
read_truck_goal_data(file_path, output_path)
