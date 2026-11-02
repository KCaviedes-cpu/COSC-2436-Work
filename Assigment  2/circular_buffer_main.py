# Program Description: Tests the CircularBuffer class by running a series of
#   add, delete, search, peek and clear operations on a buffer whose capacity
#   is entered by the user.
# Author: Kevin Caviedes
# Date: 11/1/2026
"""
Test circular buffer class to perform data operations
"""
# Import Circular Buffer class here
from circular_buffer import CircularBuffer


def main():
    """ main function to test the functionality of circular buffer """
    capacity = int(input('Enter Buffer Capacity:'))
    cb = CircularBuffer(capacity)

    print('1. Delete operation:')
    delete_and_show(cb)

    print('2. Add 15:')
    cb.add(15)
    print(cb)

    print('3. Add 5:')
    cb.add(5)
    print(cb)

    print('4. Delete operation:')
    delete_and_show(cb)

    print('5. Add 3:')
    cb.add(3)
    print(cb)

    print('6. Add 26:')
    cb.add(26)
    print(cb)

    print('7. Delete operation:')
    delete_and_show(cb)

    print('8. Add 76:')
    cb.add(76)
    print(cb)

    print('9. Add 105:')
    cb.add(105)
    print(cb)

    print('10. Search 48:')
    if cb.find(48):
        print('48 is in the buffer')
    else:
        print('48 is not in the buffer')

    print('11. Display items at first and last')
    print(f'{cb.peek_first()} is the first item, '
          f'and {cb.peek_last()} is the last item')

    print('12. Add all items:')
    print(f'Sum = {add_all(cb)}')

    print('13. Locate the largest/smallest item')
    buffer = cb.get_buffer()
    print(f'The largest item = {buffer[get_max_index(cb)]} '
          f'and the smallest item = {buffer[get_min_index(cb)]}')

    print('14. Clear the buffer')
    cb.clear()
    print(cb)


def add_all(cb):
    """ add all the items in the circular buffer and return the sum """
    buffer = cb.get_buffer()
    total = 0
    for i in range(cb.get_size()):
        total += buffer[(cb.get_head() + i) % cb.get_capacity()]
    return total


def get_max_index(cb):
    """ return the index (in the underlying buffer list) holding the largest
    item, or -1 if the buffer is empty """
    buffer = cb.get_buffer()
    max_index = -1
    for i in range(cb.get_size()):
        index = (cb.get_head() + i) % cb.get_capacity()
        if max_index == -1 or buffer[index] > buffer[max_index]:
            max_index = index
    return max_index


def get_min_index(cb):
    """ return the index (in the underlying buffer list) holding the smallest
    item, or -1 if the buffer is empty """
    buffer = cb.get_buffer()
    min_index = -1
    for i in range(cb.get_size()):
        index = (cb.get_head() + i) % cb.get_capacity()
        if min_index == -1 or buffer[index] < buffer[min_index]:
            min_index = index
    return min_index


def delete_and_show(cb):
    """ helper: delete the first item and display the result, or display an
    error message if the buffer is empty """
    if cb.is_empty():
        print('Buffer is empty')
    else:
        print(f'{cb.delete()} has been deleted')
        print(cb)


if __name__ == '__main__':
    main()