# Write a class to hold player information, e.g. what room they are in
# currently


class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def dip(self, direction, current_loc):
        # try to move in the specified direction
        attribute = direction + '_to'

        # can we move in the specified location from our current location
        if hasattr(current_loc, attribute):
            # get the room in the specified direction
            return getattr(current_loc, attribute)

        print("You can't go that way\n")
        return current_loc
