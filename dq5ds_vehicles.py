
import struct
import json

def read_vehicle_data(file_path, output_path):
    try:
        vehicle_data_list = []
        with open(file_path, "rb") as f:
            f.seek(0x14)
            while True:
                data = f.read(0x10)  # Taille de la structure VehicleData (16 octets)

                if len(data) != 0x10:
                    break  # Fin du fichier ou lecture incorrecte

                # Déballage des données
                unpacked = struct.unpack("<IIHHBcBB", data)

                vehicle_data_entry = {
                    "shipX": unpacked[0],
                    "shipY": unpacked[1],
                    "placeNum": unpacked[2],
                    "floor": unpacked[3],
                    "id": unpacked[4],
                    "byte_1": unpacked[5].hex(),
                    "dummy0": unpacked[6],
                    "dummy1": unpacked[7],
                }

                vehicle_data_list.append(vehicle_data_entry)

        # Sauvegarde en JSON
        with open(output_path, "w") as f_output:
            json.dump(vehicle_data_list, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_vehicles.dat"  # Remplace par le chemin de ton fichier binaire
output_path = "./data/dq5ds_vehicles.json"    # Remplace par le chemin de sortie du fichier JSON
read_vehicle_data(file_path, output_path)
