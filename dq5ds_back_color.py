import struct
import json


def read_back_color(file_path,output_path):
    try:
        back_color = []
        with open(file_path, "rb") as f:
            f.seek(0x14)  
            while True:
                data = f.read(0x18)  

                if len(data) != 0x18:
                    break  

                unpacked = struct.unpack("<24B", data)

                color = {
                    "colorR1": unpacked[0],
                    "colorG1": unpacked[1],
                    "colorB1": unpacked[2],
                    "colorR2": unpacked[3],
                    "colorG2": unpacked[4],
                    "colorB2": unpacked[5],
                    "colorR3": unpacked[6],
                    "colorG3": unpacked[7],
                    "colorB3": unpacked[8],
                    "colorR4": unpacked[9],
                    "colorG4": unpacked[10],
                    "colorB4": unpacked[11],
                    "colorR5": unpacked[12],
                    "colorG5": unpacked[13],
                    "colorB5": unpacked[14],
                    "colorR6": unpacked[15],
                    "colorG6": unpacked[16],
                    "colorB6": unpacked[17],
                    "colorR7": unpacked[18],
                    "colorG7": unpacked[19],
                    "colorB7": unpacked[20],
                    "colorR8": unpacked[21],
                    "colorG8": unpacked[22],
                    "colorB8": unpacked[23],
                }

                back_color.append(color) 

        with open(output_path, "w") as f_output:
            json.dump(back_color, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

file_path = "./LEVELDATA/dq5ds_back_color.dat"
output_path = "./data/dq5ds_back_color.json"
read_back_color(file_path,output_path)
