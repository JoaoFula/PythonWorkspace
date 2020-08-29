class Node(object):
    def __init__(self, d, n=None):
        self.data = d
        self.nextNode = n

    def getNext(self):
        return self.nextNode

    def getData(self):
        return self.data

    def setNext(self, n):
        self.nextNode = n

    def setData(self, d):
        self.data = d

class LinkedList(object):
    def __init__(self, r = None):
        self.root = r
        self.size = 0

    def get_size(self):
        return self.size

    def add(self, d):
        newNode = Node(d, self.root)
        self.root = newNode
        self.size += 1

    def remove(self, d):
        thisNode = self.root
        prevNode = None

        while thisNode:
            if thisNode.getData() == d:
                if prevNode:
                    prevNode.setNext(thisNode.getNext())
                else:
                    self.root = thisNode.getNext()
                    self.size -= 1
                    return True # data has been removed
            else:
                prevNode = thisNode
                thisNode = thisNode.getNext()
            return False # if it does not find any data

    def find(self, d):
        thisNode = self.root
        while thisNode:
            if thisNode.getData() == d:
                return d
            else:
                thisNode = thisNode.getNext()
        return None

myList = LinkedList()
myList.add(5)
myList.add(8)
myList.add(12)
myList.remove(8)
print(myList.remove(12))
print(myList.find(5))