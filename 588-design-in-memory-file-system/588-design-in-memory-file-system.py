class File:
    # content is string if it is a regular file, or a map from name to File if it is a directory
    def __init__(self, name: str, isDirectory: bool, content):
        self.name = name
        self.isDirectory = isDirectory
        self.content = content

class FileSystem:

    def __init__(self):
        self.root = File('/', True, dict())

    def ls(self, path: str) -> List[str]:
        if path == '/':
            result = list(self.root.content)
            result.sort()
            return result
        
        pathComponents = path.split('/')[1:]
        
        currFile = self.root
        for pathComponent in pathComponents:
            currFile = currFile.content[pathComponent]
        
        if currFile.isDirectory:
            result = list(currFile.content)
            result.sort()
            return result
        return [currFile.name]

    def mkdir(self, path: str) -> None:
        pathComponents = path.split('/')[1:]
        
        currDir = self.root
        for pathComponent in pathComponents:
            if pathComponent in currDir.content:
                currDir = currDir.content[pathComponent]
            else:
                newDir = File(pathComponent, True, dict())
                currDir.content[pathComponent] = newDir
                currDir = newDir

    def addContentToFile(self, filePath: str, content: str) -> None:
        pathComponents = filePath.split('/')[1:]
        
        currDir = self.root
        for pathComponent in pathComponents[:-1]:
            if pathComponent in currDir.content:
                currDir = currDir.content[pathComponent]
            else:
                newDir = File(pathComponent, True, dict())
                currDir.content[pathComponent] = newDir
                currDir = newDir
        
        if pathComponents[-1] not in currDir.content:
            currDir.content[pathComponents[-1]] = File(pathComponents[-1], False, '')
        
        currDir.content[pathComponents[-1]].content += content

    def readContentFromFile(self, filePath: str) -> str:
        pathComponents = filePath.split('/')[1:]
        
        currFile = self.root
        for pathComponent in pathComponents:
            currFile = currFile.content[pathComponent]
        
        return currFile.content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)