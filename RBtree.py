class RBNode:
    def __init__(self, data = None):
        if data:
            self.data = data
            self.right = RBNode()
            self.left = RBNode()
            self.color = "red" #1:Red - 0:Black
        else:
            self.data = None
            self.color = "black"
            self.right = None
            self.left = None

    def is_a_leaf(self):
        if self.data == None:
            return True
        return False

class RBTree:
    def __init__(self):
        self.root = RBNode()
        self.size = 0
    
    def RB_insert(self, x):
        self.root = self.rec_RB_insert(self.root, x)
        # Root should always be black.
        self.root.color = "black"
        self.size += 1

    def rec_RB_insert(self, v, x):
        """ INSERT X INTO A TREE V """
        # Check if tree is empty || inserting into a leaf.
        if v.is_a_leaf():
            return RBNode(x)
        if v.data > x:
            v.left = self.rec_RB_insert(v.left, x)

            # Check if the left child is black:
            if v.left.color == "black":
                return v
            # Check if there are 2 red nodes in a row:
            elif (v.left.left.color == "red") or (v.left.right.color == "red"):
                if v.left.left.color == "red":
                    return self.Left_Left_fix(v)
                else:
                    return self.Left_Right_fix(v)
            else:
                return v
        else:
            v.right = self.rec_RB_insert(v.right, x)

            if v.right.color == "black":
                return v
            elif (v.right.left.color) == "red" or (v.right.right.color == "red"):
                if v.right.left.color == "red":
                    return self.Right_Left_fix(v)
                else:
                    return self.Right_Right_fix(v)
            else:
                return v

    def Left_Left_fix(self, GP):
        """ Fixes the LEFT-LEFT case given the 
        grandparent Node. """
        P = GP.left
        U = GP.right
        ### D
        if U.color == "red":
            P.color = "black"
            U.color = "black"
            GP.color = "red"
            return GP
        else:
            GP.left = P.right
            P.right = GP
        # Fix the colors
        P.color = "black"
        GP.color = "red"
        return P
    
    def Left_Right_fix(self, GP):
        P = GP.left
        U = GP.right
        # Case 1: Only recolor
        if U.color == "red":
            P.color = "black"
            U.color = "black"
            GP.color = "red"
            return GP
        # Case 3: Double rotate and recolor.
        else:
            C = P.right
            P.right = C.left
            C.left = P

            GP.left = C.right
            C.right = GP

            # Fix the colors
            C.color = "red"
            GP.color = "black"
            # Return the new root of this subtree
            return C

    def Right_Right_fix(self, GP):
        P = GP.right
        U = GP.left

        if U.color == "red":
            P.color = "black"
            U.color = "black"
            GP.color = "red"
            return GP

        else:
            GP.right = P.left
            P.left = GP
            # fix the colors
            P.color = "black"
            GP.color = "red"
            return P

    def Right_Left_fix(self, GP):
        P = GP.right
        U = GP.left
        # Case 1: Only recolor
        if U.color == "red":
            P.color = "black"
            U.color = "black"
            GP.color = "red"
            return GP
        # Case 3: Double rotate and recolor.
        else:
            C = P.left
            # Remove C's subtree as C will become parent of GP and P
            P.left = C.right
            GP.right = C.left
            # Set C as parent
            C.right = P
            C.left = GP
            # Fix the colors
            C.color = "black"
            GP.color = "red"
            # Return the new root of this subtree
            return C

    def printTree(self, node, level=0):
        if node is None:
            return
        if node.data != None:
            self.printTree(node.left, level + 1)
            print(' ' * 4 * level + '->', str(node.data) + "(" + node.color + ")")
            self.printTree(node.right, level +1)

    def getSize(self):
        return self.size

if __name__ == '__main__':
    inputdata = [8,2,200,4,7,11,18,5,15,27,40,80]
    tree = RBTree()

    for x in inputdata:
        tree.RB_insert(x)
        print("-------------")
        tree.printTree(tree.root)

    