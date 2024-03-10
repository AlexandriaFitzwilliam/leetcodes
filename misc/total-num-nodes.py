from collections import deque

# Definition for a binary tree node.


class BinaryNode:

  def __init__(self, data=0, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

  def search_right(self):
    
    #init a list to keep track of path
    right_values = []
    #create a marker to keep track where we are
    marker = self
    
    #while there is always a .right keep going
    while marker:
      right_values.append(marker.data)
      if not marker.right:
        return right_values
      marker = marker.right
    #append data of current node to list
    #move the marker to .right
    
    # def node_count(self):
    #     count = 0
    #     count_list = []
    #     marker = self
    #     #marker = node1

    #     #while there is a new node we have not looked at
    #     while marker:
    #         count +=1
    #         if marker.left:
    #             count_list.append(marker.left)
    #         if marker.right:
    #             count_list.append(marker.right)
    #         # count_list = [marker.left(aka node2), marker.right(aka node3)]
    #         #as long as the count_list has more nodes to look at, move to next node
    #     return count


 # recursion count ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  def node_count(self):
    print(self.data)
    if not self:
      return 0
    if not self.left or not self.right or not self.right.node_count or not self.left.node_count:
        return
    # need to stop if there are no children
    count = 0
      #self.left.node_count()
    count += 1 + self.left.node_count() + self.right.node_count()
    return count

# Count nodes in left subtree:
# Count nodes in right subtree:
# Total number of nodes in tree is current node plus sizes of left and right subtrees



# create count
# use stack while loop
# check left if present count +1 
# check right if present count +1
# if not present return count

#

#given the root of a binary tree, imagin yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom

#will never be given no input
#return the values from top to bottom

node4 = BinaryNode(4)
node5 = BinaryNode(5)
node3 = BinaryNode(3, node4)
node2 = BinaryNode(2, node5)
node1 = BinaryNode(1, node2, node3)

# ===> [1, 3, 4]

print(node1.search_right())
print(node1.node_count())
# 
