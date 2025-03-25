import struct
import json

def read_camera_file(file_path, output_path):
    try:
        camera_data = []
        with open(file_path, "rb") as f:
            f.seek(0x14)  
            while True:
                data = f.read(0x10)  

                if len(data) != 0x10:
                    break  

                unpacked = struct.unpack("<16s", data)

                camera = {
                    "index": unpacked[0].decode('utf-8').strip('\x00'),    
                }

                camera_data.append(camera)

        with open(output_path, "w") as f_output:
            json.dump(camera, f_output, indent=4)
    
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))

file_path = "./LEVELDATA/dq5ds_camera_file.dat"
output_path = "./data/dq5ds_camera_file.json"
read_camera_file(file_path, output_path)