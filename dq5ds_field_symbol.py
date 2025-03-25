import struct
import json

def read_field_symbol(file_path, output_path):
    try:
        field_symbol_data = []
        with open(file_path, "rb") as f:
            f.seek(0x14)
            while True:
                data = f.read(0xC)  # Taille de la structure FieldSymbol (12 octets)

                if len(data) != 0xC:
                    break  # Fin du fichier ou lecture incorrecte

                # Déballage des données
                unpacked = struct.unpack("<LHHBBBc", data)

                field_symbol_entry = {
                    "message": unpacked[0],
                    "uid": unpacked[1],
                    "item": unpacked[2],
                    "posY": unpacked[3],
                    "posX": unpacked[4],
                    "type": unpacked[5],
                    "byte_1": unpacked[6].hex()
                }

                field_symbol_data.append(field_symbol_entry)

        # Sauvegarde en JSON
        with open(output_path, "w") as f_output:
            json.dump(field_symbol_data, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_field_symbol.dat"
output_path = "./data/dq5ds_field_symbol.json"
read_field_symbol(file_path, output_path)
