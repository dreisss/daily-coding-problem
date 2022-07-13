
from types import NoneType


def serialize(root: object):
  result = "{ "

  dict = root.__dict__
  for key in dict.keys():

    if (type(dict[key]) == str or type(dict[key]) == NoneType):
      result += f"{key}: {dict[key]}, "

    else:
      result += f"{key}: {serialize(dict[key])}, "

  result += "}"

  # print(result)
  return result


class Node:
  def __init__(self, val, left = None, right = None) -> None:
    self.val = val
    self.left = left
    self.right = right

print(serialize(Node('root', Node('left', Node('left.left')))))
