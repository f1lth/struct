from queue import Queue
import binarySearchTree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def traverse_inOrder(cur):
        if cur == None:
            return
        Tree.traverse_inOrder(cur.left)
        print(cur.data)
        Tree.traverse_inOrder(cur.right)
    
    def traverse_inOrderTree(self):
        cur = self.root.data
        if cur == None:
            return

        Tree.traverse_inOrder(cur.left)
        print(cur.data)
        Tree.traverse_inOrder(cur.right)

    def traverse_postOrder(cur):
        if cur == None:
            return
        Tree.traverse_postOrder(cur.left)
        Tree.traverse_postOrder(cur.right)
        print(cur.data)
    
    def traverse_preOrder(cur):
        if cur == None:
            return
        print(cur.data)
        Tree.traverse_preOrder(cur.left)
        Tree.traverse_preOrder(cur.right)

    def traverse_byLevel(cur):
        Q = Queue()
        Q.enqueue(cur)
        # Print each level from left to right.
        while Q.isEmpty() is False:
            temp = Q.dequeue()
            print(temp.data)
            if temp.left is not None:
                Q.enqueue(temp.left)
            if temp.right is not None:
                Q.enqueue(temp.right)

    def insertIter(self, v):
        newNode = Node(v)
        # Is this an empty tree?
        if self.root == None:
            self.root = newNode
        else:
            cur = self.root
            done = False
        # Should we put v into left or right tree?
        while not done:
            if v > cur.data:
                if cur.right == None:
                    cur.right = newNode
                    done = True
                else:
                    cur = cur.right
            else:
                if cur.left == None:
                    cur.left = newNode
                    done = True

    def insertRec(self, v):
        try:
            cur = self.root
        except: 
            tree = Tree()
            tree.root = Node(v)
            return tree
        if v > cur.data:
            cur.right = Tree.insertRec(cur.right, v)
        else:
            cur.left = Tree.insertRec(cur.left, v)
        return cur

    
    def searchTreeRec(v, cur):
        if cur == None:
            return False
        elif v == cur.data:
            return True
        elif v < cur.data:
            return searchTreeRec(v, cur.left)
        else:
            return searchTreeRec(v, cur.right)
    
    def searchTreeIter(v, cur):
        while cur != None:
            if v == cur.data:
                return True
            elif v < cur.data:
                cur = cur.left
            else:
                cur = cur.right
        return False
        
if __name__ == '__main__':
    """
    ##### CREATE TREE(S) #####
    """ 
    bst = Tree()
    bst.root = Node(13)
    bst.root.left = Node(7)
    bst.root.right = Node(17)
    bst.root.left.left = Node(4)
    bst.root.right.right = Node(19)
    bst.root.right.right.left = Node(14)
    bst.insertRec(20)

    root2 = Node("F")
    root2.left = Node("B")
    root2.right = Node("G")
    root2.left.left = Node("A")
    root2.left.right = Node("D")
    root2.left.right.left = Node("C")
    root2.left.right.right = Node("E")
    root2.right.right = Node("I")
    root2.right.right.left = Node("H")

    root1 = Node(13)
    root1.left = Node(7)
    root1.right = Node(17)
    root1.left.left = Node(4)
    root1.right.right = Node(19)
    root1.right.right.left = Node(14)


    bst.traverse_inOrder3()
    print()
    '''
    Tree.traverse_preOrder(root)
    print()
    Tree.traverse_postOrder(root)
    print()
    Tree.traverse_byLevel(bst.root)
    '''
    print(binarySearchTree.searchTreeRec(19, root1))
    print(binarySearchTree.searchTreeIter(19, root1))
