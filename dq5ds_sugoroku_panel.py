import struct
import json

def read_sugoroku_panel_list(file_path, output_path):
    try:
        sugoroku_panel_list = []
        with open(file_path, "rb") as f:
            f.seek(0x14)
            while True:
                data = f.read(0xC)  # Taille de la structure (12 octets)

                if len(data) != 0xC:
                    break  # Fin du fichier ou lecture incorrecte

                # Déballage des données
                unpacked = struct.unpack("<LLHBB", data)

                sugoroku_panel_entry = {
                    "execMsg": unpacked[0],
                    "divergentMsg": unpacked[1],
                    "panelNo": unpacked[2],
                }

                sugoroku_panel_list.append(sugoroku_panel_entry)

        # Sauvegarde en JSON
        with open(output_path, "w") as f_output:
            json.dump(sugoroku_panel_list, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_sugoroku_panel.dat"
output_path = "./data/dq5ds_sugoroku_panel.json"
read_sugoroku_panel_list(file_path, output_path)
