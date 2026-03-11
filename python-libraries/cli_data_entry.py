from rich.console import Console
from rich.table import Table
import os

console = Console()

console.print("Here is some initial data:", style="bold cyan")

table = Table(title="Cultural Foods")
table.add_column("Food", style="cyan", no_wrap=True)
table.add_column("Country/Region", style="magenta")
table.add_column("Type", style = "yellow", justify="right")
table.add_row("Kimchi", "Korea", "Side dish")
table.add_row("Okonomiyaki", "Japan", "Savory pancake")
table.add_row("Pho", "Vietnam", "Noodle soup")
table.add_row("Jollof", "Nigeria", "Rice dish")

console.print(table)

console.print("\n[bold cyan]Now I want you to enter a new cultural food:[/bold cyan]")

while True:
    food = input("Enter the name of the food: ")
    region = input("Enter the country or region: ")
    food_type = input("What's the type of dish?: ")

    console.print("You entered:", style= "bold cyan")
    console.print("Food: " + food)
    console.print("Country/Region " + region)
    console.print("Dish Type: " + food_type)

    correct = console.input("Is this correct? (type yes or no)")

    if correct.lower() == 'yes':
        break
    else:
        print("Please enter the data again")


with open ('cultural_foods.txt', 'a') as file:
    file.write(food + ',' + region + ',' + food_type + '\n')

path = os.path.abspath ('cultural_foods.txt')
print ("Data saved!")
print("File location: " + path)

