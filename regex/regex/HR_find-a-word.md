# [HR_find-a-word](https://www.hackerrank.com/challenges/find-a-word)

* en

  ```en
  For every word, print the number of occurrences of the word in all the N sentences listed
  ```

* tc

  ```tc
  Input: 1
  foo bar (foo) bar foo-bar foo_bar foobar bar-foo bar, foo.
  2
  foo
  foobar

  Output:
  5  # foobar doesn't count
  1
  ```

## Solution

* cpp

  ```cpp
  #include <bits/stdc++.h>
  using namespace std;


  int main() {
    int nSentence;
    std::cin >> nSentence;

    std::vector<std::string> sentences(nSentence, "");
    for (int i = 0; i < nSentence; ++i)
      std::getline(std::cin, sentences[i]);

    uint nWords;
    std::cin >> nWords;

    std::vector<std::string> words(nWords, "");
    for (int i = 0; i < nWords; ++i)
      std::getline(std::cin, words[j]);

    for (int i = 0; i < nWords; ++i) {
      uint countOfWords = 0;
      std::regex re {R"(([^a-zA-Z0-9_]|\b))" + words[j] + R"((?![a-zA-Z0-9_]))"};
      for (uint i = 0; i < nSentence; ++i)
        countOfWords += std::distance(std::sregex_iterator(sentences[i].begin(), sentences[i].end(), re), std::sregex_iterator{});

      std::cout << countOfWords << std::endl;
    }
    return 0;
  }
  ```

* py

  ```py
  import re

  sentence = ' '.join(input() for _ in range(int(input())))
  for _ in range(int(input())):
    print(len(re.findall(fr'\b{input()}\b', sentence)))
  ```
