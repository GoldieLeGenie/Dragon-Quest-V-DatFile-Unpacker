import struct
import json

def read_monster_anim(file_path, output_path):
    try:
        monster_anim_list = []
        with open(file_path, "rb") as f:
            f.seek(0x14)
            while True:
                data = f.read(0x18)  # Taille de la structure (24 octets)

                if len(data) != 0x18:
                    break  # Fin du fichier ou lecture incorrecte

                # Déballage des données
                unpacked = struct.unpack("<f8HBBBc", data)

                monster_anim_entry = {
                    "scale": unpacked[0],    # fx32 (float)
                    "index": unpacked[1],    # u_short (16 bits)
                    "action": unpacked[2],   # u_short (16 bits)
                    "sound": unpacked[3],    # u_short (16 bits)
                    "hitframe": unpacked[4], # u_short (16 bits)
                    "wait": unpacked[5],     # u_short (16 bits)
                    "effect": unpacked[6],   # u_short (16 bits)
                    "camera": unpacked[7],   # u_short (16 bits)
                    "camera2": unpacked[8],  # u_short (16 bits)
                    "anim": unpacked[9],     # u_char (8 bits)
                    "animfile": unpacked[10],# u_char (8 bits)
                    "startframe": unpacked[11], # u_char (8 bits)
                    "byte_1": unpacked[12].hex()   # char (8 bits signé)
                }

                monster_anim_list.append(monster_anim_entry)

        # Sauvegarde en JSON
        with open(output_path, "w") as f_output:
            json.dump(monster_anim_list, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_monster_anim.dat"
output_path = "./data/dq5ds_monster_anim.json"
read_monster_anim(file_path, output_path)