import struct
import json

def read_floor_fog(file_path, output_path):
    try:
        floor_fog_data = []
        with open(file_path, "rb") as f:
            f.seek(0x14)
            while True:
                data = f.read(0x14)  # Taille de la structure FloorFog (20 octets)

                if len(data) != 0x14:
                    break  # Fin du fichier ou lecture incorrecte

                # Déballage des données
                unpacked = struct.unpack("<ffHH8B", data)

                floor_fog_entry = {
                    "rate01": unpacked[0],
                    "rate00": unpacked[1],
                    "offset00": unpacked[2],
                    "offset01": unpacked[3],
                    "colorR00": unpacked[4],
                    "colorR01": unpacked[5],
                    "colorG00": unpacked[6],
                    "colorG01": unpacked[7],
                    "colorB00": unpacked[8],
                    "colorB01": unpacked[9],
                    "dummy0": unpacked[10],
                    "dummy1": unpacked[11]
                }

                floor_fog_data.append(floor_fog_entry)

        # Sauvegarde en JSON
        with open(output_path, "w") as f_output:
            json.dump(floor_fog_data, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_fog_data.dat"
output_path = "./data/dq5ds_fog_data.json"
read_floor_fog(file_path, output_path)
