"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        # overrides len function
        return self.size

    def push(self, value):
        # appends value to array
        # increment size by 1
        self.storage.append(value)
        self.size += 1

    def pop(self):
        # if storage(array) is empty, just return none
        # otherwise use pop function to remove last element in stack
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.pop()
