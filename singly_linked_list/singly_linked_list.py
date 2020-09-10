class Node:
    """
    Stores two pieces of data, the value, and the pointer to next_node
    1. Value
    2. Next Node

    Methods/Behavior/Operations:
    1. Get value from node
    2. Set value
    3. Get next
    4. Set next
    """
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_next(self):
        return self.next_node
    
    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    """
    Data:
    1. A reference to the head Node
    2. A reference to the tail Node
    
    Behavior/Methods/Operations:
    1. Append(Add a new node to the Node referenced by the Tail) / Add to Tail
    2. Prepend(Add a new node and point that Node's next_node at the old Head; update Head pointer)
    3. Remove Head
    4. Remove Tail
    5. Contains?
    6. Get Maximum?
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        new_node = Node(value, None)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
    
    def remove_head(self):
        # Empty list
        if self.head is None:
            return None
        # LL of one item
        if self.head.get_next() is None:
            head = self.head
            
            self.head = None
            self.tail = None

            return head.get_value()
        
        # More than one item
        value = self.head.get_value()
        self.head = self.head.get_next()
        return value

    def remove_tail(self):
        # Empty LL
        if not self.head:
            return None
        # if LL has one item only - check for head.next or check if head is same as tail
        # if self.head.get_next() is None:
        # if self.head.get_next() is None:
        if self.head == self.tail:
            val = self.head.get_value()
            self.head = None
            self.tail = None
            return val
        
        current = self.head
        # looping using while loop until we hit the second to last node
        while current.get_next() is not self.tail:
            current = current.get_next()
        # once out of the while loop, we store the current tail val and set the self.tail to
            # current which now holds the second to last node, now becoming the tail
        val = self.tail.get_value()
        self.tail = current 
        return val

    def contains(self, value):
        current = self.head
        # not really needed since while can also handle this and return false 
        # but makes it faster if there is no head to begin with
        if not self.head:
            return False
        while current:
            if current.get_value() == value:
                return True
            current = current.get_next()
        return False

    def get_max(self):
        currentMax = self.head.get_value()
        possibleMax = self.head.get_next()

        while currentMax:
            if possibleMax.get_value() > currentMax.get_value():
                currentMax = possibleMax.get_value()
            possibleMax = possibleMax.get_next()
        maxVal = currentMax
        # exits out of while loop once current's next becomes none, breaking the while loop
        return maxVal