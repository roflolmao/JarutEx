# BST
import gc
import sys

gc.enable()
gc.collect()

class BSTNode:
    def __init__(self, info):
        self.left = None
        self.info = info
        self.right = None
       
    def insert(self, info):
        if self.info == info:
            return
        if info < self.info:
            # ย้ายไปทางซ้าย
            if self.left != None:
                self.left.insert( info )
            else:
                self.left = BSTNode( info )
                #print("l->{}".format(info))
        # ย้ายไปทางขวา
        if info > self.info:
            if self.right != None:
                self.right.insert( info )
            else:
                self.right = BSTNode( info )
                
    def preorder(self):
        print(self.info)
        if (self.left is not None):
            self.left.preorder()
        if (self.right is not None):
            self.right.preorder()

    def inorder(self):
        if (self.left is not None):
            self.left.inorder()
        print(self.info)
        if (self.right is not None):
            self.right.inorder()

    def postorder(self):
        if (self.left is not None):
            self.left.postorder()
        if (self.right is not None):
            self.right.postorder()
        print(self.info)
    
root = BSTNode( 5 )
root.insert(3)
root.insert(7)
root.insert(1)
root.insert(0)
root.insert(2)
root.insert(4)
root.insert(6)
root.insert(9)
root.insert(8)
print("Pre-order")
root.preorder()
print("In-order")
root.inorder()
print("Post-order")
root.postorder()
