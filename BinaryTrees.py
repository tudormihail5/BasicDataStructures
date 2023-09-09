class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 
def insert(root, val):
    if root is None:
        return Node(val)
    else:
        if root.val == val:
            return root
        elif root.val < val:
            root.right = insert(root.right, val)
        else:
            root.left = insert(root.left, val)
    return root

def get_min(root):
    current = root
    while (current.left):
        current = current.left
    return current.val

def get_max(root):
    current = root
    while (current.right):
        current = current.right
    return current.val

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)
