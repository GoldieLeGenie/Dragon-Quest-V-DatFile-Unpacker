import struct
import json


def read_apprise_item(file_path,output_path):
    try:
        apprise_data = []
        with open(file_path, "rb") as f:
            f.seek(0x14)  
            while True:
                data = f.read(0x28)  

                if len(data) != 0x28:
                    break  

                unpacked = struct.unpack("<9LHBB", data)

                apprise_item = {
                    "message9": unpacked[0],
                    "message1": unpacked[1],
                    "message2": unpacked[2],
                    "message3": unpacked[3],
                    "message4": unpacked[4],
                    "message5": unpacked[5],
                    "message6": unpacked[6],
                    "message7": unpacked[7],
                    "message8": unpacked[8],
                    "ID": unpacked[9],
                    "dummy0": unpacked[10],
                    "dummy1": unpacked[11]
                }

                apprise_data.append(apprise_item) 

        with open(output_path, "w") as f_output:
            json.dump(apprise_data, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

file_path = "./LEVELDATA/dq5ds_apprise_item.dat"
output_path = "./data/dq5ds_apprise_item.json"
read_apprise_item(file_path,output_path)
