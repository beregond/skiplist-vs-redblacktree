import numpy.random as R


class SkipListNode():
	"""
	Skip list node.
	"""

	def __init__(self, key):
		self.key = key
		self._levels = {}

	def next(self, level=1):
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
	MAX_LEVEL_THRESHOLD = 2**MAX_LEVEL
	head = property(fget=lambda self: self._head, doc="The head of list.")

	def __init__(self, prototype=SkipListNode):
		"Init."
		self._prototype = prototype
		self._head = self._prototype(None)

	def generateLevel(self):
		"Generates new level with fixed probability."
		seed = 0
		level = 0
		found = 0

		while not found:
			if (seed < 2):
				seed = R.randint(0, self.MAX_LEVEL_THRESHOLD)
			level += 1
			found = seed % 2
			seed /= 2

		if level >= self.MAX_LEVEL:
			level = self.MAX_LEVEL - 1

		return level

	def search(self, value, forInsert=False):
		"""
		Search for node with given key, if forInsert is given
		return list of nodes at each level after which new node
		should be placed.
		"""
		node = self._head

		if forInsert:
			result = {}

		for level in range(self._head.getLevel(), 0, -1):
			while True:
				next = node.next(level)
				if not next:
					break

				if next.key > value:
					break
				else:
					node = next

			if forInsert:
				result[level] = node

		if forInsert:
			return result
		elif node.key == value:
			return node
		else:
			return False

	def addNode(self, node):
		"Adds new node to list."
		levels = self.generateLevel()
		nodes = self.search(node.key, True)
		for level in range(levels, 0, -1):
			try:
				node.set(nodes[level].next(level), level)
				nodes[level].set(node, level)
			except KeyError:
				self._head.set(node, level)

	def insert(self, value):
		"Adds new value to list."
		node = self._prototype(value)
		return self.addNode(node)

	def getValues(self, level=1):
		"Returns list of nodes at specified level."
		node = self._head
		result = []
		while True:
			tmp = node.next(level)
			if not tmp:
				break
			result.append(tmp.key)
			node = tmp
		return result

