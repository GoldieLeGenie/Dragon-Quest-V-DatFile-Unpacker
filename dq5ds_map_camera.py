import struct
import json

def read_map_camera(file_path, output_path):
    try:
        map_camera_list = []
        with open(file_path, "rb") as f:
            f.seek(0x14)
            while True:
                data = f.read(0x34)  # Taille de la structure MapCamera (52 octets)

                if len(data) != 0x34:
                    break  # Fin du fichier ou lecture incorrecte
                def validate_float(value):
                    # Vérifier si la valeur est un NaN ou invalide et la corriger
                    if value != value:  # NaN vérifié en utilisant la propriété que NaN != NaN
                        return 0.0  # Remplacer NaN par une valeur par défaut, ici 0.0
                    return value
                # Déballage des données
                unpacked = struct.unpack("<fffffffHHH16sBB", data)  # fx32 (I), u_short (H), char[16] (16s), u_char (B)
                
                def validate_fx32(value):
                    # Vérifier si la valeur est un NaN ou invalide et la corriger
                    if value != value:  # NaN vérifié en utilisant la propriété que NaN != NaN
                        return 0  # Remplacer NaN par une valeur par défaut, ici 0
                    return value
                
                map_camera_entry = {
                    "distance": validate_fx32(unpacked[0]),
                    "angleX": validate_fx32(unpacked[1]),
                    "angleY": validate_fx32(unpacked[2]),
                    "angleZ": validate_fx32(unpacked[3]),
                    "x": validate_fx32(unpacked[4]),
                    "y": validate_fx32(unpacked[5]),
                    "z": validate_fx32(unpacked[6]),
                    "areaNo": unpacked[7],
                    "flagNo": unpacked[8],
                    "floorNo": unpacked[9],
                    "fileNo": unpacked[10].decode("utf-8",).strip('\x00'),  # Conversion en chaîne de caractères
                    "dummy0": unpacked[11],
                    "dummy1": unpacked[12]
                }

                map_camera_list.append(map_camera_entry)

        # Sauvegarde en JSON
        with open(output_path, "w") as f_output:
            json.dump(map_camera_list, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_map_camera.dat"
output_path = "./data/dq5ds_map_camera.json"
read_map_camera(file_path, output_path)
