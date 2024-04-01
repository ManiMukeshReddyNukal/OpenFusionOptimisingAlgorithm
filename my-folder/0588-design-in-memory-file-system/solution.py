class FileSystem:
    class Dir:
        def __init__(self):
            self.dirs = {}
            self.files = {}

    def __init__(self):
        self.root = self.Dir()

    def ls(self, path):
        t = self.root
        files = []
        if path != "/":
            d = path.split("/")
            for i in range(1, len(d) - 1):
                t = t.dirs[d[i]]
            if d[-1] in t.files:
                files.append(d[-1])
                return files
            else:
                t = t.dirs.get(d[-1], t)  # Default to t if d[-1] is not found.
        files.extend(list(t.dirs.keys()))
        files.extend(list(t.files.keys()))
        files.sort()
        return files

    def mkdir(self, path):
        t = self.root
        d = path.split("/")
        for i in range(1, len(d)):
            if d[i] not in t.dirs:
                t.dirs[d[i]] = self.Dir()
            t = t.dirs[d[i]]

    def addContentToFile(self, filePath, content):
        t = self.root
        d = filePath.split("/")
        for i in range(1, len(d) - 1):
            t = t.dirs[d[i]]
        t.files[d[-1]] = t.files.get(d[-1], "") + content

    def readContentFromFile(self, filePath):
        t = self.root
        d = filePath.split("/")
        for i in range(1, len(d) - 1):
            t = t.dirs[d[i]]
        return t.files[d[-1]]

        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
