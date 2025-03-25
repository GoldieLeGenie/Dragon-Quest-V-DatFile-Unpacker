import struct
import json


def read_bank_message(file_path,output_path):
    try:
        bank_data = []
        with open(file_path, "rb") as f:
            f.seek(0x14)  
            while True:
                data = f.read(0x8)  

                if len(data) != 0x8:
                    break  

                unpacked = struct.unpack("<LcBBB", data)

                bank = {
                    "message1": unpacked[0],
                    "byte_1": unpacked[1].hex(),
                    "dummy0": unpacked[2],
                    "dummy1": unpacked[3],
                    "dummy2": unpacked[4],
                }

                bank_data.append(bank) 

        with open(output_path, "w") as f_output:
            json.dump(bank_data, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))


file_path = "./LEVELDATA/dq5ds_bank_message.dat"
output_path = "./data/dq5ds_bank_message.json"
read_bank_message(file_path,output_path)
