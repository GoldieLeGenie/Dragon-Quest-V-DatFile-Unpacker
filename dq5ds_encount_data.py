import struct
import json

def read_encount_data(file_path, output_path):
    try:
        encount_data_list = []
        with open(file_path, "rb") as f:
            f.seek(0x14)
            while True:
                data = f.read(0x1C)  # Taille de la structure (28 octets)

                if len(data) != 0x1C:
                    break  # Fin du fichier ou lecture incorrecte

                # Déballage des données
                unpacked = struct.unpack("<H12B13cB", data)

                encount_entry = {
                    "bgm":unpacked[0],
                    "monsterA":unpacked[1],
                    "monsterB":unpacked[2],
                    "monsterC":unpacked[3],
                    "monsterD":unpacked[4],
                    "monsterE":unpacked[5],
                    "monsterF":unpacked[6],
                    "monsterG":unpacked[7],
                    "monsterH":unpacked[8],
                    "monsterI":unpacked[9],
                    "monsterJ":unpacked[10],
                    "particulParty":unpacked[11],
                    "tileLevel":unpacked[12],
                    "byte_1":unpacked[13].hex(),
                    "byte_2":unpacked[14].hex(),
                    "byte_3":unpacked[15].hex(),
                    "byte_4":unpacked[16].hex(),
                    "byte_5":unpacked[17].hex(),
                    "byte_6":unpacked[18].hex(),
                    "byte_7":unpacked[19].hex(),
                    "byte_8":unpacked[20].hex(),
                    "byte_9":unpacked[21].hex(),
                    "byte_10":unpacked[22].hex(),
                    "byte_11":unpacked[23].hex(),
                    "byte_12":unpacked[24].hex(),
                    "byte_13":unpacked[25].hex(),
                    "dummy0":unpacked[26],
                }

                encount_data_list.append(encount_entry)

        # Sauvegarde en JSON
        with open(output_path, "w") as f_output:
            json.dump(encount_data_list, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

# Exemple d'utilisation
file_path = "./LEVELDATA/dq5ds_encount_data.dat"
output_path = "./data/dq5ds_encount_data.json"
read_encount_data(file_path, output_path)
