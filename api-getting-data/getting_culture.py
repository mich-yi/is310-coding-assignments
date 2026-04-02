import requests
import json
import os

mc_url = "https://api.mcsrvstat.us/2/mc.hypixel.net"
mc_response = requests.get(mc_url)
mc_data = mc_response.json()

print("=== Minecraft Server Data ===")
print(json.dumps(mc_data, indent=2))


EUROPEANA_KEY = os.getenv("EUROPEANA_API_KEY")

euro_url = "https://api.europeana.eu/record/v2/search.json"
params = {
    "wskey": EUROPEANA_KEY,
    "query": "Minecraft",
    "rows": 1
}

euro_response = requests.get(euro_url, params=params)
euro_data = euro_response.json()

print("\n=== Europeana Data ===")
print(json.dumps(euro_data, indent=2))


output = {
    "minecraft_server": {
        "hostname": mc_data.get("hostname"),
        "players_online": mc_data.get("players", {}).get("online"),
        "players_max": mc_data.get("players", {}).get("max"),
        "version": mc_data.get("version")
    },
    "europeana_item": None
}

if "items" in euro_data and len(euro_data["items"]) > 0:
    item = euro_data["items"][0]
    output["europeana_item"] = {
        "title": item.get("title"),
        "type": item.get("type"),
        "dataProvider": item.get("dataProvider")
    }

with open("minecraft_data.json", "w", encoding="utf-8") as f:
    json.dump(output, f, indent=2, ensure_ascii=False)

print("\nSaved to minecraft_data.json")