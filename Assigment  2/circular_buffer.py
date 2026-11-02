# Program Description: Defines a CircularBuffer class, a fixed-size FIFO data
#   structure backed by a Python list. When the buffer is full, adding a new
#   item overwrites the oldest item.
# Author: Kevin Caviedes
# Date: 11/1/2026
"""
Create circular buffer class to perform data operations
"""


class CircularBuffer:
    """ Fixed-size first-in-first-out buffer that overwrites the oldest item
    when it is full. All attributes are private. """

    # initializer
    def __init__(self, capacity):
        """ create an empty buffer of the given capacity, with every
        element set to None and size, head and tail set to 0 """
        if capacity <= 0:
            raise ValueError('Capacity must be a positive integer')
        self.__capacity = capacity
        self.__size = 0
        self.__buffer = [None] * capacity
        self.__head = 0   # index of the first (oldest) item
        self.__tail = 0   # index of the next available spot for a new item

    # getters and setter
    def get_capacity(self):
        """ return the maximum number of items the buffer can hold """
        return self.__capacity

    def set_capacity(self, capacity):
        """ change the capacity; existing items are kept in order, and if the
        new capacity is smaller only the most recent items are kept """
        if capacity <= 0:
            raise ValueError('Capacity must be a positive integer')
        items = self.__items_in_order()
        if len(items) > capacity:
            items = items[-capacity:]
        self.__capacity = capacity
        self.__buffer = [None] * capacity
        for i, item in enumerate(items):
            self.__buffer[i] = item
        self.__size = len(items)
        self.__head = 0
        self.__tail = len(items) % capacity

    def get_buffer(self):
        """ return the underlying list that stores the buffer """
        return self.__buffer

    def get_head(self):
        """ return the index of the first item """
        return self.__head

    def get_tail(self):
        """ return the index of the next available spot for a new item """
        return self.__tail

    def get_size(self):
        """ return the current number of items in the buffer """
        return self.__size

    # methods
    def add(self, item):
        """ insert item at the tail position and move the tail forward;
        if the buffer is full, the oldest item is overwritten and the head
        moves forward as well """
        was_full = self.__size == self.__capacity
        self.__buffer[self.__tail] = item
        self.__tail = (self.__tail + 1) % self.__capacity
        if was_full:
            self.__head = (self.__head + 1) % self.__capacity  # overwrite
        else:
            self.__size += 1

    def delete(self):
        """ remove and return the item at the head position, then move the
        head forward; return None if the buffer is empty """
        if self.is_empty():
            return None
        item = self.__buffer[self.__head]
        self.__buffer[self.__head] = None
        self.__head = (self.__head + 1) % self.__capacity
        self.__size -= 1
        return item

    def clear(self):
        """ reset every element to None and reset head, tail and size to 0 """
        self.__buffer = [None] * self.__capacity
        self.__head = 0
        self.__tail = 0
        self.__size = 0

    def is_empty(self):
        """ return True if the buffer holds no items, otherwise False """
        return self.__size == 0

    def peek_first(self):
        """ return the first item (at the head position) without removing it;
        return None if the buffer is empty """
        if self.is_empty():
            return None
        return self.__buffer[self.__head]

    def peek_last(self):
        """ return the last item (the one just before the tail position)
        without removing it; return None if the buffer is empty """
        if self.is_empty():
            return None
        return self.__buffer[(self.__tail - 1) % self.__capacity]

    def find(self, item):
        """ return True if item is in the buffer, otherwise False """
        return item in self.__items_in_order()

    def __items_in_order(self):
        """ helper: return a list of the items from head to tail """
        return [self.__buffer[(self.__head + i) % self.__capacity]
                for i in range(self.__size)]

    def __str__(self):
        """ return the items from head to tail, for example
        'Buffer: 5 --> 3 --> 26', or 'Buffer is empty' """
        if self.is_empty():
            return 'Buffer is empty'
        return 'Buffer: ' + ' --> '.join(str(i) for i in self.__items_in_order())