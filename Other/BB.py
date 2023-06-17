from time import sleep

total_cost = 0

def check_for_spelling(thing, options):
    while thing not in options:
        thing = input("Check your spelling!\n>>")
    return thing

def yes_no_formatting(vegetable, vegetable_type):
    global total_cost
    if vegetable == "yes":
        total_cost += prices[vegetable_type]
        vegetable = ", " + vegetable_type
    else:
        vegetable = ""
    return vegetable

prices = {
    "plain" : 30,
    "salted" : 32,
    "beef" : 100,
    "pork" : 80,
    "chicken" : 79,
    "fried chicken" : 86,
    "cheese" : 20,
    "tomatoes" : 10,
    "onions" : 15,
    "lettuce" : 5,
    "pickles" : 5,
    "bacon" : 25,
    "jalapenos peppers" : 20,
    "fried onions" : 15,
    "ketchup" : 5,
    "mayo" : 7,
    "BBQ" : 12,
    "hot" : 9,
    "ranch" : 12,
    "honey mustard" : 12,
}

print("Welcome to Build Burgers. Here you build your own burger. Let's start with a bun.\n")
sleep(3)

bun = input("What bun would you like? (plain or salted)\n>>").lower()
bun = check_for_spelling(bun, ["salted", "plain"])
total_cost += prices[bun]

meat = input("Now, let's pick a kind of meat (beef, pork, chicken or fried chicken)\n>>").lower()
meat = check_for_spelling(meat, ["beef", "pork", "chicken", "fried chicken"])
total_cost += prices[meat]

cheese = input("Great choice! Would you like a slice of a cheese on it? (yes or no)\n>>").lower()
cheese = check_for_spelling(cheese, ["yes", "no"])
cheese = yes_no_formatting(cheese, "cheese")

print("Now let's pick some vegetables (yes or no)")

tomatoes = input("Tomatoes?\n>>").lower()
tomatoes = check_for_spelling(tomatoes, ["yes", "no"])
tomatoes = yes_no_formatting(tomatoes, "tomatoes")

onions = input("Onions?\n>>").lower()
onions = check_for_spelling(onions, ["yes", "no"])
onions = yes_no_formatting(onions, "onions")

lettuce = input("Lettuce?\n>>").lower()
lettuce = check_for_spelling(lettuce, ["yes", "no"])
lettuce = yes_no_formatting(lettuce, "lettuce")

pickles = input("Pickles?\n>>").lower()
pickles = check_for_spelling(pickles, ["yes", "no"])
pickles = yes_no_formatting(pickles, "pickles")

addons = input("Would you like any addons? (bacon, jalapenos peppers, fried onions, no)\n>>").lower()
addons = check_for_spelling(addons, ["bacon", "jalapenos peppers", "fried onions", "no"])

if addons != "no":
    total_cost += prices[addons]
else:
    addons = ""

sauces = input("What sauces would you like? (ketchup, mayo, BBQ, hot, ranch, honey mustard)\n>>").lower()
sauces = check_for_spelling(sauces, ["ketchup", "mayo", "BBQ", "hot", "ranch", "honey mustard"])

total_cost += prices[sauces]

#final_burger = bun + " bun, " + meat + ", " + cheese_slice_option + ", " + tomatoes + onions + lettuce + pickles + addons + ", " + sauces
final_burger = f"{bun.capitalize()} bun with {meat}{cheese}{tomatoes}{onions}{lettuce}{pickles}{addons} and {sauces} sauce"

print(f"\nYour burger is: {final_burger}")
sleep(2)
print(f"Your total cost is: {total_cost}Kč")
sleep(1)
print("Enjoy your meal!")