import struct
import json

def read_split_message(file_path, output_path):
    try:
        split_messages = []
        with open(file_path, "rb") as f:
            f.seek(0x14)
            while True:
                data = f.read(0xF4)  # Taille de la structure (244 octets)

                if len(data) != 0xF4:
                    break  # Fin du fichier ou lecture incorrecte

                # Déballage des données
                unpacked = struct.unpack("<61L", data)

                split_message_entry = {
                    "branch": unpacked[0],
                    "carriageTwo": unpacked[1],
                    "aliveTwo": unpacked[2],
                    "monsterOne": unpacked[3],
                    "monsterTwo": unpacked[4],
                    "monsterOneGroup": unpacked[5],
                    "monsterTwoGroup": unpacked[6],
                    "monsterMore": unpacked[7],
                    "targetMonster": unpacked[8],
                    "venom": unpacked[9],
                    "notmanusa": unpacked[10],
                    "manusa": unpacked[11],
                    "notempty": unpacked[12],
                    "empty": unpacked[13],
                    "alive": unpacked[14],
                    "dead": unpacked[15],
                    "astoron": unpacked[16],
                    "mosyasu": unpacked[17],
                    "splitAvoid": unpacked[18],
                    "split": unpacked[19],
                    "avoid": unpacked[20],
                    "equip": unpacked[21],
                    "notEquit": unpacked[22],
                    "male": unpacked[23],
                    "female": unpacked[24],
                    "human": unpacked[25],
                    "monster": unpacked[26],
                    "jump": unpacked[27],
                    "strait": unpacked[28],
                    "wastePlace": unpacked[29],
                    "rura": unpacked[30],
                    "riremito": unpacked[31],
                    "wasteTime": unpacked[32],
                    "cofferItem": unpacked[33],
                    "cofferMonster": unpacked[34],
                    "cofferGold": unpacked[35],
                    "cofferNothing": unpacked[36],
                    "tuboItem": unpacked[37],
                    "tuboMonster": unpacked[38],
                    "tuboGold": unpacked[39],
                    "tuboNothing": unpacked[40],
                    "noTarget": unpacked[41],
                    "random1": unpacked[42],
                    "random2": unpacked[43],
                    "random3": unpacked[44],
                    "random4": unpacked[45],
                    "random5": unpacked[46],
                    "random6": unpacked[47],
                    "random7": unpacked[48],
                    "random8": unpacked[49],
                    "random9": unpacked[50],
                    "random10": unpacked[51],
                    "random11": unpacked[52],
                    "nothing": unpacked[53],
                    "special": unpacked[54],
                    "aliveOne": unpacked[55],
                    "carriageOne": unpacked[56],
                    "notvenom": unpacked[57],
                    "targetMale": unpacked[58],
                    "targetFemale": unpacked[59],
                    "targetHuman": unpacked[60]
                }

                split_messages.append(split_message_entry)

        # Sauvegarde en JSON
        with open(output_path, "w") as f_output:
            json.dump(split_messages, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_split_message.dat"
output_path = "./data/dq5ds_split_message.json"
read_split_message(file_path, output_path)
