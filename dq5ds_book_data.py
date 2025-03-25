import struct
import json

def read_book_data(file_path, output_path):
    try:
        book_data = []
        with open(file_path, "rb") as f:
            f.seek(0x14)  
            while True:
                data = f.read(0x4)  

                if len(data) != 0x4:
                    break  

                unpacked = struct.unpack("<HBB", data)

                book = {
                    "index": unpacked[0],  
                    "friendly": unpacked[1],  
                    "dummy0": unpacked[2],  
                }

                book_data.append(book)

        with open(output_path, "w") as f_output:
            json.dump(book_data, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

file_path = "./LEVELDATA/dq5ds_book_data.dat"
output_path = "./data/dq5ds_book_data.json"
read_book_data(file_path, output_path)