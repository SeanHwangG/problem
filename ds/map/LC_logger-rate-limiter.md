# [LC_logger-rate-limiter](https://leetcode.com/problems/logger-rate-limiter)

```en
Design logger system that receive stream of messages along with its timestamps
Each message should be printed if and only if it is not printed in the last 10 seconds
```

```txt
Logger logger = new Logger();

// logging string "foo" at timestamp 1
logger.shouldPrintMessage(1, "foo"); returns true;

// logging string "bar" at timestamp 2
logger.shouldPrintMessage(2, "bar"); returns true;

// logging string "foo" at timestamp 3
logger.shouldPrintMessage(3, "foo"); returns false;

// logging string "bar" at timestamp 8
logger.shouldPrintMessage(8, "bar"); returns false;

// logging string "foo" at timestamp 10
logger.shouldPrintMessage(10, "foo"); returns false;

// logging string "foo" at timestamp 11
logger.shouldPrintMessage(11, "foo"); returns true;
```

## Solution

* cpp

  ```cpp
  class Logger {
  public:
    Logger() {}

    bool shouldPrintMessage(int timestamp, string message) {
      if (timestamp < m[message]) return false;
      m[message] = timestamp + 10;
      return true;
    }

  private:
    unordered_map <string ,int > m;
  };
  ```
