from collections import OrderedDict
import csv


class GameInventory:

    def __init__(self, inventory=None):  # constructor
        if inventory is None:
            self.inventory = {}  # if we don't get anything, we start with an empty dictionary
        else:
            self.inventory = inventory  # ...else we use the one we've got

    def display_inventory(self):
        for key, value in self.inventory.items():  # inventory.items() is an iterable... cool!
            print(value, ' ', key)
        print ('Total number of items: ', sum(self.inventory.values()))

    def add_to_inventory(self, added_items):
        item_cache = []  # to avoid iterating through multiple items of the same kind, we cache the ones we go through
        for item in added_items:
            if item in item_cache:  # if our item is in the cache, we added it already, so just keep going
                continue
            else:  # if not, then proceed to add it
                item_cache.append(item)
                ammount = added_items.count(item)
                if item in self.inventory:  # we check whether or not our item exists in the dictionary
                    self.inventory[item] += ammount  # if yes, increment it
                else:
                    self.inventory[item] = ammount  # if no, add it

    def getcharlength(self, listofelements):  # Takes a list, returns the length of its longest element
        longestlength = 0  # we need to know the element with the longest charlength to calculate spacing
        for element in listofelements:
            if len(str((element))) > longestlength:
                longestlength = len(str(element))
        return longestlength

    def print_table(self, order=None):
        longestkeylen = self.getcharlength(self.inventory.keys())  # this has to be at least 9 (or larger)
        if longestkeylen < 9:  # 9 because "item name" = 9 chars
            longestkeylen = 9
        longestvaluelen = self.getcharlength(self.inventory.values())  # same here
        if longestvaluelen < 5:  # 5 because "count" = 5 chars
            longestvaluelen = 5

        sum_of_items = 0  # to count the total number of items
        print('Inventory: ')  # table printing begins here
        print(' '+(longestvaluelen-5)*' '+'count', ' '+(longestkeylen-9)*' ', ' item name')
        print((longestkeylen + longestvaluelen + 6) * '-')

        if order == 'count,asc':  # we use OrderedDict to sort the dictionary
            sortedinv = OrderedDict(sorted(self.inventory.items(), key=lambda t: t[1]))
            for key, value in sortedinv.items():
                sum_of_items += value  # just to display the total ammount of stuff at the end
                spacelength_key = longestkeylen - (len(str(key)))  # calculate the correct ammount of spaces
                spacelenght_value = longestvaluelen - (len(str(value)))  # to make it look nice
                print(spacelenght_value*' ', value, ' ', spacelength_key*' ', key)

        elif order == 'count,desc':
            sortedinv = OrderedDict(sorted(self.inventory.items(), key=lambda t: t[1], reverse=True))
            for key, value in sortedinv.items():
                sum_of_items += value
                spacelength_key = longestkeylen - (len(str(key)))
                spacelenght_value = longestvaluelen - (len(str(value)))
                print(spacelenght_value*' ', value, ' ', spacelength_key*' ', key)

        else:
            for key, value in self.inventory.items():
                sum_of_items += value
                spacelength_key = longestkeylen - (len(str(key)))
                spacelenght_value = longestvaluelen - (len(str(value)))
                print(spacelenght_value*' ', value, ' ', spacelength_key*' ', key)

        print((longestkeylen + longestvaluelen + 6) * '-')
        print ('Total number of items: ', sum_of_items)

    def import_inventory(self, filename="test_inventory.csv"):
        reader = csv.reader(open(filename, 'r', newline=''), quoting=csv.QUOTE_NONE, escapechar="|")
        for row in reader:
            for item in row:
                if item in self.inventory:  # we check whether or not our item exists in the dictionary
                    self.inventory[item] += 1  # if yes, increment it
                else:
                    self.inventory[item] = 1  # if no, add it

    def export_inventory(self, filename="export_inventory.csv"):
        listtowrite = []  # we make a temporary list to get the format for writing
        writer = csv.writer(open(filename, 'w'), quoting=csv.QUOTE_NONE, escapechar="|")  # args handle special cases
        for key, value in self.inventory.items():  # for every key/value pair
            for i in range(value):  # we put the key (item) to the list [value] times
                listtowrite.append(key)
        writer.writerow(listtowrite)  # and finally we write it to the file


# >>>main<<<
inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}  # given by assignment
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']  # given by assignment

invhandler = GameInventory(inv)  # class instance declaration

# Demonstration of functions

invhandler.display_inventory()
print()
invhandler.add_to_inventory(dragon_loot)
print('added items...')
invhandler.display_inventory()
invhandler.import_inventory()  # note that this imports a previously exported inventory
print('imported items...')
invhandler.display_inventory()
print()
invhandler.print_table("count,desc")  # parameter can be changed to test all branches of func
invhandler.export_inventory()
