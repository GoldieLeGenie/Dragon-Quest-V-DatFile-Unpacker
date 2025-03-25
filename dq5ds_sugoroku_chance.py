import struct
import json

def read_sugoroku_chance_card(file_path, output_path):
    try:
        chance_cards = []
        with open(file_path, "rb") as f:
            f.seek(0x14)
            while True:
                data = f.read(0xC)  # Taille de la structure (12 octets)

                if len(data) != 0xC:
                    break  # Fin du fichier ou lecture incorrecte

                # Déballage des données
                unpacked = struct.unpack("<LLBccB", data)

                chance_card_entry = {
                    "exec": unpacked[0],
                    "divergent": unpacked[1],
                    "chance": unpacked[2],
                    "byte_1": unpacked[3].hex(),
                    "byte_2": unpacked[4].hex(),
                    "dummy0": unpacked[5]
                }

                chance_cards.append(chance_card_entry)

        # Sauvegarde en JSON
        with open(output_path, "w") as f_output:
            json.dump(chance_cards, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_sugoroku_chance.dat"
output_path = "./data/dq5ds_sugoroku_chance.json"
read_sugoroku_chance_card(file_path, output_path)
