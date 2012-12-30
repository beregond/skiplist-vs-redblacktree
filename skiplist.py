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

	def __init__(self, prototype=SkipListNode):
		self._prototype = prototype
		self._head = self._prototype(None)
		self.head = self._head

	def generateLevel(self):
		seed = R.randint(0, 2**self.MAX_LEVEL)
		level = 0
		found = 0

		while not found:
			level += 1
			found = seed % 2
			seed /= 2

		if level >= self.MAX_LEVEL:
			level = self.MAX_LEVEL - 1

		return level

	def search(self, value, forInsert=False):
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
		else:
			return node

	def addNode(self, node):
		levels = self.generateLevel()
		nodes = self.search(node.key, True)
		for level in range(levels, 0, -1):
			try:
				node.set(nodes[level].next(level), level)
				nodes[level].set(node, level)
			except KeyError:
				self._head.set(node, level)

	def addValue(self, value):
		node = self._prototype(value)
		return self.addNode(node)
