class Node(object):
	def __init__(self,data):
		self.data = data
		self.nextNode = None

class Queue(object):
	def __init__(self):
		self.head = None
		self.last = None
		self.size = 0

	def enqueue(self,data):
		self.size += 1

		if self.last is None:
			self.head = Node(data)
			self.last = self.head
		else:
			self.last.nextNode = Node(data)
			self.last = self.last.nextNode

	def dequeue(self):
		if self.head is None:
			return None

		else:
			returned = self.head.data
			self.head = self.head.nextNode
			return returned

	def traverseList(self):
		actualNode = self.head

		while actualNode is not None:
			print(actualNode.data)
			actualNode = actualNode.nextNode


queue = Queue()

while True:
	print("Enqueue <value>")
	print("Dequeue")
	print("Traverse")
	print("Quit")

	do = input("What would you like to do? ").split()

	operation = do[0].strip().lower()

	if operation == "enqueue":
		queue.enqueue(int(do[1]))

	elif operation == "dequeue":
		dequeued = queue.dequeue()

		if dequeued is None:
			print("Queue is empty")
		else:
			print("dequeued element : ", int(dequeued))

	elif operation == "traverse":
		queue.traverseList()

	elif operation == "quit":
		break
			