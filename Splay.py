class Node :
    def __init__(self, key):
        self.key = key
        self.parent = self.left = self.right = None
    def __str(self) :
        return str(self.key)

class BST :
    def __init__(self):
        self.root = None
        self.size = 0
    def __len__(self) :
        return self.size
    def preorder(self,v) :
        if v :
            print(v.key, end=' ')
            self.preorder(v.left)
            self.preorder(v.right)
    def inorder(self,v) :
        if v :
            self.inorder(v.left)
            print(v.key,end=' ')
            self.inorder(v.right)
    def postorder(self,v):
        if v :
            self.postorder(v.left)
            self.postorder(v.right)
            print(v.key,end=' ')
    def find_loc(self, key) :
        if self.size == 0 : return None
        p = None
        v = self.root
        while v :
            if v.key == key : return v
            else :
                p = v
                if v.key < key : v = v.right
                else : v = v.left
        return p
    def search(self, key) :
        p = self.find_loc(key)
        if p and p.key == key : return p
        else : return None
    def insert(self, key):
        v = Node(key)
        if self.size == 0 : self.root = v
        else :
            p = self.find_loc(key)
            if p and p.key != key :
                if p.key < key : p.right = v
                else : p.left = v
                v.parent = p
        #if v: self.size += 1
        self.size += 1
        return v
    def rotate_left(self, z):
        x = z.right
        if x is None : return None
        b = x.left
        x.parent = z.parent
        if z.parent :
            if z.parent.left == z : z.parent.left = x
            else : z.parent.right = x
        if x:
            x.left = z
            z.parent = x
            z.right = b
        if b : b.parent = z
        if z == self.root and z : self.root = x
    def rotate_right(self, z) :
        x = z.left
        if x is None : return None
        b = x.right
        x.parent = z.parent
        if z.parent :
            if z.parent.left == z : z.parent.left = x
            else : z.parent.right = x
        if x :
            x.right = z
            z.parent = x
            z.left = b
        if b : b.parent = z
        if z == self.root and z is not None: self.root = x

class SplayTree(BST) :
    def splay(self, x) :
        pt = x.parent
        while pt :
            if x.parent is None or x == self.root : return x
            if pt.parent is None or pt == self.root :
                if pt.left == x : super(SplayTree,self).rotate_right(pt)
                else: super(SplayTree,self).rotate_left(pt)
            elif (pt.parent.left==pt and pt.left==x) :
                super(SplayTree,self).rotate_right(pt)
                super(SplayTree,self).rotate_right(x.parent)
            elif (pt.parent.right==pt and pt.right==x) :
                super(SplayTree,self).rotate_left(pt)
                super(SplayTree,self).rotate_left(x.parent)
            elif (pt.parent.right==pt and pt.left==x) :
                super(SplayTree,self).rotate_right(pt)
                super(SplayTree,self).rotate_left(x.parent)
            elif (pt.parent.left==pt and pt.right==x) :
                super(SplayTree,self).rotate_left(pt)
                super(SplayTree,self).rotate_right(x.parent)
            pt = x.parent
        return x
    def search(self, key):
        v = super(SplayTree, self).search(key)
        if v : self.root = self.splay(v)
        return v
    def insert(self, key):
        v = super(SplayTree, self).insert(key)
        self.root = self.splay(v)
        return v
    def delete(self, x):
        v = self.splay(x)
        l, r = v.left, v.right
        if l :
            m = l
            while m.right : m = m.right
            self.splay(m)
            m.right = None
            if r : m.right, r.parent = r, m
        elif l is None and r :
            r.parent = None
            self.root = r
        elif l is None and r is None :
            if x == self.root : self.root = None
            else :
                if x.parent.left == x : x.parent.left = None
                else : x.parent.right = None
                x.parent = None
        x.left = x.right = None
        self.size -= 1

T = SplayTree()
while True:
    cmd = input().split()
    if cmd[0] == 'insert':
        v = T.insert(int(cmd[1]))
        print("+ {0} is inserted".format(v.key))
    elif cmd[0] == 'delete':
        v = T.search(int(cmd[1]))
        T.delete(v)
        print("- {0} is deleted".format(int(cmd[1])))
    elif cmd[0] == 'search':
        v = T.search(int(cmd[1]))
        if v == None:
            print("* {0} is not found!".format(cmd[1]))
        else:
            print("* {0} is found!".format(cmd[1]))
    elif cmd[0] == 'preorder':
        T.preorder(T.root)
        print()
    elif cmd[0] == 'postorder':
        T.postorder(T.root)
        print()
    elif cmd[0] == 'inorder':
        T.inorder(T.root)
        print()
    elif cmd[0] == 'exit':
        break
    else:
        print("* not allowed command. enter a proper command!")
