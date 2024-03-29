# [LC_design-in-memory-file-system](https://leetcode.com/problems/design-in-memory-file-system)

* en

  ```en
  FileSystem() Initializes the object of the system.
  List\<String\> ls(String path)
    If path is a file path, returns a list that only contains this file's name.
    If path is a directory path, returns the list of file and directory names in this directory.
    The answer should in lexicographic order.
  void mkdir(String path) Makes a new directory according to the given path. The given directory path does not exist
    If the middle directories in the path do not exist, you should create them as well.
  void addContentToFile(String filePath, String content)
    If filePath does not exist, creates that file containing given content.
    If filePath already exists, appends the given content to original content.
    String readContentFromFile(String filePath) Returns the content in the file at filePath.
  ```

* tc

  ```tc
  Input:
  ["FileSystem", "ls", "mkdir", "addContentToFile", "ls", "readContentFromFile"]
  [[], ["/"], ["/a/b/c"], ["/a/b/c/d", "hello"], ["/"], ["/a/b/c/d"]]

  Output:
  [null, [], null, null, ["a"], "hello"]
  ```

## Solution

* py

  ```py
  Trie = lambda: collections.defaultdict(Trie)

  class FileSystem(object):
    def __init__(self):
      self.fs = Trie()
      self.fileinfo = collections.defaultdict(str)

    def ls(self, path):
      if path in self.fileinfo:
        return path.split('/')[-1:]

      cur = self.fs
      for token in path.split('/'):
        if token in cur:
          cur = cur[token]
        elif token:
          return []

      return sorted(cur.keys())

    def mkdir(self, path):
      cur = self.fs
      for token in path.split('/'):
        if token: cur = cur[token]

    def addContentToFile(self, filePath, content):
      self.mkdir(filePath)
      self.fileinfo[filePath] += content

    def readContentFromFile(self, filePath):
      return self.fileinfo[filePath]
  ```
