import struct
import json

def read_truck_rail_data(file_path, output_path):
    try:
        truck_rail_data_list = []
        with open(file_path, "rb") as f:
            f.seek(0x14)
            while True:
                data = f.read(0x10)  # Taille de la structure TruckRail (16 octets)

                if len(data) != 0x10:
                    break  # Fin du fichier ou lecture incorrecte

                # Déballage des données
                unpacked = struct.unpack("<6HBB", data)

                truck_rail_data_entry = {
                    "moveFloor": unpacked[0],
                    "floor": unpacked[1],
                    "link1": unpacked[2],
                    "link2": unpacked[3],
                    "ID": unpacked[4],
                    "branch": unpacked[5],
                    "moveID": unpacked[6],
                    "special": unpacked[7],
                    "dummy0": unpacked[8],
                }

                truck_rail_data_list.append(truck_rail_data_entry)

        # Sauvegarde en JSON
        with open(output_path, "w") as f_output:
            json.dump(truck_rail_data_list, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_truck_rail.dat"  # Remplace par le chemin de ton fichier binaire
output_path = "./data/dq5ds_truck_rail.json"    # Remplace par le chemin de sortie du fichier JSON
read_truck_rail_data(file_path, output_path)
