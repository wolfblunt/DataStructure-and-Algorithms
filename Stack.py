class Node(object):

	def __init__(self,data):
		self.data = data
		self.nextNode = None

class Stack(object):

	def __init__(self):
		self.head = None
		self.size = 0

	def push(self,data):
		self.size += 1
		newNode = Node(data)
		if self.head is None:
			self.head = newNode
		else:
			newNode.nextNode = self.head
			self.head = newNode

	def pop(self):
		if self.head is None:
			return None

		else:
			popped = self.head.data
			self.head = self.head.nextNode
			return popped

	def traverseList(self):
		actualNode = self.head
		while actualNode is not None:
			print(actualNode.data)
			actualNode = actualNode.nextNode


stack = Stack()

while True:
	print("Push <value>")
	print("Pop")
	print("Traverse")
	print("quit")

	do = input('What would you like to do? ').split()

	operation = do[0].strip().lower()

	if operation == 'push':
		stack.push(int(do[1]))
	elif operation == 'pop':
		popped = stack.pop()

		if popped is None:
			print('Stack is empty')

		else:
			print('Popped value: ', int(popped))

	elif operation == 'traverse':
		stack.traverseList()

	elif operation =='quit':
		break

