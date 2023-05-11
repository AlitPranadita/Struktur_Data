class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

root = Node(2)#root
root.left = Node(3) #child kiri dari root
root.right = Node(5) #child kanan dari root
root.left.left = Node(7) #child kiri dari 3
root.left.right = Node(9) #child kanan dari 3
root.right.left = Node(11) #child kiri dari 5
root.right.right = Node(13) #child kanan dari 5
root.PrintTree()

class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

root = Node(7)#root
root.left = Node(8) #child kiri dari root
root.right = Node(9) #child kanan dari root
root.left.left = Node(10) #child kiri dari 3
root.left.right = Node(11) #child kanan dari 3
root.right.left = Node(12) #child kiri dari 5
root.left.right.left = Node(13)
root.right.left.left = Node(14)
root.right.left.right = Node(15)
print(root.inorderTraversal(root))


