import cloudscraper
from bs4 import BeautifulSoup
import csv

url = "https://stardewvalleywiki.com/Crops"

scraper = cloudscraper.create_scraper()
response = scraper.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

data = []
current_season = None

content = soup.find("div", class_="mw-parser-output")

for tag in content.find_all(["h2", "h3"]):
    # season sections
    if tag.name == "h2":
        season_text = tag.get_text(" ", strip=True)
        if "Spring Crops" in season_text:
            current_season = "Spring"
        elif "Summer Crops" in season_text:
            current_season = "Summer"
        elif "Fall Crops" in season_text:
            current_season = "Fall"
        elif "Winter Crops" in season_text:
            current_season = "Winter"
        elif "Special Crops" in season_text:
            current_season = "Special"

    elif tag.name == "h3" and current_season:
        crop_name = tag.get_text(" ", strip=True)

        crop_name = " ".join(crop_name.split())

        skip = [
            "Monsters", "Crows", "Farm Animals", "Fertilizing and Planting",
            "Trellis Crops", "Grow Times", "End of Season",
            "Giant Crops", "Crop Quality", "Gold per Day"
        ]

        if crop_name not in skip:
            data.append({
                "name": crop_name,
                "season": current_season
            })

print(data[:10])
print(f"scraped {len(data)} crops")

with open("crops.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "season"])
    writer.writeheader()
    writer.writerows(data)

print("saved crops.csv")