class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.words = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.words

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        curr.word = True

    def search(self, word: str) -> bool:
        root = self.words

        def backtrack(i, curr):
            if i == len(word):
                return curr.word
            
            c = word[i]
            if c != '.' and c in curr.children:
                return backtrack(i + 1, curr.children[c])
            elif c == '.':
                for key in curr.children:
                    if backtrack(i + 1, curr.children[key]):
                        return True
            return False
        
        return backtrack(0, root)