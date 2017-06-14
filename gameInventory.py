from collections import OrderedDict
import csv


class GameInventory:

    def __init__(self, inventory=None):  # constructor
        if inventory is None:
            self.inventory = {}  # if we don't get anything, we start with an empty dictionary
        else:
            self.inventory = inventory  # ...else we use the one we've got

    def display_inventory(self):
        sum_of_items = 0
        for key, value in self.inventory.items():  # inventory.items() is an iterable... cool!
            sum_of_items += value
            print(value, ' ', key)
        print ('Total number of items: ', sum_of_items)

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
                sum_of_items += value
                spacelength_key = longestkeylen - (len(str(key)))
                spacelenght_value = longestvaluelen - (len(str(value)))
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
        reader = csv.reader(open(filename, 'r', newline=''))

        for row in reader:
            for item in row:
                if item in self.inventory:  # we check whether or not our item exists in the dictionary
                    self.inventory[item] += 1  # if yes, increment it
                else:
                    self.inventory[item] = 1  # if no, add it

    def export_inventory(self, filename="export_inventory.csv"):
        listtowrite = []
        writer = csv.writer(open(filename, 'w'))


# >>>main<<<
inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

invhandler = GameInventory(inv)
invhandler.display_inventory()
print()
invhandler.add_to_inventory(dragon_loot)
print('added items...')
invhandler.display_inventory()
invhandler.import_inventory()
print('imported items...')
invhandler.display_inventory()
print()
invhandler.print_table("count,desc")
invhandler.export_inventory()
