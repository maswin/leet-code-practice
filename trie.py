# https://leetcode.com/problems/implement-trie-prefix-tree/


class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}

    def add_children(self, val):
        if val not in self.children:
            self.children[val] = Node(val)
        return self.children[val]


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node("/")

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        def insert_util(word, i, root):
            if i == len(word):
                root.add_children("$")
                return
            insert_util(word, i + 1, root.add_children(word[i]))
        insert_util(word, 0, self.root)

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        def search_util(word, i, root):
            if i == len(word):
                return "$" in root.children
            return word[i] in root.children and search_util(word, i + 1, root.children[word[i]])
        return search_util(word, 0, self.root)

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        def search_util(word, i, root):
            if i == len(word):
                return True
            return word[i] in root.children and search_util(word, i + 1, root.children[word[i]])
        return search_util(prefix, 0, self.root)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

class Trie_Iterative:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node("/")

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        root = self.root
        for i in range(0, len(word)):
            root = root.add_children(word[i])
        root.add_children("$")

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        root = self.root
        ans = True
        for i in range(0, len(word)):
            ans = word[i] in root.children
            if not ans:
                break
            root = root.children[word[i]]
        return ans and "$" in root.children

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        root = self.root
        ans = True
        for i in range(0, len(prefix)):
            ans = prefix[i] in root.children
            if not ans:
                break
            root = root.children[prefix[i]]
        return ans
