# [LC_design-twitter](https://leetcode.com/problems/design-twitter)

Input:
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]

Output: [null, null, [5], null, null, [6, 5], null, [5]]

```txt
Design twitter with following methods
  postTweet(userId, tweetId)
  getNewsFeed(userId)
  follow(follwerId, followeeId)
  unfollow(follwerId, follweeId)
```

## Solution

* go

```go
type Twitter struct {
  posts [][2]int
  friends map[int]map[int]bool
}

func Constructor() Twitter {
  return Twitter{
    posts : [][2]int{},
    friends : make(map[int]map[int]bool),
  }
}

func (this *Twitter) PostTweet(userId int, tweetId int)  {
  this.posts = append(this.posts, [2]int{tweetId, userId})
}

func (this *Twitter) GetNewsFeed(userId int) []int {
  res := []int{}
  for i := len(this.posts) - 1; i >= 0; i -- {
    if this.posts[i][1] == userId || this.friends[userId][this.posts[i][1]] {
      res = append(res, this.posts[i][0])
      if len(res) == 10 {
        return res
      }
    }
  }
  return res
}

func (this *Twitter) Follow(followerId int, followeeId int)  {
  if _, ok := this.friends[followerId]; !ok {
    this.friends[followerId] = make(map[int]bool)
  }
  this.friends[followerId][followeeId] = true
}

func (this *Twitter) Unfollow(followerId int, followeeId int)  {
  if _, ok := this.friends[followerId]; ok {
    this.friends[followerId][followeeId] = false
  }
}
```

* py

```py
class Twitter(object):
  def __init__(self):
    self.timer = itertools.count(step=-1)
    self.tweets = collections.defaultdict(collections.deque)
    self.followees = collections.defaultdict(set)

  def postTweet(self, userId, tweetId):
    self.tweets[userId].appendleft((next(self.timer), tweetId))

  def getNewsFeed(self, userId):
    tweets = heapq.merge(*(self.tweets[u] for u in self.followees[userId] | {userId}))
    return [t for _, t in heapq.nsmallest(10, tweets)]

  def follow(self, followerId, followeeId):
    self.followees[followerId].add(followeeId)

  def unfollow(self, followerId, followeeId):
    self.followees[followerId].discard(followeeId)
```
