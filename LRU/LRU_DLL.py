from DLL import DoublyLinkedList, Node


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
