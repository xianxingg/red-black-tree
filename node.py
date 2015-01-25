class Node:
  color = 'Red'
  value = None
  left = None
  right = None
  parent = None
  side = None

  def __init__(self, value):
    self.value = value

  def initChildren(self):
    self.left = Node(None)
    self.right = Node(None)
  
  @staticmethod
  def initTree(value):
    node = Node(None)
    node.value = value
    node.initChildren()
    case1(node)
    return node

  def __str__(self):
    if self.value == None:
      return 'nilNode'
    return str(self.value) + self.color[0]

  def tree(self,level = 0):
    print '\t'*level, self
    if self.left.value != None:
      self.left.tree(level+1)
    if self.right.value != None:
      self.right.tree(level+1)

  # Accessing family members means that only the parent needs to be updated
  def grandparent(self):
    return self.parent.parent

  def uncle(self):
    if(self.parent.side == 'Left'):
      return self.grandparent().right
    else:
      return self.grandparent().left

  def brother(self):
    if(self.side == 'Left'):
      return self.parent.right
    else:
      return self.parent.left

  def family(self):
    print 'left\t\t' + str(self.left)
    print 'right\t\t' + str(self.right)
    print 'grandparent\t' + str(self.grandparent())
    print 'parent\t\t' + str(self.parent)
    print 'uncle\t\t' + str(self.uncle())
    print 'brother\t\t' + str(self.brother())

  def insert(self,value):
    if self.left.value == None:
      self.left.initChildren()
      self.left.parent = self
      self.left.value = value
      self.left.side = 'Left'
      case1(self.left)
    elif self.right.value == None:
      self.right.initChildren()
      self.right.parent = self
      self.right.value = value
      self.right.side = 'Right'
      case1(self.right)
    elif abs(self.left.value-value) < abs(self.right.value-value):
      self.left.insert(value)
    else:
      self.right.insert(value)
    self.blr()
    #self.balance()

  # Balances the left and right side of a node (smaller value on right)
  def blr(self):
    if self.left.value == None:
      self.left = self.right
    if self.left.value == None or self.right.value == None:
      return
    if self.left.value > self.right.value:
      self.left, self.right = self.right, self.left
    self.left.side = 'Left'
    self.right.side = 'Right'

  def weight(self):
    count = 0
    if self.color == 'Black':
      count += 1
    else:
      count += 0
    if self.left.value == None and self.right.value == None:
      return count
    if self.right.value == None:
      count += self.left.weight()
    else:
      count += self.left.weight() + self.right.weight()
    return count
 
  # Returns -1 if balanced; 0/1 if that node is heavier (more black subnodes) 
  def unbalanced(self):
    if self.left.value == None and self.right.value == None:
      return -1
    weight0 = self.left.weight()
    if self.right.value == None:
      if weight0 != 0:
        return 0
      else:
        return -1
    weight1 = self.right.weight()
    if weight0 > weight1:
      return 0
    elif weight0 < weight1:
      return 1
    else:
      return -1
    
  def rotateLeft(self):
    print None

def case1(node):
  print node
  print 'case1'
  if node.parent == None:
    node.color = 'Black'
  else: 
    case2(node)

def case2(node):
  print 'case2'
  if node.parent.color == 'Black':
    return
  else:
    case3(node)

def case3(node):
  print 'case3'
  if node.parent.color == 'Red' and node.uncle().color == 'Red':
    node.parent.color = 'Black'
    node.uncle().color = 'Black'
    node.grandparent().color = 'Red'
    case1(node.grandparent())
  else:
    case4(node)

def case4(node):
  print 'case4'
  if node.side != node.parent.side:
    print 'true'
    

def case5(node):
  print 'case5'
  print None


