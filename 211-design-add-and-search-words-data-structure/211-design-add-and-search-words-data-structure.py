class WordDictionary:

    def __init__(self):
        self.map = dict()
        self.exact = False

    def addWord(self, word: str) -> None:
        if len(word) != 0:
            if word[0] not in self.map:
                self.map[word[0]] = WordDictionary()
            self.map[word[0]].addWord(word[1:])
        else:
            self.exact = True

    def search(self, word: str) -> bool:
        if len(word) == 0:
            return self.exact
        if word[0] == '.':
            return any(w.search(word[1:]) for w in self.map.values())
        return word[0] in self.map and self.map[word[0]].search(word[1:])


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)