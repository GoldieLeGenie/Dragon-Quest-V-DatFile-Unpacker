import struct
import json

def read_fukuro_item(file_path, output_path):
    try:
        fukuro_item_data = []
        with open(file_path, "rb") as f:
            f.seek(0x14)
            while True:
                data = f.read(0x14)  # Taille de la structure FukuroItem (20 octets)

                if len(data) != 0x14:
                    break  # Fin du fichier ou lecture incorrecte

                # Déballage des données
                unpacked = struct.unpack("<H18B", data)

                fukuro_item_entry = {
                    "fukuroNum": unpacked[0],
                    "itemID1": unpacked[1],
                    "itemID2": unpacked[2],
                    "itemID3": unpacked[3],
                    "itemID4": unpacked[4],
                    "itemID5": unpacked[5],
                    "itemID6": unpacked[6],
                    "itemID7": unpacked[7],
                    "itemID8": unpacked[8],
                    "itemID9": unpacked[9],
                    "itemID10": unpacked[10],
                    "itemID11": unpacked[11],
                    "itemID12": unpacked[12],
                    "itemID13": unpacked[13],
                    "itemID14": unpacked[14],
                    "itemID15": unpacked[15],
                    "itemID16": unpacked[16],
                    "itemID17": unpacked[17],
                    "dummy0": unpacked[18]
                }

                fukuro_item_data.append(fukuro_item_entry)

        # Sauvegarde en JSON
        with open(output_path, "w") as f_output:
            json.dump(fukuro_item_data, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_fukuro_item.dat"
output_path = "./data/dq5ds_fukuro_item.json"
read_fukuro_item(file_path, output_path)
