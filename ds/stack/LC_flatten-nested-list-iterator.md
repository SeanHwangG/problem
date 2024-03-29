# [LC_flatten-nested-list-iterator](https://leetcode.com/problems/flatten-nested-list-iterator)

* en

  ```en
  Implement the NestedIterator class:
  NestedIterator(List\<NestedInteger\> nestedList) Initializes the iterator with the nested list nestedList.
  int next() Returns the next integer in the nested list.
  boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.
  ```

* tc

  ```tc
  Input: nestedList = [[1,1],2,[1,1]]
  Output: [1,1,2,1,1]
  ```

## Solution

* py

  ```py
  # class NestedInteger:
  #   def isInteger(self) -> bool:
  #     """ @return True if this NestedInteger holds a single integer, rather than a nested list. """
  #
  #   def getInteger(self) -> int:
  #     """ @return the single integer that this NestedInteger holds, if it holds a single integer
  #     return None if this NestedInteger holds a nested list #
  #
  #   def getList(self) -> [NestedInteger]:
  #     """ @return the nested list that this NestedInteger holds, if it holds a nested list
  #     return None if this NestedInteger holds a single integer """
  def __init__(self, nestedList):
    self.stack = [[nestedList, 0]]

  def next(self):
    self.hasNext()
    nestedList, i = self.stack[-1]
    self.stack[-1][1] += 1
    return nestedList[i].getInteger()

  def hasNext(self):
    s = self.stack
    while s:
      nestedList, i = s[-1]
      if i == len(nestedList):
        s.pop()
      else:
        x = nestedList[i]
        if x.isInteger():
          return True
        s[-1][1] += 1
        s.append([x.getList(), 0])
    return False
  ```
