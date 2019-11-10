from Queue import deque
import copy

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        n = len(beginWord)
        cur_layer = [beginWord]
        words = {}
        for word in wordList:
            words[word] = True
        depth = 1
        while cur_layer:
            next_layer = []
            for word in cur_layer:
                if word == endWord:
                    return depth
                for i in range(n):
                    for index in "abcdefghijklmnopqrstuvwxyz":
                        new_word = word[:i] + index + word[i + 1:]
                        if new_word in words:
                            next_layer.append(new_word)
                            del words[new_word]
            depth += 1
            cur_layer = next_layer

        return 0


class Solution02(object):
    """
    Solution02比较有意思，要求求出s->v的所有最短路径并输出，这是一个常规问题。
    在解决输出所有路径的问题上，花了不少的时间。
    1。解决的基本思路是，parent[u]不再是单个值， 而是一个数组。这样在求最短路径的时候，需要遍历所有的路径。用回溯方法
    遍历所有的路径。。。。是个好题
    2。在判断条件的时候，寻找多个parent。主要是通过判断下一层的所有节点的时候，当处理完下一层某个结点后，并不马上放入visited
    队列。而是通过判断下一次访问时，存在visited，需要append.加了一个level dict.用于判断每个结点的level值。
    """
    def findLadders(self, beginWord, endWord, wordList):
        """
        ac:
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        n = len(beginWord)
        parent = {beginWord: []}
        frontier = [beginWord]
        words = set(wordList)
        all_paths = []
        levels = {beginWord: 0}
        cur_level = 1
        stack = []
        while frontier:
            next_layer = []
            for w in frontier:
                if w == endWord:
                    self.find_path(parent, endWord, beginWord, all_paths, stack)
                    return all_paths
                for i in range(n):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        new_w = w[0:i] + j + w[i+1:]
                        if new_w in words:  # 寻找adj
                            if levels.get(new_w) == cur_level and new_w != w: # 多次访问。注意第二次判断条件。new_w和w不等。
                                parent[new_w].append(w)
                            elif new_w not in levels: # 当前节点第一次访问
                                parent[new_w] = [w]
                                next_layer.append(new_w)
                                levels[new_w] = cur_level
            frontier = next_layer
            cur_level += 1

        return all_paths

    def find_path(self, parent, begin, end, paths, stack):
        #回
        stack.append(begin)
        if begin == end:
            p = copy.copy(stack)
            p.reverse()
            paths.append(p)
            stack.pop()
            return

        adjs = parent[begin]
        for adj in adjs:
            self.find_path(parent, adj, end, paths, stack)
        stack.pop()



