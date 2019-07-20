class Node(object):

	def __init__(self,data):
		self.data = data
		self.nextNode = None

class LinkedList(object):

	def __init__(self):

		self.head = None
		self.size = 0;

	def insertBefore(self, data):
		self.size += 1
		newNode = Node(data)

		if not self.head:
			self.head = newNode;

		else:
			newNode.nextNode = self.head
			self.head = newNode;

	def insertEnd(self,data):
		self.size += 1
		newNode = Node(data)
		actualNode = self.head;

		while actualNode.nextNode is not None:
			actualNode = actualNode.nextNode

		actualNode.nextNode = newNode

	def traverseList(self):
		actualNode = self.head

		while actualNode is not None:
			print(actualNode.data)
			actualNode = actualNode.nextNode


linkedlist = LinkedList();
linkedlist.insertBefore(12);
linkedlist.insertBefore(13);
linkedlist.insertBefore(14);
linkedlist.insertBefore(15);
linkedlist.insertEnd(5);
linkedlist.insertEnd(4);
linkedlist.insertEnd(3);
linkedlist.insertEnd(2);

linkedlist.traverseList()



