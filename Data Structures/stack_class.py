"""
  Python Stack Class
"""

class Stack:
  def __init__(self):
    self.items = []


  def is_empty(self):
    # return len(self.items) == 0
    return not self.items

  def push(self, item):
    self.items.append(item)

  def pop(self):
    return self.items.pop()

  def peek(self):
    return self.items[-1]   # In Python can access end of a list by using negative indeces | In this case self.items[-1] is last item in the list

  def size(self):
    return len(self.items)

  def __str__(self):
    return str(self.items)


if __name__ == "__main__":   # If importing Stack class to another project, don't want the code below to run. So if the file is the main file, run code below

  s = Stack ()
  print(s)
