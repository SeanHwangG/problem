# [LC_reformat-date](https://leetcode.com/problems/reformat-date)

* en

  ```en
  Given date string in the form Day Month Year
  Convert date string to the format YYYY-MM-DD
  ```

* tc

  ```tc
  Input: date = "20th Oct 2052"
  Output: "2052-10-20"
  ```

## Solution

* cpp

  ```cpp
  class Solution {
    unordered_map<string, string> months = {
        {"Jan", "01"}, {"Feb", "02"}, {"Mar", "03"}, {"Apr", "04"},
        {"May", "05"}, {"Jun", "06"}, {"Jul", "07"}, {"Aug", "08"},
        {"Sep", "09"}, {"Oct", "10"}, {"Nov", "11"}, {"Dec", "12"}};

  public:
    string reformatDate(string date) {
      stringstream ss(date);
      string d, m, y;
      ss >> d;
      ss >> m;
      ss >> y;

      // reformat month
      m = months[m];

      // reformat day
      d = to_string(stoi(d));
      if (d.size() == 1) d = "0" + d;

      return y + "-" + m + "-" + d;
    }
  };
  ```

* go

  ```go
  func reformatDate(date string) string {
    month := map[string]string{
      "Jan": "01",
      "Feb": "02",
      "Mar": "03",
      "Apr": "04",
      "May": "05",
      "Jun": "06",
      "Jul": "07",
      "Aug": "08",
      "Sep": "09",
      "Oct": "10",
      "Nov": "11",
      "Dec": "12",
    }
    if len(date) == 12 { date = "0" + date }
    return date[9:] + "-" + month[date[5:8]] + "-" + date[:2]
  }
  ```

* js

  ```js
  reformatDate(date) => {
    new Date(Date.parse(date.replace(/.. /, ''))).toISOString().slice(0, 10);
  }
  ```

* py

  ```py
  def reformatDate(self, date: str) -> str:
    return datetime.datetime.strptime(re.sub(r"(st|th|rd|nd)", "", date), "%d %b %Y").strftime("%Y-%m-%d")
  ```
