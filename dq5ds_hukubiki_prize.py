import struct
import json

def read_hukubiki_prize(file_path, output_path):
    try:
        hukubiki_prize_data = []
        with open(file_path, "rb") as f:
            f.seek(0x14)
            while True:
                data = f.read(0x4)  # Taille de la structure HukubikiPrize (4 octets)

                if len(data) != 0x4:
                    break  # Fin du fichier ou lecture incorrecte

                # Déballage des données
                unpacked = struct.unpack("<hBB", data)  # short = h (2 octets), u_char = B (1 octet)

                hukubiki_prize_entry = {
                    "prize": unpacked[0],
                    "dummy0": unpacked[1],
                    "dummy1": unpacked[2]
                }

                hukubiki_prize_data.append(hukubiki_prize_entry)

        # Sauvegarde en JSON
        with open(output_path, "w") as f_output:
            json.dump(hukubiki_prize_data, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_hukubiki_prize.dat"
output_path = "./data/dq5ds_hukubiki_prize.json"
read_hukubiki_prize(file_path, output_path)
