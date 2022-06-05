# [HR_text-processing-sort-7](https://www.hackerrank.com/challenges/text-processing-sort-7)

```en
Sort data in descending order of the average monthly temperature in January
```

```txt
Input: 
Bismarck, N.D.|10.2|43.3|70.4|45.2|16.84|96|44.3|64
Austin, Texas|50.2|68.3|84.2|70.6|33.65|85|0.9|62 / 58
Baltimore, Md.|32.3|53.2|76.5|55.4|41.94|115|21.5|53

Output:
Austin, Texas|50.2|68.3|84.2|70.6|33.65|85|0.9|62 / 58
Baltimore, Md.|32.3|53.2|76.5|55.4|41.94|115|21.5|53
Bismarck, N.D.|10.2|43.3|70.4|45.2|16.84|96|44.3|64
```

## Solution

* sh

  ```sh
  sort -nr -k2 -t'|'
  ```
