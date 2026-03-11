# CLI Cultural Food Data Entry

## Description
This Python script allows a user to enter cultural food data through the terminal and save it to a file.

The script first displays example foods using the **Rich** library in a formatted table.  
The user is then asked to enter a new food, including:
- Food name
- Country or region
- Type of dish

The script shows the entered data and asks the user to confirm if it is correct. If confirmed, the data is saved to `cultural_foods.txt`. If not, the user is asked to enter the data again.

After saving, the script prints the file path so the user can locate the saved data.

## Requirements
Install the Rich library:

pip install rich

## How to Run
Navigate to the folder and run:

python cli_data_entry.py

## Output
User entries are saved to:

cultural_foods.txt