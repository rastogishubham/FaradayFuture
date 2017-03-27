#!/usr/bin/env python2.7
import collections


class ItemList:

    # Initialization of class
    def __init__(self, items_to_store):
        self.item_list = items_to_store

    def __len__(self):
        return len(self.item_list)

    # Function to get the unique items of the list
    def get_unique_items(self):
        return list(set(self.item_list))

    # Function to get the items and their frequencies from the list
    def get_item_and_frequency(self):
        return dict(collections.Counter(self.item_list))

    # Function to append a list of items or an item to the list
    def append_to_list(self, items):
        if type(items) is list:
            self.item_list.extend(items)
        else:
            self.item_list.append(items)

    # Function to insert an item or a list of items in an index in the list
    def insert_in_list(self, items, index):
        if type(items) is list:
            self.item_list[index:index] = items
        else:
            self.item_list.insert(index, items)

if __name__ == "__main__":
    newList = ItemList([1, 2, 3])
    print "List after initial initialization:"
    print newList.item_list
    newList.append_to_list(3)
    print ''
    print ''
    print "List after appending 3 to it:"
    print newList.item_list
    newList.append_to_list([4, 4, 5, 6])
    print ''
    print ''
    print "List after appending a list [4, 4, 5, 6] to it:"
    print newList.item_list
    newList.insert_in_list(6, 3)
    print ''
    print ''
    print "List after inserting the number 6 at index 3:"
    print newList.item_list
    newList.insert_in_list([1, 1, 3], 4)
    print ''
    print ''
    print "List after inserting the list [1, 1, 3] at index 4:"
    print newList.item_list
    print ''
    print ''
    print "Dictionary of items and their frequency:"
    print newList.get_item_and_frequency()
    print ''
    print ''
    print "List of all unique items:"
    print newList.get_unique_items()