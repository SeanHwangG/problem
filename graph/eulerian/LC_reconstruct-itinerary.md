# [LC_reconstruct-itinerary](https://leetcode.com/problems/reconstruct-itinerary)

* en

  ```en
  Given a list of airline tickets where tickets[i] = [fromi, toi] represent departure and arrival airports of one flight
  Reconstruct itinerary in order and return it
  ```

* tc

  ```tc
  Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
  Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
  ```

## Solution

* py

  ```py
  def findItinerary(self, tickets: List[List[str]]) -> List[str]:
    targets = collections.defaultdict(list)
    for a, b in sorted(tickets)[::-1]:
      targets[a] += b,
    route, stk = [], ['JFK']
    while stk:
      while targets[stk[-1]]:
        stk += [targets[stk[-1]].pop()]
      route += [stk.pop()]
    return route[::-1]
  ```
