#!/usr/bin/env python2.7


class ItemList:

    def __init__(self, items_to_store):
        self.item_list = []
        self.item_list = items_to_store

    def get_unique_items(self):
        return list(set(self.item_list))

    def get_item_and_frequency(self):
        frequency_dictionary = {}
        for item in self.item_list:
            if item not in frequency_dictionary:
                frequency_dictionary[item] = 1
            else:
                frequency_dictionary[item] += 1

        return frequency_dictionary

    def append_to_list(self, items):
        if type(items) is list:
            self.item_list.extend(items)
        else:
            self.item_list.append(items)

    def insert_in_list(self, items, index):
        if type(items) is list:
            self.item_list[index:index] = items
        else:
            self.item_list.insert(index, items)