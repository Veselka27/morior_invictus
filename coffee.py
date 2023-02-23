import re

print("> Hello, welcome to Starbucks!")

name = input("> What is your name?\n").lower().capitalize()

if name in ["Ben", "Poppy", "Loki"]:
	evil_status = input("\n> Are you evil?\n").lower()
	if evil_status == "yes":
		good_deeds = re.findall(r"\d+\.d+|\d+", input("\n> How many good deeds have you done today?\n"))[0]
		if int(good_deeds) < 4:
			print(f"\n> You are not welcome here {name}! Get out!")
			exit()

print(f"\n> Hello {name}, thank you so much for coming in today!")
	
menu = "Latte, Black Coffee, Espresso, Frappuccino, Cappuccino"

print(f"> What would you like from our today's menu, {name}?\n> Here's what we're serving: \n> {menu}")

order = input().lower()

if order == "latte":
	price = 90
	cream = input("\n> Would you like some additional whip cream?\n").lower()
	if cream == "yes":
		price += 10
		
elif order == "black coffee":
	price = 50
elif order == "espresso":
	price = 50
elif order == "frappuccino":
	price = 90
elif order == "cappuccino":
	price = 80
else:
	print("\n> Sorry we don't have that right now")
	exit()

#quantity = input("> How many coffees would you like?\n")
quantity = re.findall(r"\d+\.d+|\d+", input("\n> How many coffees would you like?\n"))[0]

total = price * int(quantity)

print(f"\n> Thank you. Your total is: {total} Kč.")

#print("\n> Okay, " + name + ", your " + quantity + " " + order + "s will be ready in a few minutes.")

if int(quantity) == 1:
	print(f"> Okay, {name} your {order.capitalize()} will be ready in a few minutes.")
else:
	print(f"> Okay {name}, your {quantity} {order.capitalize()}s will be ready in a few minutes.")