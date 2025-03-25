import struct
import json

def read_clut_code(file_path, output_path):
    try:
        clut_data = []
        with open(file_path, "rb") as f:
            f.seek(0x14)
            while True:
                data = f.read(0xC)  # Taille de la structure (12 octets)

                if len(data) != 0xC:
                    break  # Fin du fichier ou lecture incorrecte

                # Déballage des données
                unpacked = struct.unpack("<fff", data)

                clut_entry = {
                    "colorB": unpacked[0],
                    "colorR": unpacked[1],
                    "colorG": unpacked[2],
                }

                clut_data.append(clut_entry)

        # Sauvegarde en JSON
        with open(output_path, "w") as f_output:
            json.dump(clut_data, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_clut_code.dat"
output_path = "./data/dq5ds_clut_code.json"
read_clut_code(file_path, output_path)
