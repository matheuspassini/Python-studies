"""
This module implements a Stack data structure using a linked list approach.
The Stack class provides basic stack operations:
- push: adds an element to the top of the stack
- pop: removes and returns the element from the top of the stack
- peek: returns the top element without removing it
- size management: tracks stack size and supports a maximum size limit (default 1000)
The implementation uses a linked list with a top pointer for efficient LIFO (Last In, First Out) operations.
"""

from linked_lists import Node

class Stack:
  def __init__(self, limit=1000):
    self.top_item = None
    self.size = 0
    self.limit = limit
  
  def push(self, value):
    if self.has_space():
      item = Node(value)
      item.set_next_node(self.top_item)
      self.top_item = item
      self.size += 1
      print("Adding {} to the pizza stack!".format(value))
    else:
      print("No room for {}!".format(value))

  def pop(self):
    if not self.is_empty():
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      print("Delivering " + item_to_remove.get_value())
      return item_to_remove.get_value()
    print("All out of pizza.")

  def peek(self):
    if not self.is_empty():
      return self.top_item.get_value()
    print("Nothing to see here!")

  def has_space(self):
    return self.limit > self.size

  def is_empty(self):
    return self.size == 0