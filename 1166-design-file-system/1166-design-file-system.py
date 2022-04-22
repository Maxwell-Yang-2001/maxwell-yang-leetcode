class FileSystem:

    def __init__(self):
        self.path_map = dict()

    def createPath(self, path: str, value: int) -> bool:
        if path in self.path_map:
            return False
        
        last_slash = path.rindex('/')
        if last_slash != 0 and path[:last_slash] not in self.path_map:
            return False
        self.path_map[path] = value
        return True

    def get(self, path: str) -> int:
        return self.path_map[path] if path in self.path_map else -1


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)