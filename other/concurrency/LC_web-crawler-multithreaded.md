# [LC_web-crawler-multithreaded](https://leetcode.com/problems/web-crawler-multithreaded)

Given a url startUrl and an interface HtmlParser
implement a Multi-threaded web crawler to crawl all links that are under same hostname as startUrl
  Start from the page: startUrl
  Call HtmlParser.getUrls(url) to get all urls from a webpage of given url
  Do not crawl the same link twice
  Explore only the links that are under the same hostname as startUrl

```txt
Input:
urls = [
  "http://news.yahoo.com",
  "http://news.yahoo.com/news",
  "http://news.yahoo.com/news/topics/",
  "http://news.google.com",
  "http://news.yahoo.com/us"
]
edges = [[2,0],[2,1],[3,2],[3,1],[0,4]]
startUrl = "http://news.yahoo.com/news/topics/"

Output:
[
  "http://news.yahoo.com",
  "http://news.yahoo.com/news",
  "http://news.yahoo.com/news/topics/",
  "http://news.yahoo.com/us"
]
```

## Solution

* java

```java
import java.net.URI;
class Solution {
  public List<String> crawl(String startUrl, HtmlParser htmlParser) {
    String host = URI.create(startUrl).getHost();
    Crawler crawler = new Crawler(startUrl, host, htmlParser);
    crawler.resultArray = new ArrayList<>();
    crawler.start();
    Crawler.joinThread(crawler);
    return crawler.resultArray;
  }
}

class Crawler extends Thread {
  String startUrl, hostname;
  HtmlParser htmlParser;
  public static volatile List<String> resultArray = new ArrayList<>();
  public Crawler(String startUrl, String hostname, HtmlParser htmlParser){
    this.startUrl = startUrl;
    this.hostname = hostname;
    this.htmlParser = htmlParser;
  }
  @Override
  public void run(){
    String host=URI.create(startUrl).getHost();
    if(!host.equals(hostname) || resultArray.contains(startUrl)) return;

    resultArray.add(startUrl);
    List<Thread> threads = new ArrayList<>();
    for (String s: htmlParser.getUrls(startUrl)){
      Crawler crawler = new Crawler(s, hostname, htmlParser);
      crawler.start();
      threads.add(crawler);
    }
    for(Thread t: threads){
      try{
        thread.join();
      } catch(InterruptedException e){}
    }
  }
}
```

* py

```py
import threading
import queue
from urllib.parse import urlsplit

class Solution:
  def crawl(self, startUrl: str, htmlParser: "HtmlParser") -> List[str]:
    domain = urlsplit(startUrl).netloc
    requestQueue, resultQueue = queue.Queue([startUrl]), queue.Queue()
    t = threading.Thread(target=self._crawl, args=(domain, htmlParser, requestQueue, resultQueue), daemon=True)
    t.start()
    running = 1
    visited = set([startUrl])
    while running > 0:
      for url in resultQueue.get():
        if url in visited:
          continue
        visited.add(url)
        requestQueue.put(url)
        running += 1
      running -= 1
    return list(visited)

  def _crawl(self, domain, htmlParser, requestQueue, resultQueue):
    while True:
      url = requestQueue.get()
      newUrls = []
      for url in htmlParser.getUrls(url):
        u = urlsplit(url)
        if u.netloc == domain:
          newUrls.append(url)
      resultQueue.put(newUrls)
```

* CV:

  ```py
  class HtmlParser(object):
    def getUrls(self, url):
      """
      :type url: str
      :rtype List[str]
      """
      pass

  class Solution(object):
    NUMBER_OF_WORKERS = 8

    def __init__(self):
      self.__cv = threading.Condition()
      self.__q = Queue.Queue()

    def crawl(self, startUrl: str, htmlParser: HtmlParser) -> list[str]:
      SCHEME = "http://"
      def hostname(url):
        pos = url.find('/', len(SCHEME))
        if pos == -1:
          return url
        return url[:pos]

      def worker(htmlParser, lookup):
        while True:
          from_url = self.__q.get()
          if from_url is None:
            break
          name = hostname(from_url)
          for to_url in htmlParser.getUrls(from_url):
            if name != hostname(to_url):
              continue
            with self.__cv:
              if to_url not in lookup:
              lookup.add(to_url)
              self.__q.put(to_url)
          self.__q.task_done()

      workers = []
      self.__q = Queue.Queue()
      self.__q.put(startUrl)
      lookup = set([startUrl])
      for i in xrange(self.NUMBER_OF_WORKERS):
        t = threading.Thread(target=worker, args=(htmlParser, lookup))
        t.start()
        workers.append(t)
      self.__q.join()
      for t in workers:
        self.__q.put(None)
      for t in workers:
        t.join()
      return list(lookup)

  ```
