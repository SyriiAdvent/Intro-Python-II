from player import Player
from room import Room
from item import Item

# Declare all the rooms

room = {
    "outside": Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. 
    Dusty passages run north and east.""",
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
    ),
    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
    ),
    "shed": Room('shed', """You find yourself staring into a dark abyss, maybe a light source could help? Head back for now?"""
    ),
    "stairwell": Room("stairwell", """You walk down the solid stone stairs and your flashlight suddenly dies.""")
}


# Link rooms together

room["outside"].n_to = room["foyer"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].e_to = room["narrow"]
room["foyer"].w_to = room["shed"]
room["shed"].s_to = room["foyer"]
room["shed"].n_to = room["stairwell"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["treasure"].s_to = room["narrow"]

# Initialize items
iron_sword = Item(
    "Sword","The sword appears to be old, however you feel it still has some shine and glory!"
)
flashlight = Item(
    'Flashlight', "Appears to be rather new. It Even has batteries."
)


# Add Items to the Room
room["foyer"].items = [iron_sword]
room['overlook'].items = [flashlight]


#
# Main
#
is_playing = True

# Make a new player object that is currently in the 'outside' room.
player = Player(room["outside"])


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


def game_began():
    print(f" \n {player.loc} \n")


def action_menu():
    action_menu = input('What would you like to do next: ').lower()
    for choice in action_menu.split():
        if choice == 'move' or choice == 'go':
            direction_choice(action_menu)
        elif choice == 'drop' or choice == 'remove':
            map_items()


# User direction handler
# TODO: extract quit game
def direction_choice(choice=None):
    a = choice.split()
    
    if len(a) <= 1:
        user_input = input("Which way will you go now? (N, W, S, E): ").lower()

        if user_input == "n":
            check_route(player.loc, user_input)
        elif user_input == "w":
            check_route(player.loc, user_input)
        elif user_input == "e":
            check_route(player.loc, user_input)
        elif user_input == "s":
            check_route(player.loc, user_input)
        elif user_input == "q":
            global is_playing
            is_playing = user_input
    else:
        for direction in choice.split():
            if direction == "n":
                check_route(player.loc, direction)
            elif direction == "w":
                check_route(player.loc, direction)
            elif direction == "e":
                check_route(player.loc, direction)
            elif direction == "s":
                check_route(player.loc, direction)
            elif direction == "q":
                is_playing = direction

# Will check if a cardinal direction is a valid map direction
def check_route(player_loc, choice):
    dir = choice + "_to"
    if hasattr(player_loc, dir):
        player.loc = getattr(player_loc, dir)
    else:
        print(f"\n You looked but don't see anything in that direction.")

# Will print out all items in the current map if any
def show_items():
    if len(player.loc.items) >= 1:
        i = 1
        print(f"There appears to be something of interest in this room. \n")

        for item in player.loc.items:
            print(f"\t{str(i)}) {item.name}: {item.description}")
            print("\n")
        item_choice = input(f"Select a item to interact with: ")
        return int(item_choice)

def input_parser(a):
    s = a.lower().split()

    if len(s) > 1:
        for word in s:
            for i in player.loc.items:
                if word == i.name.lower():
                    player.items.append(i)
                    player.loc.items.remove(i)

                    # how to delete item based on its dictionary id
                    # for ids in player.loc.items:
                    #     if i.id == ids.id:
                    #         player.loc.items.remove(ids)
                    
    elif a == 'yes' or 'take':
        player.items.append(iron_sword)


# Handles the user interacting with any items in map
def map_items():
    items_amount = len(player.loc.items)
    item_choice = show_items()

    if item_choice:
        take_item = input(f"Will you take the {player.loc.items[item_choice - 1].name}: ").lower()
        input_parser(take_item)

while is_playing != "q":
    # Init Game
    game_began()

    # Deal with player interactions
    # knows how to deal with (move, go)
    # TODO pickup,drop,remove, inspect
    action_menu()

    # ask user to interact with any map items
    map_items()
    
    # User direction choice
    # direction_choice()

    # Puzzle Keys
    # for i in player.items:
    #     if i.name == 'Flashlight':
    #         room['shed']['description'] = "With your flashlight you now see theres a access hatch leading underground. Wind blows in from the south flowing into the stairwell"
