import struct
import json

def read_furniture_param(file_path, output_path):
    try:  
        
       furniture_param = []
       
       with open(file_path, "rb") as f:
            f.seek(0x14)  
            while True:
                data = f.read(0x18) 
                if len(data) != 0x18:
                    break
                    
                unpacked = struct.unpack("<LLLLLHBc", data)
                furniture = {
                        "normalMsg": unpacked[0],
                        "nothingMsg": unpacked[1],
                        "monsterMsg": unpacked[2],  
                        "backMsg": unpacked[3],
                        "checkMsg": unpacked[4],
                        "sound": unpacked[5],
                        "type": unpacked[6],
                        "byte_1": unpacked[7].hex(),
                    }

                furniture_param.append(furniture)

       with open(output_path, "w") as f_output:
            json.dump(furniture_param, f_output, indent=4)

    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))


file_path = "./LEVELDATA/dq5ds_furniture_param.dat"  
output_path = "./data/dq5ds_furniture_param.json"
read_furniture_param(file_path,output_path)