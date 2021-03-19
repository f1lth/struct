"""
AUTHOR: MAX KANG
S#: 20172211
CISC 235 - A1
PROGRAM: List based Stack
"""
class Stack:
    def __init__(self):
        """ Initialize the Stack """
        self.stack = []
        self.count = 0

    def isEmpty(self):
        """ Return True if stack is empty. """
        return self.stack == []

    def push(self, item):
        """ Add an item to the top of the stack """
        self.stack.append(item)
        self.count += 1
    
    def pop(self):
        """ Remove and return the top element. """
        self.count -= 1
        return self.stack.pop()

    def top(self):
        """ Return the top element. """
        return self.stack[len(self.stack) - 1]

    def size(self):
        """ Return the size of the stack. """
        return self.count

if __name__ == '__main__':
    # Testing code.
    S = Stack()
    S.push(1)
    S.push(2)
    S.push(3)
    S.pop()
    print('Top of the stack is: ', S.top())
    print('Size of stack: ', S.size())
    print('Is the stack empty? ', S.isEmpty())

