# [LC_implement-queue-using-stacks](https://leetcode.com/problems/implement-queue-using-stacks)

* en

  ```en
  Implement a first in first out (FIFO) queue using only two stacks
  Implemented queue should support all the functions of a normal queue (push, peek, pop, and empty)
  ```

* tc

  ```tc
  Input: ["MyQueue", "push", "push", "peek", "pop", "empty"]
  [[], [1], [2], [], [], []]

  Output: [null, null, null, 1, 1, false]
  ```

## Solution

* cpp

  ```cpp
  class Queue {
    stack<int> input, output;
    public:

    void push(int x) {
      input.push(x);
    }

    void pop(void) {
      peek();
      output.pop();
    }

    int peek(void) {
      if (output.empty())
        while (input.size())
          output.push(input.top()), input.pop();
      return output.top();
    }

    bool empty(void) {
      return input.empty() && output.empty();
    }
  };
  ```
