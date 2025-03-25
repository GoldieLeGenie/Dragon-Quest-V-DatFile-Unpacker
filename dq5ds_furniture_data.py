import struct
import json

def read_furniture_data(file_path, json_path, output_path):
    try:
        
       with open(json_path, 'r') as f_json:
            items_shop = json.load(f_json)
        
       all_items = []
       furniture_list = []
       
       with open(file_path, "rb") as f:
            f.seek(0x14)  # Sauter les 20 octets du header

            while True:
                data = f.read(0x14) 
                if len(data) != 0x14:
                    break
                    
                unpacked = struct.unpack("<LHHHHHHBBBc", data)
                furniture = {
                        "message": unpacked[0],
                        "uid": unpacked[1],
                        "item": unpacked[2].to_bytes(2, 'little')[:1].hex().upper(),  
                        "gold": unpacked[3],
                        "encount": unpacked[4],
                        "openIndex": unpacked[5],
                        "flagIndex": unpacked[6],
                        "type": unpacked[7],
                        "furnIndex": unpacked[8],
                        "ListSize": unpacked[9],
                        "byte_1": unpacked[10].hex()  # Convertir byte_1 en hexadécimal
                    }

                if furniture["item"] != "00":
                    all_items.append(furniture["item"])

                item_code = furniture["item"]  
                item_name = items_shop.get(item_code, {}).get("name", "Unknown")
                furniture["item"] = item_name

                furniture_list.append(furniture)
            
       with open(output_path, "w") as f_output:
            json.dump(furniture_list, f_output, indent=4)

    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))


file_path = "./LEVELDATA/dq5ds_furniture_data.dat"  
output_path = "./data/dq5ds_furniture_data.json"
json_path = "./data/items_shop.json"
read_furniture_data(file_path, json_path, output_path)

