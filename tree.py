class RedBlackNode():
	"""
	A node of red black tree.
	"""

	def __init__(self, key):
		"Init."
		self.key = key
		self.red = False
		self.left = None
		self.right = None
		self.parent = None

	def __str__(self):
		return self.key


class RedBlackTree():
	"""
	A red black tree.
	"""

	nil = property(fget=lambda self: self._nil, doc="The tree nil node.")
	prototype = property(fget=lambda self: self._prototype, doc="The tree node prototype.")

	def __init__(self, prototype=RedBlackNode):
		"Init."
		self.prototype = prototype
		self._nil = self.prototype(None)
		self.root = self._nil

	def rotateLeft(self, node):
		"Rotate left at given node."
		tmp = node.right
		node.right = tmp.left

		if tmp.left != self.nil:
			tmp.left.parent = node

		tmp.parent = node.parent

		if node.parent == self.nil:
			self.root = tmp
		elif node == node.parent.left:
			node.parent.left = tmp
		else:
			node.parent.right = tmp

		tmp.left = node
		node.parent = tmp

	def rotateRight(self, node):
		"Rotate right at given node."
		tmp = node.left
		node.left = tmp.right

		if tmp.right != self.nil:
			tmp.right.parent = node

		tmp.parent = node.parent

		if node.parent == self.nil:
			self.root = tmp
		elif node == node.parent.left:
			node.parent.left = tmp
		else:
			node.parent.right = tmp

		tmp.right = node
		node.parent = tmp

	def fixup(self, node):
		"Fix up the tree starting from given node."
		while node.parent.red:
			if node.parent == node.parent.parent.left:
				tmp = node.parent.parent.right
				if tmp.red:
					node.parent.red = False
					tmp.red = False
					node.parent.parent.red = True
					node = node.parent.parent
				else:
					if node == node.parent.right:
						node = node.parent
						self.rotateLeft(node)
					node.parent.red = False
					node.parent.parent.red = True
					self.rotateRight(node.parent.parent)
			else:
				tmp = node.parent.parent.left
				if tmp.red:
					node.parent.red = False
					tmp.red = False
					node.parent.parent.red = True
					node = node.parent.parent
				else:
					if node == node.parent.left:
						node = node.parent
						self.rotateRight(node)
					node.parent.red = False
					node.parent.parent.red = True
					self.rotateLeft(node.parent.parent)
		self.root.red = False

	def insertNode(self, node):
		"Insert node into the tree."
		parent = self.nil
		actual = self.root
		while actual != self.nil:
			parent = actual
			if node.key < actual.key:
				actual = actual.left
			else:
				actual = actual.right

		node.parent = parent
		if parent == self.nil:
			self.root = node
		elif node.key < parent.key:
			parent.left = node
		else:
			parent.right = node

		node.left = self.nil
		node.right = self.nil
		node.red = True
		self.fixup(node)

	def insert(self, value):
		"Insert value into the tree."
		node = self.prototype(value)
		return self.insertNode(node)

	def search(self, value):
		"Search form node with given value."
		node = self.root
		next = node
		while True:
			if node.key == value:
				break
			elif node.key > value:
				next = node.left
			else:
				next = node.right

			if next == self._nil:
				break

			node = next

		if node.key != value or node == self._nil:
			return False
		else:
			return node

	def printTree(self, node=None, depth=1):
		"Printing tree. Usefull for test purposes only."
		if node == None:
			node = self.root

		if node == self._nil:
			return

		tab = ''
		for i in range(1, depth):
			tab += ' '

		depth2 = depth + 1

		self.printTree(node.right, depth2)
		print tab + str(node.key)
		self.printTree(node.left, depth2)

