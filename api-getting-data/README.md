# GETting Culture Across APIs

For this assignment, I used the Minecraft Server Status API, which provides information about Minecraft servers. I chose this API because I am interested in Minecraft.

My script performs the following steps:
- Sends a request to the Minecraft Server Status API to get data about the Hypixel Minecraft server
- Prints the server data, including hostname, player count, and version
- Uses a related search term ("Minecraft") to query the Europeana API
- Prints the Europeana response for a related cultural item
- Saves selected data from both APIs into a JSON file (`minecraft_data.json`)

This project demonstrates how data from different APIs can be connected to explore relationships between contemporary digital culture (gaming) and cultural heritage collections.

## How to Run

Make sure you have Python installed and the `requests` library:

```bash
pip install requests