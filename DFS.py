class Node(object):
	 def __init__(self,name):
	 	self.name = name
	 	self.adjacencyList = [];
	 	self.visited = False

class DepthFirstSearch(object):

	def dfs(self, node):
		node.visited = True
		print("%s" %node.name)

		for n in node.adjacencyList:
			if not n.visited:
				self.dfs(n)


node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")
node6 = Node("F")
node7 = Node("G")
node8 = Node("H")

node1.adjacencyList.append(node2)
node1.adjacencyList.append(node6)
node1.adjacencyList.append(node7)
node2.adjacencyList.append(node3)
node2.adjacencyList.append(node4)
node7.adjacencyList.append(node8)
node4.adjacencyList.append(node5)


dfs = DepthFirstSearch()
dfs.dfs(node1)