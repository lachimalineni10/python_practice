class Node:
    def __init__(self, data):
        self.data = data
        self.ref  = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def print_LL(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.ref

    def add_node_at_begining(self, data):
        new_node        = Node(data)
        new_node.ref    = self.head
        self.head       = new_node

    def add_node_at_end(self, data):
        new_node        = Node(data)
        n               = self.head
        if self.head is None:
            self.head = new_node
        else:
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
    
    def add_node_after_a_node(self, data, x):
        n = self.head

        while n is not None:
            if n.data == x:
                break
            n = n.ref

        if n is None:
            print("Node not found")
        else:
            new_node        = Node(data)
            new_node.ref    = n.ref
            n.ref           = new_node 

    def add_node_before_a_node(self, data, x):
        n = self.head
        
        if self.head is not None and self.head.data == x:
            new_node        = Node(data)
            new_node.ref    = self.head
            self.head       = new_node
            return
        
        elif self.head is None:
            return
        
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        
        if n.ref is None:
            print(f"Node {x} Not Found")
        else:
            new_node        = Node(data)
            new_node.ref    = n.ref
            n.ref           = new_node

LL1 = LinkedList()
LL1.add_node_at_begining(20)
LL1.add_node_at_begining(10)
LL1.add_node_at_end(100)
# LL1.add_node_after_a_node(30, 20)
LL1.add_node_before_a_node(50, 1000)
print(LL1.print_LL())
