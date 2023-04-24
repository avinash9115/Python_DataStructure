class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def printTree(root):
    if root==None:
        return
    print(root.data,end=": ")
    if root.left!=None:
        print("L",root.left.data,end=",")
    if root.right!=None:
        print("R",root.right.data,end="")
    print()
    printTree(root.left)
    printTree(root.right)

def treeInput():
    rootData=int(input())
    if rootData==-1:
        return None
    
    root=Node(rootData)
    left=treeInput()
    right=treeInput()
    root.left=left
    root.right=right

    return root

def cntNodes(root):
    if root==None:
        return 0
    
    return 1+cntNodes(root.left)+cntNodes(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.data,end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")

def insert(temp,data):
    if temp==None:
        return Node(data)
    
    q=[]
    q.append(temp)

    while(len(q)>0):
        x=q[0]
        q.pop(0)

        if x.left==None:
            x.left=Node(data)
            break
        else:
            q.append(x.left)

        if x.right==None:
            x.right=Node(data)
            break
        else:
            q.append(x.right)

def search(root,data):
    if root==None:
        return False
    
    if root.data==data:
        return True
    
    return search(root.left,data) or search(root.right,data)

# root=treeInput()
# # printTree(root)
# # print(cntNodes(root))
# inorder(root)
# print()
# preorder(root)
# print()
# postorder(root)

root=Node(10)
root.left=Node(11)
root.left.left=Node(7)
root.right=Node(9)
root.right.left=Node(15)
root.right.right=Node(8)

insert(root,12)

if search(root,99):
    print("yes")
else:
    print("no")