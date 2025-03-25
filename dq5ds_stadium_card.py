import struct
import json

def read_stadium_card(file_path, output_path):
    try:
        stadium_cards = []
        with open(file_path, "rb") as f:
            f.seek(0x14)
            while True:
                data = f.read(0x10)  # Taille de la structure (16 octets)

                if len(data) != 0x10:
                    break  # Fin du fichier ou lecture incorrecte

                # Déballage des données
                unpacked = struct.unpack("<5H6B", data)

                stadium_card_entry = {
                    "monsterID1": unpacked[0],
                    "monsterID2": unpacked[1],
                    "monsterID3": unpacked[2],
                    "monsterID4": unpacked[3],
                    "encount": unpacked[4],
                    "odds4": unpacked[5],
                    "odds1": unpacked[6],
                    "odds2": unpacked[7],
                    "odds3": unpacked[8],
                    "level": unpacked[9],
                    "dummy0": unpacked[10]
                }

                stadium_cards.append(stadium_card_entry)

        # Sauvegarde en JSON
        with open(output_path, "w") as f_output:
            json.dump(stadium_cards, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_stadium_card.dat"
output_path = "./data/dq5ds_stadium_card.json"
read_stadium_card(file_path, output_path)
