import numpy.random as R


class SkipListNode():
	"""
	Skip list node.
	"""

	def __init__(self, key):
		self.key = key
		self._levels = {}

	def next(level=1):
		try:
			return self._levels[level]
		except KeyError:
			return None


	def set(self, node, level=1):
		self._levels[level] = node

	def getLevel(self):
		return len(self._levels)


class SkipList():
	"""
	Skip list.
	"""

	MAX_LEVEL = 16

	def __init__(self, prototype=SkipListNode):
		self._prototype = prototype
		self._head = self._prototype(None)

	def generateLevel(self):
		seed = R.randint(0, 2**self.MAX_LEVEL)
		h = 0
		found = 0

		while not found:
			h += 1
			found = seed % 2
			seed /= 2

		if h >= self.MAX_LEVEL:
			h = self.MAX_LEVEL - 1

		return h

	def search(self, value, forInsert=False):
		node = self._head

		if forInsert:
			result = {}

		for level in range(self._head.getLevel(), 0, -1):
			while next = node.next(level):
				if next.key > value:
					break
				else:
					node = next

			if forInsert:
				result[level] = node

		if forInsert:
			return result
		else:
			return node

	def addNode(self, node):
		levels = self.generateLevel
		nodes = self.search(node.key, True)
		for level in range(level, 0, -1):
			try:
				prevnode = nodes[level]
			except KeyError:
				prevnode = self._head

			node.set(prevnode.next(), level)
			prevnode.set(node, level)

	def addValue(self, value):
		node = self._prototype()
		node.key = value
		return self.addNode(node)