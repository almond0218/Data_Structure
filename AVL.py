class Node:
    def __init__(self, key):
        self.key = key
        self.parent = self.left = self.right = None
        self.height = 0

    def __str(self):
        return str(self.key)


class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def preorder(self, v):
        if v != None:
            print(v.key, end=" ")
            self.preorder(v.left)
            self.preorder(v.right)

    def inorder(self, v):
        if v:
            self.inorder(v.left)
            print(v.key, end=" ")
            self.inorder(v.right)

    def postorder(self, v):
        if v:
            self.postorder(v.left)
            self.postorder(v.right)
            print(v.key, end=" ")

    def find_loc(self, key):
        if self.size == 0:
            return None
        p = None
        v = self.root
        while v:
            if v.key == key:
                return v
            else:
                p = v
                if v.key < key:
                    v = v.right
                else:
                    v = v.left
        return p

    def search(self, key):
        p = self.find_loc(key)
        if p and p.key == key:
            return p
        else:
            return None

    def insert(self, key):  # 노드들의 height 정보 update 필요
        v = Node(key)
        if self.size == 0:
            self.root = v
        else:
            p = self.find_loc(key)
            if p and p.key != key:
                if p.key < key:
                    p.right = v
                else:
                    p.left = v
                v.parent = p
            r = v
            if self.height(p.left) != self.height(p.right):
                while p != None and r.height == p.height and r:
                    p.height += 1
                    r = p
                    p = p.parent
        self.size += 1
        return v

    def deleteByCopying(self, x):
        a, b, pt = x.left, x.right, x.parent
        if a == None and b == None:
            if pt == None or x == self.root:
                self.deleteByMerging(x)
                self.size += 1
            elif pt.left == x:
                pt.left = None
            elif pt.right == x:
                pt.right = None
            h = pt
            while h and (
                h.height != self.height(h.left) + 1
                or h.height != self.height(h.right) + 1
            ):
                h.height = (
                    self.height(h.left) + 1
                    if self.height(h.left) >= self.height(h.right)
                    else self.height(h.right) + 1
                )
                h = h.parent
            x.parent = None
            self.size -= 1
            return pt
        elif a == None:
            c = m = b
            while c.left:
                c = c.left
            if x.parent == None or x == self.root:
                self.root = c
            else:
                if x == pt.right:
                    pt.right = c
                elif x == pt.left:
                    pt.left = c
            if c == m:
                h = pt
            elif c.right:
                c.right.parent = c.parent
                c.parent.left = c.right
                h = c.parent
            elif c != m:
                c.parent.left = None
                c.right, m.parent = m, c
                h = c.parent
            c.parent = pt
            rv = h
            while h and (
                h.height != self.height(h.left) + 1
                or h.height != self.height(h.right) + 1
            ):
                h.height = (
                    self.height(h.left) + 1
                    if self.height(h.left) >= self.height(h.right)
                    else self.height(h.right) + 1
                )
                h = h.parent
            self.size -= 1
            return rv
        elif a != None:
            c = m = a
            while c.right:
                c = c.right
            if x.parent == None or x == self.root:
                self.root = c
            else:
                if x == pt.right:
                    pt.right = c
                else:
                    pt.left = c
            if c == m:
                h = c
            elif c.left:
                c.left.parent, c.parent.right = c.parent, c.left
                h = c.parent
            else:
                c.parent.right = None
                c.left, m.parent = m, c
                h = c.parent
            if b:
                c.right, b.parent = b, c
            c.parent = pt
            rv = h
            while h and (
                h.height != self.height(h.left) + 1
                or h.height != self.height(h.right) + 1
            ):
                h.height = (
                    self.height(h.left) + 1
                    if self.height(h.left) >= self.height(h.right)
                    else self.height(h.right) + 1
                )
                h = h.parent
            self.size -= 1
            return rv

    def height(self, x):  # 노드 x의 height 값을 리턴
        if x == None:
            return -1
        else:
            return x.height

    def succ(self, x):
        if x == None or self.size == 1:
            return None
        s = self.find_loc(x.key)
        if s.right != None:
            s = s.right
            while s.left != None:
                s = s.left
            return s
        elif s.parent != None and s.parent.left == s:
            return s.parent
        else:
            p = s.parent
            if p == None:
                return None
            while p.parent != None and p.parent.left != p:
                p = p.parent
            return p.parent
        return None

    def pred(
        self, x
    ):  # key값의 오름차순 순서에서 x.key 값의 이전 노드(predecssor) 리턴 # x의 predecessor가 없다면 (즉, x.key가 최소값이면) None 리턴
        if x == None or self.size == 1:
            return None
        suc = self.find_loc(x.key)
        if suc.left != None:
            suc = suc.left
            while suc.right != None:
                suc = suc.right
            return suc
        elif suc.parent != None and suc.parent.right == suc:
            return suc.parent
        else:
            sp = suc.parent
            while suc.parent != None and sp.left == suc:
                if sp.parent == None:
                    return None
                if sp.parent.right == sp:
                    return sp.parent
                suc, sp = sp, sp.parent
            return None

    def rotateLeft(self, z):  # 균형이진탐색트리의 1차시 동영상 시청 필요 (height 정보 수정 필요)
        x = z.right
        if x == None:
            return None
        b = x.left
        x.parent = z.parent
        if z.parent:
            if z.parent.left == z:
                z.parent.left = x
            else:
                z.parent.right = x
        if x:
            x.left = z
            z.parent = x
            z.right = b
            if b:
                b.parent = z
        if z == self.root and z != None:
            self.root = x
        z.height = (
            self.height(z.left) + 1
            if self.height(z.left) >= self.height(z.right)
            else self.height(z.right) + 1
        )
        n = z
        while n.parent:
            np = n.parent
            if (
                self.height(np) != self.height(np.right) + 1
                or self.height(np) != self.height(np.left) + 1
            ):
                np.height = (
                    self.height(np.right) + 1
                    if self.height(np.right) >= self.height(np.left)
                    else self.height(np.left) + 1
                )
            n = n.parent

    def rotateRight(self, z):  # 균형이진탐색트리의 1차시 동영상 시청 필요 (height 정보 수정 필요)
        x = z.left
        if x == None:
            return None
        b = x.right
        x.parent = z.parent
        if z.parent:
            if z.parent.left == z:
                z.parent.left = x
            else:
                z.parent.right = x
        if x:
            x.right = z
            z.parent = x
            z.left = b
        if b:
            b.parent = z
        if z == self.root and z != None:
            self.root = x
        z.height = (
            self.height(z.right) + 1
            if self.height(z.right) >= self.height(z.left)
            else self.height(z.left) + 1
        )
        n = z
        while n.parent:
            np = n.parent
            if (
                self.height(np) != self.height(np.right) + 1
                or self.height(np) != self.height(np.left) + 1
            ):
                np.height = (
                    self.height(np.right) + 1
                    if self.height(np.right) >= self.height(np.left)
                    else self.height(np.left) + 1
                )
            n = n.parent


