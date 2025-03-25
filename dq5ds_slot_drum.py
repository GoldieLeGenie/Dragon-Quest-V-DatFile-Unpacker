import struct
import json

def read_slot_drum(file_path, output_path):
    try:
        slot_drums = []
        with open(file_path, "rb") as f:
            f.seek(0x14)
            while True:
                data = f.read(0x8)  # Taille de la structure (8 octets)

                if len(data) != 0x8:
                    break  # Fin du fichier ou lecture incorrecte

                # Déballage des données
                unpacked = struct.unpack("<8B", data)

                slot_drum_entry = {
                    "drum5": unpacked[0],    # u_char
                    "name": unpacked[1],     # u_char
                    "drum1": unpacked[2],    # u_char
                    "drum2": unpacked[3],    # u_char
                    "drum3": unpacked[4],    # u_char
                    "drum4": unpacked[5],    # u_char
                    "dummy0": unpacked[6],   # u_char
                    "dummy1": unpacked[7],   # u_char
                }

                slot_drums.append(slot_drum_entry)

        # Sauvegarde en JSON
        with open(output_path, "w") as f_output:
            json.dump(slot_drums, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/slot_drum_data.dat"
output_path = "./data/slot_drum_data.json"
read_slot_drum(file_path, output_path)
