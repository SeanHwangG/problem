# Requirements

* Facebook:
  * Functional Requirements
    * Newsfeed will be generated based on the posts from the people, pages, and groups that a user follows
    * User may have many friends and follow a large number of pages/groups
    * Feeds may contain images, videos, or just text
    * Our service should support appending new posts as they arrive to the newsfeed for all active users

  * Non-functional Requirements
    * Generate any user’s newsfeed in real-time - maximum latency seen by end user would be 2s
    * Post shouldn’t take more than 5s to make it to a user’s feed assuming a new newsfeed request comes in

  * Architecture:
    * ![Architecture](images/20210815_221420.png)
  * Use case Diagram
    * ![Use case Diagram](images/20210815_205536.png)

  * OOP
    * ![OOP](images/20210815_205619.png)

  * Feed Publishing
    * Fan-out-on-load (Pull): Keeping recent feed data in memory so user can pull from server whenever they need it
      * [-] New data might not be shown to the users until they issue a pull request, hard to find the right pull cadence
    * Fan-out-on-write (Push): Once a user has published a post, we can immediately push this post to all the followers
      * [+] Reduces read operations
      * [-] Maintain a Long Poll request with server for receiving updates

  * How many feed items should we store in memory for a user’s feed?
    * Initially, can decide to store 500 feed items/user, but this number can be adjusted later based on the usage pattern

  * Should we generate (and keep in memory) newsfeeds for all users?
    * Many idle users -> LRU cache that can remove users from memory that haven’t accessed their newsfeed for long time
    * Figure out login pattern of users to pre-generate their newsfeed (ex: at what time of day user is active, etc)

  * How many feed items can we return to the client in each request?
    * Maximum limit for the number of items a user can fetch in one request (say 20)
    * But, let client specify how many feed items they want with each request, mobile vs. desktop

  * Should we always notify users if there are new posts available for their newsfeed?
    * Yes. However, on mobile devices, data usage is expensive, it can consume unnecessary bandwidth
    * Let users “Pull to Refresh” to get new posts
