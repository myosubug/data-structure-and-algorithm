class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        search_queue = deque()
        visited = set()
        search_queue.append(beginWord)
        visited.add(beginWord)

        wordList_set = set(wordList)
        wordList_set.add(beginWord)
        adj_list = {}
        for word in wordList_set:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                if pattern not in adj_list:
                    adj_list[pattern] = []
                adj_list[pattern].append(word)

        count = 0
        while search_queue:
            count += 1
            for _ in range(len(search_queue)):
                popped = search_queue.popleft()
                if popped == endWord:
                    return count
                for j in range(len(popped)):
                    pattern = popped[:j] + "*" + popped[j+1:]
                    for nei in adj_list.get(pattern, []):
                        if nei not in visited:
                            visited.add(nei)
                            search_queue.append(nei)

        return 0
