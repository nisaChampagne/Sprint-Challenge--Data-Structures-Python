from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length == 0:
            self.storage.add_to_head(item)
            self.current = self.storage.head
            #nothing in DLL, add item to start
        elif self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
            #still have room in DLL, add item to list
        elif self.current is self.storage.tail:
            self.storage.remove_from_head()
            self.storage.add_to_head(item)
            self.current = self.storage.head
            # if current is the last item in list
            # remove item from start
            # add this new item to the start
            # now current is the head of the DLL
        else:
            self.current.insert_after(item)
            self.storage.length += 1
            self.current = self.current.next
            self.storage.delete(self.current.next)
            # insert item after current
            # increase length of DLL by 1
            # set current to next
            # deletes the next item to allow new items
            # in DLL as long as not over capacity.

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        #empty list
        current = self.storage.head
        #start of DLL  set to variable name current
        while current is not None:
            # as long as current has a value:
            list_buffer_contents.append(current.value)
            #add value of current to end of empty list created
            current = current.next
            #and repeat with each num
        return list_buffer_contents

rb = RingBuffer(4)
rb.append(4)
rb.append(5)
rb.append(8)
rb.append(8)
print(rb.get())

rb.append(10)
rb.append(11)
rb.append(12)
rb.append(13)
print(rb.get())

# ----------------Stretch Goal-------------------
'''
Both Linked List and Arrays used to store linear 
data

pros:
    1) faster access to the elements
    2) easier to use

cons:
    1) Arrays have a fixed size while linked list are dynamic
    2) memory utilization is inefficient in arrays
'''

class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None] * capacity

    def append(self, item):
        pass

    def get(self):
        pass