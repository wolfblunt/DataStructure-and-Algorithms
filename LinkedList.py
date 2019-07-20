class Node(object):
    def __init__(self, data):
        self.data = data;
        self.nextNode = None;

class LinkedList(object):

    def __init__(self):
        self.head = None;
        self.size = 0;

    def insertBefore(self, data):
        self.size = self.size +1;
        newNode = Node(data);

        if not self.head:
            self.head = newNode;
        else:
            newNode.nextNode = self.head;
            self.head = newNode;

    def remove(self, data):
        if self.head is None:
            return;

        self.size - self.size - 1;
        currentNode = self.head;
        previousNode = None;

        while currentNode.data != data:
            previousNode = currentNode;
            currentNode = currentNode.nextNode;

        if previousNode is None:
            self.head = currentNode.nextNode;
        else:
            previousNode.nextNode = currentNode.nextNode;

    def size1(self):
            return self.size;

    def size2(self):

        actualNode = self.head;
        size = 0;

        while actualNode is not None:
            size+=1;
            actualNode = actualNode.nextNode;

        return size;

    def insertEnd(self, data):
        self.size = self.size + 1;
        newNode = Node(data);
        actualNode = self.head;

        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode;

        actualNode.nextNode = newNode;

    def traverseList(self):
            actualNode = self.head;

            while actualNode is not None:
                print(actualNode.data);
                actualNode = actualNode.nextNode;


linkedlist = LinkedList();
linkedlist.insertBefore(12);
linkedlist.insertBefore(13);
linkedlist.insertBefore(15);
linkedlist.insertBefore(16);
linkedlist.insertEnd(22);

linkedlist.traverseList();
linkedlist.remove(13);
print(" ");
linkedlist.traverseList();

print(" ");
print(linkedlist.size2());
print(linkedlist.size1());
linkedlist.remove(22);
print(linkedlist.size1());
print();
linkedlist.traverseList();
print();
print(linkedlist.size2());




