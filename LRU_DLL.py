# Creating a node class
class Node:
  def __init__(self, data):
    self.data = data #adding an element to the node
    self.next = None # Initally this node will not be linked with any other node
    self.prev = None # It will not be linked in either direction
    
  
  def __repr__(self) -> str:
    return f'Node({self.data})'

# Creating a doubly linked list class
class DoublyLinkedList:
  def __init__(self):
    self.head = None # Initally there are no elements in the list
    self.tail = None
    self.count = 0

  def add_left(self, node): # Adding an element before the first element
    
    node.next = self.head # newly created node's next pointer will refer to the old head

    if self.head != None: # Checks whether list is empty or not
        self.head.prev = node # old head's previous pointer will refer to newly created node
        self.head = node # new node becomes the new head
        node.prev = None
        self.count += 1
    
    else: # If the list is empty, make new node both head and tail
      self.head = node
      self.tail = node
      node.prev = None # There's only one element so both pointers refer to null
      self.count += 1
    

  def add(self, node): # Adding an element after the last element
      
      node.prev = self.tail

      if self.tail == None: # checks whether the list is empty, if so make both head and tail as new node
        self.head = node 
        self.tail = node
        node.next = None # the first element's previous pointer has to refer to null
        self.count += 1
              
      else: # If list is not empty, change pointers accordingly
        self.tail.next = node
        node.next = None
        self.tail = node # Make new node the new tail
        self.count += 1
    

  def peek_head(self): # returns first element
    if self.head == None: # checks whether list is empty or not
      print("List is empty")
    else:
      return self.head

  
  def peek_tail(self): # returns last element
    if self.tail == None: # checks whether list is empty or not
      print("List is empty")
    else:
      return self.tail
  

  def pop_head(self): # removes and returns the first element
    if self.head == None:
      print("List is empty")

    elif self.head == self.tail:
        tmp = self.head
        self.head = None
        self.tail = None
        self.count -=1 
        return tmp
    else:
        tmp = self.head
        self.head.next.prev = None
        self.head = self.head.next
        self.count -=1
        return tmp
    
  
  def pop_tail(self): # removes and returns the last element
    if self.tail == None:
      print("List is empty")

    elif self.head == self.tail:
        tmp = self.head
        self.head = None
        self.tail = None
        self.count -=1
        return tmp
    else:
        tmp = self.tail
        self.tail.prev.next = None
        self.tail = self.tail.prev
        self.count -=1
        return tmp
        
  def del_node(self,node: Node):


    if self.count == 1:
        tmp = self.head
        self.head = None
        self.tail = None
        return tmp
    else:
        tmp = node
        node.prev.next = node.next
        node.next.prev = node.prev
        self.count -= 1
        return tmp
  

  def find(self, data):
    
    if self.head is None:
        raise Exception("Empty List!")
    else:
        current = self.head
        while current.data != data:
            
            current = current.next
            if current is None:
                return None
        
        return current
    

  def insert_after(self, temp_node, new_data): # Inserting a new node after a given node
    if temp_node == None:
      print("Given node is empty")
    
    if temp_node != None:
      new_node = Node(new_data)
      new_node.next = temp_node.next
      temp_node.next = new_node
      new_node.prev = temp_node
      if new_node.next != None:
        new_node.next.prev = new_node
      
      if temp_node == self.tail: # checks whether new node is being added to the last element
        self.tail = new_node # makes new node the new tail
    
  
  def insert_before(self, temp_node, new_data): # Inserting a new node before a given node
    if temp_node == None:
      print("Given node is empty")
    
    if temp_node != None:
      new_node = Node(new_data)
      new_node.prev = temp_node.prev
      temp_node.prev = new_node
      new_node.next = temp_node
      if new_node.prev != None:
        new_node.prev.next = new_node
      
      if temp_node == self.head: # checks whether new node is being added before the first element
        self.head = new_node # makes new node the new head

  def __repr__(self) -> str:
    current = self.head
    li = []
    while current is not None:
        li.append(str(current.data))
        current = current.next
    return "--> ".join(li)


class LRU():

    def __init__(self) -> None:

       self.dll = DoublyLinkedList()
       self.hashmap = dict()
       self.cacheCap = 5
       self.cacheSize = 0

    def load_to_cache(self, node):

        if self.dll.count >= self.cacheCap:
            self.evict(self.get_least_recent_item())
            self.dll.add_left(node)
            self.hashmap.setdefault(node.data,node)
        
        else: 
            self.dll.add_left(node)
            self.hashmap.setdefault(node.data,node)

    def evict(self,node):

        self.dll.pop_tail()
        del self.hashmap[node.data]

    def get_least_recent_item(self):

        return self.dll.peek_tail()
    
    def get_most_recent_item(self):

        return self.dll.peek_head()

    def update(self, node):
        
        self.dll.del_node(node)
        self.dll.add_left(node)

    def search(self, data):
        
        retrivedNode = self.hashmap.get(data)

        if retrivedNode is not None:

            print(f'Fast Response -> {retrivedNode.data}')
            self.update(retrivedNode)
        else:
            self.load_to_cache(Node(data))



lru = LRU()

lru.search(54)
lru.search(65)
lru.search(45)
lru.search(35)
lru.search(25)
lru.search(75)
lru.search(45)
lru.search(54)
