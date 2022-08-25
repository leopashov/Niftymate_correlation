import requests

url = "https://lsxpne5aa7gu5thx4ualghouds7q5slw5ab2hcsltcyxs7b75qka.arweave.net/XK72k6AHzU7M9-UAsx3UHL8OyXboA6OKS5ixeXw_7BQ"

r = requests.get(url)
if r.status_code == 200:
    data = {
        collection_obj["collection_slug"]: {
            "datetime": collection_obj["datetime"],
            "price_dictionary": {
                token_id: predicted_price
                for token_id, predicted_price in zip(collection_obj["token_ids"], collection_obj["predicted_prices"])
            }
        }
        for collection_obj in r.json()
    }
else:
    print(r.json())

# print(data["akc"]["price_dictionary"][3])
for collection_obj in r.json():
    print(collection_obj)
    print(collection_obj["datetime"])

# for key in data:
#     print(key)
#     for token in range(1,(len(data[key]["price_dictionary"]) - 5)):
#         print(data[key]["price_dictionary"][token])
    # print(type(data[key]["price_dictionary"]))