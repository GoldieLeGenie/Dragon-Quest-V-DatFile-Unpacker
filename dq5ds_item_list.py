import struct
import json

def read_item_data(file_path, output_path):
    try:
        item_data = []
        with open(file_path, "rb") as f:
            f.seek(0x14)
            while True:
                data = f.read(0x2C)  # Taille de la structure ItemData (44 octets)

                if len(data) != 0x2C:
                    break  # Fin du fichier ou lecture incorrecte

                # Déballage des données
                unpacked = struct.unpack("<4L8H4B5cBBB", data)  

                item_entry = {
                    "casino": unpacked[0],
                    "menuMes": unpacked[1],
                    "MeisanhinMsg": unpacked[2],
                    "CommentMsg": unpacked[3],
                    "BuyPrice": unpacked[4],
                    "SellPrice": unpacked[5],
                    "samall": unpacked[6],
                    "effect": unpacked[7],
                    "action": unpacked[8],
                    "battleAction": unpacked[9].to_bytes(2, 'little').hex().upper(),
                    "typeSort": unpacked[10],
                    "nameSort": unpacked[11],
                    "equipType": unpacked[12],
                    "CommentID": unpacked[13],
                    "CommentType": unpacked[14],
                    "type": unpacked[15],
                    "byte_1": unpacked[16].hex(),
                    "byte_2": unpacked[17].hex(),
                    "byte_3": unpacked[18].hex(),
                    "byte_4": unpacked[19].hex(),
                    "byte_5": unpacked[20].hex(),
                    "dummy0": unpacked[21],
                    "dummy1": unpacked[22],
                    "dummy2": unpacked[23]
                }

                item_data.append(item_entry)

        # Sauvegarde en JSON
        with open(output_path, "w") as f_output:
            json.dump(item_data, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_item_list.dat"
output_path = "./data/dq5ds_item_list.json"
read_item_data(file_path, output_path)
