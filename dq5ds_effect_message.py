import struct
import json

def read_effect_message(file_path, output_path):
    try:
        effect_message_data = []
        with open(file_path, "rb") as f:
            f.seek(0x14)
            while True:
                data = f.read(0x20)  # Taille de la structure (32 octets)

                if len(data) != 0x20:
                    break  # Fin du fichier ou lecture incorrecte

                # Déballage des données
                unpacked = struct.unpack("<7LHBB", data)

                effect_entry = {
                    "ConditionMsg": unpacked[0],
                    "OriginalCondMsg": unpacked[1],
                    "PlayerCondMsg": unpacked[2],
                    "MonsterCondMsg": unpacked[3],
                    "OverlapMsg": unpacked[4],
                    "NotLapMsg": unpacked[5],
                    "NaturalClearMsg": unpacked[6],
                    "action": unpacked[7],
                    "typeID": unpacked[8],
                }

                effect_message_data.append(effect_entry)

        # Sauvegarde en JSON
        with open(output_path, "w") as f_output:
            json.dump(effect_message_data, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_effect_message.dat"
output_path = "./data/dq5ds_effect_message.json"
read_effect_message(file_path, output_path)
