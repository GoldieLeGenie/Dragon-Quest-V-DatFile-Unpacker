
import struct
import json
def read_shop_data3(file_path,json_path, output_path):
    try:  
       
       with open(json_path, 'r') as f_json:
            items_shop = json.load(f_json)

       shops = []
       with open(file_path, "rb") as f:
            f.seek(0x14)  # Sauter les 20 octets du header

            while True:
                data = f.read(0x8) 
                if len(data) != 0x8:
                    break
                    
                unpacked = struct.unpack("<IHBB", data)
                shop_data = {
                        "price": unpacked[0],
                        "item": unpacked[1].to_bytes(2, 'little')[:1].hex().upper(),
                        "dummy0": unpacked[2],  
                        "dummy1": unpacked[3],
                    }
                
                item_code = shop_data["item"]  
                item_name = items_shop.get(item_code, {}).get("name", "Unknown")
                shop_data["item"] = item_name

                shops.append(shop_data)

       with open(output_path, "w") as f_output:
            json.dump(shops, f_output, indent=4)

    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
    except Exception as e:
        print("Erreur :", str(e))


file_path = "./LEVELDATA/dq5ds_shop_data_3.dat"  
output_path = "./data/dq5ds_shop_data_3.json"
json_path = "./data/items_shop.json"
read_shop_data3(file_path, json_path, output_path)


