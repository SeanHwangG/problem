# [LC_smallest-sufficient-team](https://leetcode.com/problems/smallest-sufficient-team)

* en

  ```en
  In a project, you have a list of required skills req_skills, and a list of people
  The ith person people[i] contains a list of skills that the person has
  Sufficient team: set of people ST for every required skill in req_skills, there should be person with that skill
    Can represent these teams by the index of each person
  Return any sufficient team of the smallest possible size, represented by the index of each person in any order
  ```

* tc

  ```tc
  Input: req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]]
  Output: [0,2]

  Input:
  req_skills = ["algorithms","math","java","reactjs","csharp","aws"],
  people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],
    ["csharp","math"],["aws","java"]]
  Output: [1,2]
  ```

## Solution

* py

  ```py
  def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
    n, m = len(req_skills), len(people)
    key = {v: i for i, v in enumerate(req_skills)}
    dp = {0: []}
    for i, p in enumerate(people):
      his_skill = 0
      for skill in p:
        if skill in key:
          his_skill |= 1 << key[skill]
      for skill_set, need in list(dp.items()):
        with_him = skill_set | his_skill
        if with_him == skill_set: continue
        if with_him not in dp or len(dp[with_him]) > len(need) + 1:
          dp[with_him] = need + [i]
    return dp[(1 << n) - 1]
  ```
