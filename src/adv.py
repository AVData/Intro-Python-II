from room import Room
from player import Player
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance\n",
                     """North of you, the cave mount beckons"""),

    'foyer':    Room("Foyer",
                     """
                     Dim light filters in from the south. Dusty passages run
                     north and east.
                     """),

    'overlook': Room("Grand Overlook",
                     """
                     A steep cliff appears before you,
                     falling into the darkness. Ahead to the north, a light
                     flickers in thedistance, but there is no way across the
                     chasm.
                     """),

    'narrow':   Room("Narrow Passage",
                     """
                     The narrow passage bends here from west to north. The\n
                     smell of gold permeates the air.
                     """),

    'treasure': Room("Treasure Chamber",
                     """
                     You've found the long-lost treasure chamber! Sadly, it has
                     already been completely emptied by earlieradventurers. The
                     only exit is to the south.
                     """),
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

'''
My code here:
'''

# Make a new player object that is currently in the 'outside' room.
#
# class Room_game:
#     def __init__(player, name, description):
#         print('Your starting point is outside, my guy, do someting about it')
#         player.location = room(name, description)
#         print(player.location)
#
#         while True:
#             direction = input('[F] Foyer [O] Outside [OL] Overlook [N]\n
#                                Narrow')
#             if direction == 'N':
#                 player.location = room['outside'].n_to

new_player = input('Your name, what is, young padawan? ')
player = Player(new_player, room['outside'])

# print agreeting with for the pllayer
print(f"{player.name}, novice one, currently, you are ")

done = False


def skip_input():
    print("That, I don't understnad\n")

    def print_help_text():
        print('''
        Valid commands:
        -[n]: move north
        -[e]: move east
        -[s]: move south
        -[w]: move west
        -[q]: quit
        -[h]: help text
        ''')

# Write a loop that:


while not done:
    # * Prints the current room name
    print(player.location)
# * Prints the current description (the textwrap module might be useful here).
    for line in textwrap.wrap(player.location.print_description()):
        print(line)
    print('\n')
# * Waits for user input and decides what to do.

    command = input("A direction, you must choose: ")

# check that the command is properly formatted
    if len(command) > 2 or len(command) < 1:
        skip_input()
        continue

    if command in ['n', 's', 'e', 'w']:
        player.location = player.dip(command, player.location)
        continue

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.

# If the user enters "q", quit the game.
    if command in ['q', 'quit', 'exit']:
        done = True

    elif command in ['?', 'help']:
        print_help_text()
        continue

    else:
        skip_input()
        continue
