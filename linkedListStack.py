"""
AUTHOR: MAX KANG
S#: 20172211
CISC 235 - A1
PROGRAM: LinkedList based Stack
"""
class Node:
    """ Nodes hold data and point to the next node. """
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Stack:
    #Implement a stack using Linked lists
    def __init__(self):
        self.head = None
        self.count = 0
    
    def push(self, data):
        """ Add an element to the top of the stack. """
        # If you are pushing to empty stack:
        if self.head is None:
            self.head = Node(data)
            self.count += 1
        else:
            newHead = Node(data)
            # Point the old head as the next link
            newHead.next = self.head
            self.head = newHead
            self.count += 1

    def pop(self):
        """ Remove and return the top element. """
        # If the stack is empty return nothing.
        if self.head is None:
            return None
        else:
            out = self.head.data
            self.head = self.head.next
            self.count -= 1
            return out
    
    def top(self):
        """ Return but do not remove top element. """
        if self.head is None:
            return None
        else:
            return self.head.data

    def isEmpty(self):
        """ True if stack is empty. """
        if self.count == 0:
            return True
        return False
    
    def size(self):
        """ Return the size of the stack. """
        return self.count

if __name__ == '__main__':
    # Testing code for the linked list stack
    S = Stack()
    print("Stack should be empty: ", S.isEmpty())

    S.push(1)
    S.push(2)
    S.push(3)
    S.push(4)
    print('The top element of the stack is: ', S.top())

    S.pop()
    S.pop()
    print('The size of the stack is now: ', S.size())
    print('The top element is: ', S.top())

    S.pop()
    S.pop()
    print('The stack should now be empty after popping 4x: ', S.isEmpty())



    