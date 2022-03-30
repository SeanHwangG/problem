```py
import re
from collections import defaultdict
class Solution(object):
  def countOfAtoms(self, formula: str) -> str:
    tokens = re.findall('([A-Z]{1}[a-z]?|\(|\)|\d+)', formula)
    stack, i = [defaultdict(int)], -1
    while i + 1 < len(tokens):
      i, token = i + 1, tokens[i + 1]
      if token == '(':
        stack.append(defaultdict(int))
      else:
        count = 1
        if i + 1 < len(tokens) and tokens[i + 1].isdigit():
          count, i = int(tokens[i + 1]), i + 1
        atoms = stack.pop() if token == ')' else { token: 1 }
        for atom in atoms: # Combine counts of atoms.
          stack[-1][atom] += atoms[atom] * count
    return ''.join([atom + (str(count) if count > 1 else '') for atom, count in sorted(stack[-1].items())])
```