# [LC_number-of-days-between-two-dates](https://leetcode.com/problems/number-of-days-between-two-dates)

Write a program to count the number of days between two dates.
The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.

```txt
Input: date1 = "2019-06-29", date2 = "2019-06-30"
Output: 1

Input: date1 = "2020-01-15", date2 = "2019-12-31"
Output: 15
```

## Solution

* cpp

```cpp
int daysBetweenDates(string date1, string date2) {
  std::tm t1{};
  t1.tm_year = std::stoi(date1.substr(0, 4)) - 1900;
  t1.tm_mon = std::stoi(date1.substr(5, 2)) - 1;
  t1.tm_mday = std::stoi(date1.substr(8, 2));

  std::tm t2{};
  t2.tm_year = std::stoi(date2.substr(0, 4)) - 1900;
  t2.tm_mon = std::stoi(date2.substr(5, 2)) - 1;
  t2.tm_mday = std::stoi(date2.substr(8, 2));

  double diff_seconds = std::difftime(std::mktime(&t1), std::mktime(&t2));
  return std::abs(static_cast<int>(diff_seconds / (60 * 60 * 24)));
}
```

* go

```go
func daysBetweenDates(date1 string, date2 string) int {
  const dateFormat = "2006-01-02"
  d1, _ := time.Parse(dateFormat, date1)
  d2, _ := time.Parse(dateFormat, date2)

  days := int(d2.Sub(d1).Hours()) / 24
  if days > 0 {
    return days
  }
  return days * -1
}
```

* java

```java
import static java.time.LocalDate.parse;
import static java.time.temporal.ChronoUnit.DAYS;

public int daysBetweenDates(String date1, String date2) {
  return (int) Math.abs(DAYS.between(parse(date1), parse(date2)));
}
```

* py

```py
def daysBetweenDates(self, date1, date2):
  d1 = date(*tuple(int(val) for val in date1.split("-")))
  d2 = date(*tuple(int(val) for val in date2.split("-")))
  return abs((d1 - d2).days)
```
