class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        visited = set()
        queue = deque()
        queue.append(beginWord)
        visited.add(beginWord)

        adj_list = {}
        wordList_set = set(wordList)
        wordList_set.add(beginWord)
        for word in wordList_set:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                if pattern not in adj_list:
                    adj_list[pattern] = []
                adj_list[pattern].append(word)

        count = 0
        while queue:
            count += 1
            for _ in range(len(queue)):
                popped = queue.popleft()
                if popped == endWord:
                    return count
                for j in range(len(popped)):
                    pattern = popped[:j] + "*" + popped[j+1:]
                    for nei in adj_list[pattern]:
                        if nei not in visited:
                            visited.add(nei)
                            queue.append(nei)
        
        return 0