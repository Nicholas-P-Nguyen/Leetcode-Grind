# Node class with key-value pair and a reference to the next item 
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, capacity: int):
        self.capacity = capacity
        # Initialize an empty hash table with size capacity
        self.hashTable = [None] * self.capacity
        self.size = 0
    
    # Returns a hash index for the key that is between 0 and the current size 
    def hashFunction(self, key: int) -> int:
        return key % self.size

    '''
    Insert a key-value pair with the key being the index, and value being the Node to the hash table. 
    If key doesn't exist insert new key-value pair, if key does exist replace old value with new value. 
    '''
    def insert(self, key: int, value: int) -> None:
        index = self.hashFunction(key)
        currentNode = self.hashTable[index]

        # If table is empty at current node, insert new Node
        if not currentNode:
            self.hashTable[index] = Node(key, value)
            self.size += 1
        else: 
            previousNode = None
            while currentNode:
                # Table is not empty, we find the node and replace the value
                if currentNode.key == key:
                    currentNode.value == value
                    return
                # Run this else statement until currentNode hits Null
                else:
                    previousNode, currentNode = currentNode, currentNode.next
            previousNode.next = Node(key, value)
            self.size += 1
        
        if self.size / self.capacity >= 0.5:
            self.resize()

    '''
    get() will return the value of the given key that is being passed through. 
    Return -1 if retrieval unsuccessful 
    '''          
    def get(self, key: int) -> int:
        index = self.hashFunction(key)
        currentNode = self.hashTable[index]

        while currentNode:
            if currentNode.key == key:
                return currentNode.value
            currentNode = currentNode.next
    
        return -1
    '''
    remove() will remove the key-value pair with the given key. 
    If key is not in hashtable return false, else return true
    '''
    def remove(self, key: int) -> bool:
        index = self.hashFunction(key)
        currentNode = self.hashTable[index]

        previousNode = None
        while currentNode:
            if currentNode.key == key:
                if not previousNode:
                    self.hashTable[index] = currentNode.next
                else:
                    previousNode.next = currentNode.next
                self.size -= 1
                return True

            previousNode, currentNode = currentNode, currentNode.next
        
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        pass
