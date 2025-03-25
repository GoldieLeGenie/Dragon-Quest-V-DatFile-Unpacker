import struct
import json

def read_chara_init(file_path, output_path):
    try:
        chara_init_data = []
        with open(file_path, "rb") as f:
            f.seek(0x14)  # Commencer à lire à l'offset 0x14
            while True:
                data = f.read(0x58)  # Lire 88 octets (0x58 en hexadécimal)

                if len(data) != 0x58:
                    break  # Arrêter si la fin du fichier est atteinte

                # Déballer les données selon la structure
                unpacked = struct.unpack("<L37HBBBBBBcBBB", data)  # Format corrigé

                chara = {
                    "exp": unpacked[0],
                    "friendID": unpacked[1],
                    "index": unpacked[2],
                    "strength": unpacked[3],
                    "agility": unpacked[4],
                    "vitality": unpacked[5],
                    "intelligence": unpacked[6],
                    "luck": unpacked[7],
                    "HP": unpacked[8],
                    "MP": unpacked[9],
                    "gold": unpacked[10],
                    "weapon": unpacked[11],
                    "armor": unpacked[12],
                    "shield": unpacked[13],
                    "hat": unpacked[14],
                    "battle1": unpacked[15],
                    "battle2": unpacked[16],
                    "battle3": unpacked[17],
                    "battle9": unpacked[18],
                    "normal1": unpacked[19],
                    "normal2": unpacked[20],
                    "normal3": unpacked[21],
                    "normal9": unpacked[22],
                    "CGNumber": unpacked[23],
                    "job": unpacked[24],
                    "sex": unpacked[25],
                    "actionMonsterID": unpacked[26],
                    "monsterID": unpacked[27],
                    "battle4": unpacked[28],
                    "battle5": unpacked[29],
                    "battle6": unpacked[30],
                    "battle7": unpacked[31],
                    "battle8": unpacked[32],
                    "normal4": unpacked[33],
                    "normal5": unpacked[34],
                    "normal6": unpacked[35],
                    "normal7": unpacked[36],
                    "normal8": unpacked[37],
                    "equipment": unpacked[38],
                    "icon": unpacked[39],
                    "mostLv": unpacked[40],
                    "level": unpacked[41],
                    "talk1": unpacked[42],
                    "talk2": unpacked[43],
                    "byte_1": unpacked[44].hex(),
                    "dummy0": unpacked[45],
                    "dummy1": unpacked[46],
                    "dummy2": unpacked[47]
                }

                chara_init_data.append(chara)

        with open(output_path, "w") as f_output:
            json.dump(chara_init_data, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

file_path = "./LEVELDATA/dq5ds_character_init.dat"
output_path = "./data/dq5ds_character_init.json"
read_chara_init(file_path, output_path)