class AVL(BST):
    def __init__(self):
        self.root = None
        self.size = 0

    def bd(self, n):
        return self.height(n.left) - self.height(n.right)

    def rebalance(self, x, y, z):
        if z.right == y and y.right == x:
            super(AVL, self).rotateLeft(z)
            return y
        elif z.left == y and y.left == x:
            super(AVL, self).rotateRight(z)
            return y
        elif z.left == y and y.right == x:
            super(AVL, self).rotateLeft(y)
            super(AVL, self).rotateRight(z)
            return x
        elif y == z.right and x == y.left:
            super(AVL, self).rotateRight(y)
            super(AVL, self).rotateLeft(z)
            return x  # return the new 'top' node after rotations # z - y - x의 경우(linear vs. triangle)에 따라 회전해서 균형잡음

    def insert(
        self, key
    ):  # BST에서도 같은 이름의 insert가 있으므로, BST의 insert 함수를 호출하려면 # super(class_name, instance_name).method()으로 호출
        v = super(AVL, self).insert(key)
        f = pf = ppf = v  # x, y, z를 찾아 rebalance(x, y, z)를 호출
        z = y = x = None
        while self.root.height >= 2 and f.parent != None:
            f, pf, ppf = f.parent, f, pf
            if self.bd(f) != 1 and self.bd(f) != 0 and self.bd(f) != -1:
                z, y, x = f, pf, ppf
                break
        if z and y and x:
            self.rebalance(x, y, z)
        return v

    def delete(self, u):  # delete the node u
        v = self.deleteByCopying(u)  # 또는 self.deleteByMerging을 호출
        f = v  # height가 변경될 수 있는 가장 깊이 있는 노드를 리턴받아 v에 저장
        z = y = x = None
        while self.root.height >= 2 and f:
            if self.bd(f) != 1 and self.bd(f) != 0 and self.bd(f) != -1:
                z = f
                y = f.left if self.height(f.left) >= self.height(f.right) else f.right
                x = y.left if self.height(y.left) >= self.height(y.right) else y.right
                if z and y and x:
                    self.rebalance(
                        x, y, z
                    )  # break# v가 AVL 높이조건을 만족하는지 보면서 루트 방향으로 이동 # z - y - x를 정한 후, rebalance(x, y, z)을 호출
            f = f.parent


T = AVL()
while True:
    cmd = input().split()
    if cmd[0] == "insert":
        v = T.insert(int(cmd[1]))
        print("+ {0} is inserted".format(v.key))
    elif cmd[0] == "delete":
        v = T.search(int(cmd[1]))
        T.delete(v)
        print("- {0} is deleted".format(int(cmd[1])))
    elif cmd[0] == "search":
        v = T.search(int(cmd[1]))
        if v == None:
            print("* {0} is not found!".format(cmd[1]))
        else:
            print("* {0} is found!".format(cmd[1]))
    elif cmd[0] == "height":
        h = T.height(T.search(int(cmd[1])))
        if h == -1:
            print("= {0} is not found!".format(cmd[1]))
        else:
            print("= {0} has height of {1}".format(cmd[1], h))
    elif cmd[0] == "succ":
        v = T.succ(T.search(int(cmd[1])))
        if v == None:
            print("> {0} is not found or has no successor".format(cmd[1]))
        else:
            print("> {0}'s successor is {1}".format(cmd[1], v.key))
    elif cmd[0] == "pred":
        v = T.pred(T.search(int(cmd[1])))
        if v == None:
            print("< {0} is not found or has no predecssor".format(cmd[1]))
        else:
            print("< {0}'s predecssor is {1}".format(cmd[1], v.key))
    elif cmd[0] == "preorder":
        T.preorder(T.root)
        print()
    elif cmd[0] == "postorder":
        T.postorder(T.root)
        print()
    elif cmd[0] == "inorder":
        T.inorder(T.root)
        print()
    elif cmd[0] == "exit":
        break
    else:
        print("* not allowed command. enter a proper command!")
