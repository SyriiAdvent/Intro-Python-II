from room import Room
from player import Player


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
is_playing = True

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])


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

def check_route(player_loc, choice):
    dir = choice + "_to"
    if hasattr(player_loc, dir):
        player.loc = getattr(player_loc, dir)
    else:
        print(f"\n You looked but don't see anything in that direction.")

while is_playing != 'q':
    print(f" \n {player.loc} \n")
    user_input = input("Which way will you go now? (N, W, S, E): ").lower()

    if user_input == 'n':
        check_route(player.loc, user_input)
    elif user_input == 'w':
        check_route(player.loc, user_input)
    elif user_input == 'e':
        check_route(player.loc, user_input)
    elif user_input == 's':
        check_route(player.loc, user_input)
    elif user_input == 'q':
        is_playing = user_input