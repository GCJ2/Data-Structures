import sys

sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
	def __init__(self, value):
		self.value = value
		self.head = None  # Added head of None for easier instantiation
		self.left = None
		self.right = None

	# Insert the given value into the tree
	def insert(self, value):
		if self.head is None:  # If the BST is empty
			self.head = BinarySearchTree(value)  # Set the head to the value via BST()
		if value < self.value:  # If the value passed in is less than the current node
			if not self.left:  # And there isn't a node to the left
				self.left = BinarySearchTree(value)  # Create the node on the left
			else:  # Otherwise...
				self.left.insert(value)  # Run the function again
		if value >= self.value:  # If the value passed in is greater than or = to current node
			if self.right is None:  # And there isn't a node to the right
				self.right = BinarySearchTree(value)  # Create the node on the right
			else:  # Otherwise
				self.right.insert(value)  # Run the function again

	# Return True if the tree contains the value
	# False if it does not
	def contains(self, target):
		if self.value is None:  # If the BST is empty
			return False  # Return false, as we can't get anything from it
		elif target is self.value:  # If the current node == the target
			return True  # Return true, as the node has been found
		elif target < self.value:  # If the target is less than the current node
			return self.left.contains(target) if self.left else False  # Run the function again if self.left if exists
		else:
			return self.right.contains(
				target) if self.right else False  # Run the function again on self.right if exists

	# Return the maximum value found in the tree
	def get_max(self):
		if not self.right:  # If there are no nodes to the left of the head, the head is the greatest
			return self.value  # So return the head
		max_value = self.right  # Create a var to store the max value found thus far from node to right
		while max_value.right:  # While there is still a node to the right of our max value node
			max_value = max_value.right  # Set max value to the node to the right, as it is greater
		return max_value.value  # Once max_value.right is None, return value of current node

	# Call the function `cb` on the value of each node
	# You may use a recursive or iterative approach
	# def for_each(self, cb):
	# 	self.fe_callback(self, cb)              # Has a method that simply takes in a callback
	#
	# def fe_callback(self, node, cb=print()):    # Call back should print node, but not sure how to get it to work
	# 	if node is None:                        # Checks if node passed in is None
	# 		return                              # If so, do nothing
	# 	cb(node.value)                          # Run cb on node passed in
	# 	self.fe_callback(node.left, cb)         # Run the callback on left node recursively
	# 	self.fe_callback(node.right, cb)        # Run the callback on right node recursively

	def for_each(self, cb):
		cb(self.value)
		if self.left:
			self.left.for_each(cb)
		if self.right:
			self.right.for_each(cb)

	# DAY 2 Project -----------------------

	# Print all the values in order from low to high
	# Hint:  Use a recursive, depth first traversal
	def in_order_print(self, node):
		if self.left:
			self.left.in_order_print(node)
		if self.value:
			print(self.value)
		if self.right:
			self.right.in_order_print(node)

	# Print the value of every node, starting with the given node,
	# in an iterative breadth first traversal
	def bft_print(self, node):
		queue = Queue()
		queue.enqueue(node)
		if node:
			while queue.len() > 0:
				current_node = queue.dequeue()
				print(current_node.value)
				if current_node.left:
					queue.enqueue(current_node.left)
				if current_node.right:
					queue.enqueue(current_node.right)

	# Print the value of every node, starting with the given node,
	# in an iterative depth first traversal
	def dft_print(self, node):
		if node:
			print(node.value)
			self.dft_print(node.left)
			self.dft_print(node.right)
		# stack = Stack()
		# if node:
		# 	current_node = node
		# 	while current_node:
		# 		if current_node:
		# 			stack.push(current_node)
		# 			print(current_node.value)
		# 			current_node = current_node.left
		# 		else:
		# 			current_node = stack.pop()
		# 			current_node = current_node.right
		# stack = Stack()
		# stack.push(node)
		# while stack.len() > 0:
		# 	current_node = stack.pop()
		# 	print(current_node.value)
		# 	if current_node.left:
		# 		stack.push(current_node.left)
		# 	if current_node.right:
		# 		stack.push(current_node.right)

# STRETCH Goals -------------------------
# Note: Research may be required

# # Print Pre-order recursive DFT
# def pre_order_dft(self, node):
# 	pass
#
#
# # Print Post-order recursive DFT
# def post_order_dft(self, node):
# 	pass
