from doubly_linked_list import DoublyLinkedList, ListNode


class LRUCache:
	"""
	Our LRUCache class keeps track of the max number of nodes it
	can hold, the current number of nodes it is holding, a doubly-
	linked list that holds the key-value entries in the correct
	order, as well as a storage dict that provides fast access
	to every node stored in the cache.
	"""

	def __init__(self, limit=10):
		self.limit = limit                  # Limit to how big cache can be
		self.size = 0                       # Initial size of cache
		self.cache = {}                     # Creates dict for cache
		self.dll = DoublyLinkedList()       # Allow use of DLL methods

	def get(self, key):                     # Takes in key as arg to look for node
		if key in self.cache:               # If the key is currently in the cache
			node = self.cache[key]          # Instant a node for the node in the cache
			# print(node)                   # Prints node in memory; Readable if Dan Levy
			# print(node.value)              # Print value of node ('item1', 'a')
			# print(node.value[0])
			# print(node.value[1])
			self.dll.move_to_front(node)    # Move node to front via dll method
			return node.value[1]            # Return the [1] value of the node (See line 23)

	def set(self, key, value):              # Takes in key and value to add/set node
		if key in self.cache:               # If key is currently in the cache
			node = self.cache[key]          # Instant a node in for the node in the cache
			node.value = (key, value)       # Set the value of that node to they passed in key and value
			# print(node.value)               # Print value of node ('item2', 'z')
			self.dll.move_to_front(node)    # Move the node to the front via dll method
			return                          # Return everything done in if block
		if self.size == self.limit:         # If the size of the cache == the cache size limit
			# print(self.cache[self.dll.tail.value[0]])   # Prints the node to be deleted (See line 22
			del self.cache[self.dll.tail.value[0]]  # Delete the node from the cache
			self.dll.remove_from_tail()             # Remove said node from the tail via dll method
			self.size -= 1                          # Update size of cache (Must be done manually)
		# print((key, value))                         # Print (key, value) to be added to head ('item1', 'a')
		self.dll.add_to_head((key, value))          # Add via dll the (key, value) to the head
		print(self.cache)                           # Prints out cache to monitor during testing
		self.cache[key] = self.dll.head             # Set current cache key to node at head
		print(self.dll.head.value)                  # Prints out new value of head from DLL
		self.size += 1                              # Update size of cache (Must be done manually)

"""
Retrieves the value associated with the given key. Also
needs to move the key-value pair to the end of the order
such that the pair is considered most-recently used.
Returns the value associated with the key or None if the
key-value pair doesn't exist in the cache.
"""

'''
Get key
Move current node to head
Return the value of the node
'''

"""
Adds the given key-value pair to the cache. The newly-
added pair should be considered the most-recently used
entry in the cache. If the cache is already at max capacity
before this entry is added, then the oldest entry in the
cache needs to be removed to make room. Additionally, in the
case that the key already exists in the cache, we simply
want to overwrite the old value associated with the key with
the newly-specified value.
"""

'''

'''
