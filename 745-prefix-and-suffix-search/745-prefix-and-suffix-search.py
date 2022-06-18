class WordFilter(object):
    # todo
    def __init__(self, words):
        Trie = lambda: collections.defaultdict(Trie)
        
        self.trie = Trie()
        
        for weight, word in enumerate(words):
            word += '#'
            for i in range(len(word)):
                cur = self.trie
                cur[False] = weight
                for j in range(i, 2 * len(word) - 1):
                    cur = cur[word[j % len(word)]]
                    cur[False] = weight

    def f(self, prefix, suffix):
        cur = self.trie
        for letter in suffix + '#' + prefix:
            if letter not in cur:
                return -1
            cur = cur[letter]
        return cur[False]