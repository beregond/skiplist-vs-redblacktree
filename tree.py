
class Node():
	"""
	A node of red black tree.
	"""

	def __init__(self, key):
		"Constructor."
		self.key = key
		self.red = False
		self.left = None
		self.right = None
		self.parent = None

	def __str__(self):
		return self.key


class Tree():
	"""
	A red black tree.
	"""

	nil = property(fget=lambda self: self._nil, doc="The tree nil node.")
	prototype = property(fget=lambda self: self._prototype, doc="The tree node prototype.")

	def __init__(self, prototype=Node):
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
			node.parent.right = tmp
		else:
			node.parent.left = tmp

		tmp.right = node
		node.parent = tmp

	def fixup(self, node):
		"Fix up the tree starting from given node."
		while node.parent.red:
			if node.parent == z.parent.parent.left:
				tmp = z.parent.parent.right
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

		node._parent = parent
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
		node = self.prototype()
		node.key = value
		return self.insertNode(node)
