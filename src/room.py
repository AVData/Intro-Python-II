# Implement a class to hold room information. This should have name and
# description attributes
'''my code'''
#
# class Room:
#     def __init__(self, name, description):
#         self.name = name
#         self.description = description
#
#     def __str__(self):
#         return f"{self.name}, {self.description}"


class Room:
    def __init__(self, name, description):
        self.name = name
        # self.subtext = subtext
        self.description = description

    # def __str_(self):
    #     return f"{self.name}"
    #
    # def print_description(self):
    #     return f"{self.subtext}"

    def __str__(self):
        return f"{self.name}"

    def print_description(self):
        return f"{self.description}"
