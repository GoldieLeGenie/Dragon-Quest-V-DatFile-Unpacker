import struct
import json

def read_meisanhin_data(file_path, output_path):
    try:
        meisanhin_data_list = []
        with open(file_path, "rb") as f:
            f.seek(0x14)
            while True:
                data = f.read(0x28)  # Taille de la structure (40 octets)

                if len(data) != 0x28:
                    break  # Fin du fichier ou lecture incorrecte

                # Déballage des données
                unpacked = struct.unpack("<7LH5BccBBB", data)

                meisanhin_entry = {
                    "message1": unpacked[0],      # uslong (32 bits)
                    "message2": unpacked[1],      # uslong (32 bits)
                    "message3": unpacked[2],      # uslong (32 bits)
                    "message4": unpacked[3],      # uslong (32 bits)
                    "mizusashiMsg": unpacked[4],  # uslong (32 bits)
                    "housekiMsg": unpacked[5],    # uslong (32 bits)
                    "migakiMsg": unpacked[6],     # uslong (32 bits)
                    "itemid": unpacked[7],        # u_short (16 bits)
                    "index": unpacked[8],         # u_char (8 bits)
                    "point3": unpacked[9],        # u_char (8 bits)
                    "point4": unpacked[10],       # u_char (8 bits)
                    "point5": unpacked[11],       # u_char (8 bits)
                    "point6": unpacked[12],       # u_char (8 bits)
                    "byte_1": unpacked[13].hex(),       # char (8 bits signé)
                    "byte_2": unpacked[14].hex(),       # char (8 bits signé)
                    "dummy0": unpacked[15],       # u_char (8 bits)
                    "dummy1": unpacked[16],       # u_char (8 bits)
                    "dummy2": unpacked[17]        # u_char (8 bits)
                }

                meisanhin_data_list.append(meisanhin_entry)

        # Sauvegarde en JSON
        with open(output_path, "w") as f_output:
            json.dump(meisanhin_data_list, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_meisanhin_data.dat"
output_path = "./data/dq5ds_meisanhin_data.json"
read_meisanhin_data(file_path, output_path)
