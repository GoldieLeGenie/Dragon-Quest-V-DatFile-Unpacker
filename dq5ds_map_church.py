import struct
import json

def read_map_church(file_path, output_path):
    try:
        map_church_data = []
        with open(file_path, "rb") as f:
            f.seek(0x14)
            while True:
                data = f.read(0x1C)  # Taille de la structure (28 octets)

                if len(data) != 0x1C:
                    break  # Fin du fichier ou lecture incorrecte
                    
                # Déballage des données
                unpacked = struct.unpack("<3f5H2Bc3B", data)
                def validate_fx32(value):
                    # Vérifier si la valeur est un NaN ou invalide et la corriger
                    if value != value:  # NaN vérifié en utilisant la propriété que NaN != NaN
                        return 0  # Remplacer NaN par une valeur par défaut, ici 0
                    return value
                map_church_entry = {
                    "playerX": validate_fx32(unpacked[0]),
                    "playerY": validate_fx32(unpacked[1]),
                    "playerZ": validate_fx32(unpacked[2]),
                    "direction": unpacked[3],
                    "ranafloor": unpacked[4],
                    "settingflag": unpacked[5],
                    "checkflag": unpacked[6],
                    "floor": unpacked[7],
                    "locationSounen": unpacked[8],
                    "locationSeinen": unpacked[9],
                    "byte_1": unpacked[10].hex(),
                    "dummy0": unpacked[11],
                    "dummy1": unpacked[12],
                    "dummy2": unpacked[13]
                }

                map_church_data.append(map_church_entry)

        # Sauvegarde en JSON
        with open(output_path, "w") as f_output:
            json.dump(map_church_data, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_map_church.dat"
output_path = "./data/dq5ds_map_church.json"
read_map_church(file_path, output_path)
