#Author: Jan Handl
#Improvement: Filip Vesely
#Free to use

from time import sleep

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
    "honey mustard" : 12
}


bun_list = ["salted", "plain"]
meat_list = ["beef", "pork", "chicken", "fried chicken"]
addons_list = ["bacon", "jalapenos peppers", "fried onions", "nothing"]
sauces_list = ["ketchup", "mayo", "BBQ", "hot", "ranch", "honey mustard"]

total_cost = 0

def check_for_spelling(thing, options):
    if thing == "exit":
        print(f"\n{blue_mark} Goodbye!")
        exit()
    while thing not in options:
        if thing == "exit":
            print(f"\n{blue_mark} Goodbye!")
            exit()
        thing = input(f"\n{red_mark} Check your spelling!\n>>")
    return thing

def yes_no_formatting(vegetable, vegetable_type, color):
    global total_cost
    if vegetable == "yes" or "ye" or "y":
        total_cost += prices[vegetable_type]
        vegetable = ", " + f"{color}{vegetable_type}{RESET}"
    else:
        vegetable = ""
    return vegetable

def menu_func(meal_list):
    full = ""
    for meal in meal_list:
        if meal_list.index(meal) == len(meal_list) -2:
            full += str(meal + " or ")
        elif meal_list.index(meal) == len(meal_list) -1:
            full += str(meal)
        else:
            full += str(meal + ", ")
    return full

BOLD = "\033[1m"
RESET = "\033[0m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
RED = "\033[31m"
GREEN = "\033[32m"
BROWN = "\033[33m"
PURPLE = "\033[35m"
LIGHT_GREEN = "\033[92m"

green_mark = f"{BOLD}{GREEN}[*]{RESET}"
red_mark = f"{BOLD}{RED}[*]{RESET}"
blue_mark = f"{BOLD}{CYAN}[*]{RESET}"


try:
    print(f"\n{green_mark} Welcome to {BOLD}Build Burgers{RESET}. Here you build your own burger. Let's start with a bun.\n")
    sleep(3)

    bun = input(f"{green_mark} What bun would you like? ({menu_func(bun_list)})\n>> ").lower()
    bun = check_for_spelling(bun, bun_list)
    total_cost += prices[bun]

    meat = input(f"\n{green_mark} Now, let's pick a kind of meat ({BROWN}{menu_func(meat_list)}{RESET})\n>> ").lower()
    meat = check_for_spelling(meat, meat_list)
    total_cost += prices[meat]

    cheese = input(f"\n{green_mark} Great choice! Would you like a slice of a {YELLOW}cheese{RESET} on it? (yes or no)\n>> ").lower()
    cheese = check_for_spelling(cheese, ["yes", "no"])
    cheese = yes_no_formatting(cheese, "cheese", YELLOW)

    print("\nNow let's pick some vegetables (yes or no)")

    tomatoes = input(f"{green_mark} {RED}Tomatoes?{RESET}\n>> ").lower()
    tomatoes = check_for_spelling(tomatoes, ["yes", "no"])
    tomatoes = yes_no_formatting(tomatoes, "tomatoes", RED)

    onions = input(f"{green_mark} {PURPLE}Onions?{RESET}\n>> ").lower()
    onions = check_for_spelling(onions, ["yes", "no"])
    onions = yes_no_formatting(onions, "onions", PURPLE)

    lettuce = input(f"{green_mark} {LIGHT_GREEN}Lettuce?{RESET}\n>> ").lower()
    lettuce = check_for_spelling(lettuce, ["yes", "no"])
    lettuce = yes_no_formatting(lettuce, "lettuce", LIGHT_GREEN)

    pickles = input(f"{green_mark} {GREEN}Pickles?{RESET}\n>> ").lower()
    pickles = check_for_spelling(pickles, ["yes", "no"])
    pickles = yes_no_formatting(pickles, "pickles", GREEN)

    addons = input(f"\n{green_mark} Would you like any addons? ({menu_func(addons_list)})\n>> ").lower()
    addons = check_for_spelling(addons, addons_list)

    if addons != "nothing":
        total_cost += prices[addons]
        addons = ", " + addons
    else:
        addons = ""

    sauces = input(f"\n{green_mark} What sauces would you like? ({menu_func(sauces_list)})\n>> ").lower()
    if sauces == "bbq":
        sauces == "BBQ"
    sauces = check_for_spelling(sauces, sauces_list)

    total_cost += prices[sauces]

    #final_burger = bun + " bun, " + meat + ", " + cheese_slice_option + ", " + tomatoes + onions + lettuce + pickles + addons + ", " + sauces
    final_burger = f"{bun.capitalize()} bun with {BROWN}{meat}{RESET}{cheese}{tomatoes}{onions}{lettuce}{pickles}{addons} and {sauces} sauce"

    print(f"\n{green_mark} Your burger is: {final_burger}")
    sleep(2)
    print(f"{green_mark} Your total cost is: {total_cost}Kč")
    sleep(1)
    print(f"{green_mark} Enjoy your meal!")

except KeyboardInterrupt:
    print(f"\n\n{blue_mark} Goodbye!")
