import struct
import json

def read_monster_data(file_path, output_path):
    try:
        monster_data_list = []
        with open(file_path, "rb") as f:
            f.seek(0x14)
            while True:
                data = f.read(0x34)  # Taille de la structure (52 octets)

                if len(data) != 0x34:
                    break  # Fin du fichier ou lecture incorrecte

                # Déballage des données
                unpacked = struct.unpack("<15H10B11cB", data)

                monster_entry = {
                    "index": unpacked[0],
                    "HP": unpacked[1],
                    "MP": unpacked[2],
                    "attack": unpacked[3],
                    "defence": unpacked[4],
                    "money": unpacked[5],
                    "exp": unpacked[6],
                    "action1": unpacked[7],
                    "action2": unpacked[8],
                    "action3": unpacked[9],
                    "action4": unpacked[10],
                    "action5": unpacked[11],
                    "action6": unpacked[12],
                    "item": unpacked[13],
                    "animIndex": unpacked[14],
                    "party": unpacked[15],
                    "agility": unpacked[16],
                    "ratio": unpacked[17],
                    "animAll": unpacked[18],
                    "anim1": unpacked[19],
                    "anim2": unpacked[20],
                    "anim3": unpacked[21],
                    "anim4": unpacked[22],
                    "anim5": unpacked[23],
                    "anim6": unpacked[24],
                    "byte_1": unpacked[25].hex(),
                    "byte_2": unpacked[26].hex(),
                    "byte_3": unpacked[27].hex(),
                    "byte_4": unpacked[28].hex(),
                    "byte_5": unpacked[29].hex(),
                    "byte_6": unpacked[30].hex(),
                    "byte_7": unpacked[31].hex(),
                    "byte_8": unpacked[32].hex(),
                    "byte_9": unpacked[33].hex(),
                    "byte_10": unpacked[34].hex(),
                    "byte_11": unpacked[35].hex(),
                    "dummy0": unpacked[36]
                }

                monster_data_list.append(monster_entry)

        # Sauvegarde en JSON
        with open(output_path, "w") as f_output:
            json.dump(monster_data_list, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_monster.dat"
output_path = "./data/dq5ds_monster.json"
read_monster_data(file_path, output_path)
