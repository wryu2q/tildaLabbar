class Node :
    ''' A node in a binary tree '''
    def __init__(self,value=None) :
        self.right = None
        self.left= None
        self.val = value

    def __lt__ (self,other) :
        return self.val < other

    def __eq__ (self,other) :
        return self.val == other

    def __str__ (self) :
        return self.val


class Bintree:
    ''' Handles the binary tree '''
    def __init__(self):
        self.root = None

    def put(self,newvalue):
        # Sorterar in newvalue i trädet
        self.root = putta(self.root,newvalue)
        #print("self.root=", self.root)
    def __contains__(self,value):
        # True om value finns i trädet, False annars
        return finns(self.root,value)

    def write(self):
        # Skriver ut trädet i inorder
        skriv(self.root)
        print("\n")


def putta (root,value) :
    '''puts none existing value in binary tree'''
    if root is None :
        return Node(value)
    
    elif root == value :
        return root
            
    elif root < value :

        root.right = putta(root.right,value)

    else :
        root.left = putta(root.left,value)
    return root


def finns (root,value) :
    '''returns true if value exist in binary tree'''
    if root is None :
        return False
    
    elif root == value :
        return True
    
    elif root < value :
        return finns(root.right,value)

    else :
        return finns(root.left,value)

    
def skriv(root) :
    '''prints whats to the left in binary tree'''
    if root is None :
        return 
    
    skriv(root.left)
    print(root)
    skriv(root.right)
    
