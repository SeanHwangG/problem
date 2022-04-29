# [HR_sed-command-5](https://www.hackerrank.com/challenges/sed-command-5)

Reverse the ordering of segments in each credit card number

```txt
Input: 
1234 5678 9101 1234  
2999 5178 9101 2234  
9999 5628 9201 1232  
8888 3678 9101 1232

Output:
1234 9101 5678 1234  
2234 9101 5178 2999  
1232 9201 5628 9999  
1232 9101 3678 8888 
```

## Solution

```sh
sed -r 's/(.... )(.... )(.... )(....)/\4 \3\2\1/'
```
