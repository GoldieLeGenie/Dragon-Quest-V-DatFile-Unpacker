import struct
import json

def read_church_message(file_path, output_path):
    try:
        church_messages = []
        with open(file_path, "rb") as f:
            f.seek(0x14)  
            while True:
                data = f.read(0xC)  

                if len(data) != 0xC:
                    break  

                unpacked = struct.unpack("<LLcBBB", data)

                church_msg = {
                    "message1": unpacked[0],
                    "message2": unpacked[1],
                    "byte_1": unpacked[2].hex(),
                    "dummy0": unpacked[3],
                    "dummy1": unpacked[4],
                    "dummy2": unpacked[5],
                }

                church_messages.append(church_msg)

        with open(output_path, "w") as f_output:
            json.dump(church_messages, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

file_path = "./LEVELDATA/dq5ds_church_message.dat"
output_path = "./data/dq5ds_church_message.json"
read_church_message(file_path, output_path)
