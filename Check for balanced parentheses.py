#Q.Given an expression string, write a python program to find whether a given string has balanced parentheses or not.



#### Stack Linkedlist implimentation(LIFO)

####################################
class Node:

  def __init__(self,value):
    self.data = value
    self.next = None
    
###################################
    
class Stack:

  def __init__(self):
    self.top = None

    

  def push(self, value):

    new_node = Node(value)

    new_node.next = self.top

    self.top = new_node
    

  def pop(self):

    if self.top is None:
      return "Stack Empty"
    else:
      data = self.top.data
      self.top = self.top.next
      return data

  def traverse(self):

    temp = self.top

    while temp is not None:
      print(temp.data,end=' ')
      temp = temp.next



  def size(self):

    temp = self.top
    counter = 0

    while temp is not None:
      counter+=1
      temp = temp.next

    return counter


  def peek(self):

    if self.top is None:
      return "Stack Empty"
    else:
      return self.top.data



############################################################################


def brackets(expression):

  s = Stack()

  for i in expression:

    if i == '(' or i == '{' or i == '[':
      s.push(i)
    elif i == ')':
      if not handle_closing_bracket('(',s):
        return False
    elif i == '}':
      if not handle_closing_bracket('{',s):
        return False
    elif i == ']':
      if not handle_closing_bracket('[',s):
        return False
        

  if s.size() == 0:
    return True
  else:
    print("3")
    return False

def handle_closing_bracket(bracket_type, s):

  if s.size() == 0:
    return False
  else:
    if s.peek() == bracket_type:
      s.pop()
      return True
    else:
      return False







###########################################################################
#Examples:
#Input : {[]{()}}
#Output : Balanced

#Input : [{}{}(]
#Output : Unbalanced
