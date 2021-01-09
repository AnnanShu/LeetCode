class Node:
    def __init__(self, val = None, next_ = [], isEnd = False):
        self.val = val 
        self.next_ = {i for i in next_}
        self.isEnd = isEnd


class Trie:
    def __init__(self):
        self.node = Node()

    def insert(self, word: str) -> None:
        """
        Insert a word to a trie
        """
        temp = self.node 
        for i in word:
            if i not in temp.next_:
                temp.next_[i] = Node(i)
            temp = temp.next_[i]
        temp.isEnd = True
    
    def search(self, word: str):
        temp = self.node 
        for i in word[:-1]:
            if i not in temp.next_: return False 
            temp = temp.next_[i]
        
        if word[-1] not in temp.next_: return False
        if temp.next_[word[-1]].isEnd: return True
        return False

    def startWith(self, prefix: str) -> bool:
        """
        Return True if there is any word start with the given prefix
        """
        temp = self.node
        for i in prefix:
            if i not in prefix.next_: return False
            temp = temp.next_[i]
        return True
