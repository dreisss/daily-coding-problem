[<<]: ../02/
[>>]: ../04/

# **[<<] #03 [>>]**

Given the root to a binary tree, implement serialize(root), which serializes the tree int
a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

```py
class Node:
  def **init**(self, val, left=None, right=None):
  self.val = val
  self.left = left
  self.right = right
```

The following test should pass:

```py
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
```

#

- **Difficult:** Medium
- **Made in:** Python
