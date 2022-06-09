# [LC_search-in-a-binary-search-tree](https://leetcode.com/problems/search-in-a-binary-search-tree)

* en

  ```en
  Given an expression such as expression = "e + 8 - a + 5" and an evaluation map such as {"e": 1}
  Return the list of tokens representing simplified expression, such as ["-1*a","14"]
  ```

* tc

  ```tc
  Input: expression = "e - 8 + temperature - pressure", evalvars = ["e", "temperature"], evalints = [1, 12]
  Output: ["-1*pressure","5"]

  Input: expression = "(e + 8) * (e - 8)", evalvars = [], evalints = []
  Output: ["1*e*e","-64"]

  Input: expression = "a * b * c + b * a * c * 4", evalvars = [], evalints = []
  Output: ["5*a*b*c"]
  ```

## Solution

* py

  ```py
  def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
    class C(collections.Counter):
      def __add__(self, other):
        self.update(other)
        return self
      def __sub__(self, other):
        self.subtract(other)
        return self
      def __mul__(self, other):
        product = C()
        for x in self:
          for y in other:
            xy = tuple(sorted(x + y))
            product[xy] += self[x] * other[y]
        return product
    vals = dict(zip(evalvars, evalints))
    def f(s):
      s = str(vals.get(s, s))
      return C({(s,): 1}) if s.isalpha() else C({(): int(s)})
    c = eval(re.sub('(\w+)', r'f("\1")', expression))
    return ['*'.join((str(c[x]),) + x) for x in sorted(c, key=lambda x: (-len(x), x)) if c[x]]
  ```
