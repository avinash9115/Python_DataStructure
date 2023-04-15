# Binary Tree- preorder,inorder,postorder

class Node:
    def __init__(self,data):
        self.right=None
        self.left=None
        self.data=data

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)

#preorder traversal(root->left->right)

def preorder(root):
    if root:
        print(root.data,end=" ")
        preorder(root.left)
        preorder(root.right)

# postorder traversal(left->right->root)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=" ")


root=Node(30)
root.left=Node(20)
root.right=Node(40)
root.left.left=Node(15)
root.left.right=Node(25)
# inorder(root)
postorder(root)
print()