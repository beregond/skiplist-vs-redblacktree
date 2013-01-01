"""
Tests for SkipList and RedBlackTree. It tests with different type of data (ordered, reversed,
and randomized) with different amount of data. Of course you should remember, that even if general,
last results are usually the same (x is better than y), percentage resulst can vary very much
(it depends on os and python itself I guess) even on the same machine.
"""

import time, random
import numpy.random as R
from tree import RedBlackTree
from skiplist import SkipList

SEARCH_AMOUNT = 10
RANDOM_DATA_LOOPS = 3

def test():
	"""
	General test form SkipList and RedBlackTree.
	"""
	general = {"list_insert": 0, "list_search": 0, "tree_insert": 0, "tree_search": 0}
	# Amount is given so SkipList should handle it without problems with its MAX_LEVEL.
	for amount in [1000, 10000, 100000]:
		print "Test for amount of data: " + str(amount)
		print
		skiplist = SkipList()
		tree = RedBlackTree()

		data = range(0, amount)
		reverseddata = range(amount, 0, -1)

		randoms = []
		amount2 = amount * 2
		for i in range(0, SEARCH_AMOUNT):
			"Each time we test value that we now is in structure and one that isn't."
			randoms.append(R.randint(0, amount))
			randoms.append(R.randint(amount, amount2))

		print "Test case for ordered data."
		print
		testInserting(skiplist, tree, data, general)
		print
		testSearching(skiplist, tree, data, general)
		print
		print "Test case for reversed data."
		print
		testInserting(skiplist, tree, reverseddata, general)
		print
		testSearching(skiplist, tree, reverseddata, general)
		print

		for loop in range(0, RANDOM_DATA_LOOPS):
			random.shuffle(data)
			print "Test case for random data (attempt " + str(loop + 1) + "/" + str(RANDOM_DATA_LOOPS) + ")"
			print
			testInserting(skiplist, tree, reverseddata, general)
			print
			testSearching(skiplist, tree, reverseddata, general)
			print

	print "---------------------"
	print

	listtime = general['list_insert']
	treetime = general['tree_insert']
	print "Inserting in general:"
	print "SkipList: " + str(listtime)
	print "RedBlackTree: " + str(treetime)
	if listtime < treetime:
		msg = "SkipList"
		result = treetime / listtime * 100
	else:
		msg = "RedBlackTree"
		result = listtime / treetime * 100
	result -= 100
	msg += " is better for about " + str(int(result)) + "%"
	print msg

	print

	listtime = general['list_search']
	treetime = general['tree_search']
	print "Searching in general:"
	print "SkipList: " + str(listtime)
	print "RedBlackTree: " + str(treetime)
	if listtime < treetime:
		msg = "SkipList"
		result = treetime / listtime * 100
	else:
		msg = "RedBlackTree"
		result = listtime / treetime * 100
	result -= 100
	msg += " is better for about " + str(int(result)) + "%"
	print msg

def testInserting(skiplist, tree, data, general):
	"""
	Case for inserting data.
	"""
	start = time.time()
	for i in data:
		skiplist.insert(i)
	listtime = time.time() - start
	general['list_insert'] += listtime

	start = time.time()
	for i in data:
		tree.insert(i)
	treetime = time.time() - start
	general['tree_insert'] += treetime

	print "Inserting:"
	print "SkipList: " + str(listtime)
	print "RedBlackTree: " + str(treetime)
	if listtime < treetime:
		msg = "SkipList"
		result = treetime / listtime * 100
	else:
		msg = "RedBlackTree"
		result = listtime / treetime * 100
	result -= 100
	msg += " is better for about " + str(int(result)) + "%"
	print msg

def testSearching(skiplist, tree, data, general):
	"""
	Case for searching data.
	"""
	start = time.time()
	for i in data:
		skiplist.search(i)
	listtime = time.time() - start
	general['list_search'] += listtime

	start = time.time()
	for i in data:
		tree.search(i)
	treetime = time.time() - start
	general['tree_search'] += treetime

	print "Searching:"
	print "SkipList: " + str(listtime)
	print "RedBlackTree: " + str(treetime)
	if listtime < treetime:
		msg = "SkipList"
		result = treetime / listtime * 100
	else:
		msg = "RedBlackTree"
		result = listtime / treetime * 100
	result -= 100
	msg += " is better for about " + str(int(result)) + "%"
	print msg

if __name__ == "__main__":
	test()
