{% tabs %}{% tab title='CC_CHEFSORT.md' %}

* Given a sequence A1,A2,…,AN, wants to sort it in non-decreasing order
* Unfortunately, he can only modify it using specific operations. In each operation, Chef should do the following:
  * Choose an integer K such that 0<K<230
  * Choose an integer P such that 1≤P≤N
  * Perform one of the following actions:
    * type t=1: for each i (1≤i≤P), change Ai to Ai+K
    * type t=2: for each i (P≤i≤N), change Ai to Ai+K
    * type t=3: for each i (1≤i≤P), change Ai to Ai⊕K
    * type t=4: for each i (P≤i≤N), change Ai to Ai⊕K
* Note that you do not need to minimise the number of operations
* It is guaranteed that a solution using at most ⌊N/2⌋ operations always exists

```txt
Input:
5
3
1 10 9
4
4 3 5 1
6
12 13 15 3 7 5
3
1 2 3
3
1 2 3

Output:
1
4 2 11
2
4 4 4
2 2 2
2
3 3 12
4 3 2
1
1 3 3
0
```

{% endtab %}{% tab title='CC_CHEFSORT.py' %}

```py
for _ in range(int(input())):
  N = int(input())
  A = list(map(int, input().split()))
  ops = []
  up = sum(A[i + 1] > A[i] for i in range(N - 1))
  down = sum(A[i + 1] < A[i] for i in range(N - 1))
  P = pow(2, 30) - 1
  flag = False
  if down > up:
    flag = True
    ops.append((3, N, P)) # xor to inversion
  for i in range(N - 1):
    if (A[i + 1] < A[i] and not flag) or (A[i + 1] > A[i] and flag):
      ops.append((2, i + 2, abs(A[i] - A[i + 1])))
  print(len(ops))
  for op in ops: print(*op)
```

{% endtab %}{% endtabs %}
