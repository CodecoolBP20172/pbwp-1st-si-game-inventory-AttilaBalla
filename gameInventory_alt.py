from collections import OrderedDict
import csv


def display_inventory(inventory):
        for key, value in inventory.items():  # inventory.items() is an iterable... cool!
            print(value, ' ', key)
        print ('Total number of items: ', sum(inventory.values()))


def add_to_inventory(inventory, added_items):
        item_cache = []  # to avoid iterating through multiple items of the same kind, we cache the ones we go through
        for item in added_items:
            if item in item_cache:  # if our item is in the cache, we added it already, so just keep going
                continue
            else:  # if not, then proceed to add it
                item_cache.append(item)
                ammount = added_items.count(item)
                if item in inventory:  # we check whether or not our item exists in the dictionary
                    inventory[item] += ammount  # if yes, increment it
                else:
                    inventory[item] = ammount  # if no, add it


def getcharlength(listofelements):  # Takes a list, returns the length of its longest element
        longestlength = 0  # we need to know the element with the longest charlength to calculate spacing
        for element in listofelements:
            if len(str((element))) > longestlength:
                longestlength = len(str(element))
        return longestlength


def print_table(inventory, order=None):
        longestkeylen = getcharlength(inventory.keys())  # this has to be at least 9 (or larger)
        if longestkeylen < 9:  # 9 because "item name" = 9 chars
            longestkeylen = 9
        longestvaluelen = getcharlength(inventory.values())  # same here
        if longestvaluelen < 5:  # 5 because "count" = 5 chars
            longestvaluelen = 5

        sum_of_items = 0  # to count the total number of items
        print('Inventory: ')  # table printing begins here
        print(' '+(longestvaluelen-5)*' '+'count', ' '+(longestkeylen-9)*' ', ' item name')
        print((longestkeylen + longestvaluelen + 6) * '-')

        if order == 'count,asc':  # we use OrderedDict to sort the dictionary
            sortedinv = OrderedDict(sorted(inventory.items(), key=lambda t: t[1]))
            for key, value in sortedinv.items():
                sum_of_items += value  # just to display the total ammount of stuff at the end
                spacelength_key = longestkeylen - (len(str(key)))  # calculate the correct ammount of spaces
                spacelenght_value = longestvaluelen - (len(str(value)))  # to make it look nice
                print(spacelenght_value*' ', value, ' ', spacelength_key*' ', key)

        elif order == 'count,desc':
            sortedinv = OrderedDict(sorted(inventory.items(), key=lambda t: t[1], reverse=True))
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


def import_inventory(inventory, filename="test_inventory_export.csv"):
        reader = csv.reader(open(filename, 'r', newline=''), quoting=csv.QUOTE_NONE, escapechar="|")
        for row in reader:
            for item in row:
                if item in inventory:  # we check whether or not our item exists in the dictionary
                    inventory[item] += 1  # if yes, increment it
                else:
                    inventory[item] = 1  # if no, add it


def export_inventory(inventory, filename="export_inventory.csv"):
        listtowrite = []  # we make a temporary list to get the format for writing
        writer = csv.writer(open(filename, 'w'), quoting=csv.QUOTE_NONE, escapechar="|")  # args handle special cases
        for key, value in inventory.items():  # for every key/value pair
            for i in range(value):  # we put the key (item) to the list [value] times
                listtowrite.append(key)
        writer.writerow(listtowrite)  # and finally we write it to the file


# >>>main<<<
inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}  # given by assignment
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']  # given by assignment

# Demonstration of functions

display_inventory(inv)
print()
add_to_inventory(inv, dragon_loot)
print('added items...')
display_inventory(inv)
# invhandler.import_inventory()  # note that this imports a previously exported inventory
# print('imported items...')
# invhandler.display_inventory()
# print()
# invhandler.print_table("count,desc")  # parameter can be changed to test all branches of func
# invhandler.export_inventory()
