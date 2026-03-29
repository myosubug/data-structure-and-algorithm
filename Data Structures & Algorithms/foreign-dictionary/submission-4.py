class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj_list = defaultdict(set)
        in_degree = defaultdict(int)
        all_chars = set("".join(words))
        for char in all_chars:
            in_degree[char] = 0

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1.startswith(w2):
                    return ""
            
            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in adj_list[w1[j]]:
                        adj_list[w1[j]].add(w2[j])
                        in_degree[w2[j]] += 1
                    break

        queue = deque()
        ret = []

        for c in all_chars:
            if in_degree[c] == 0:
                queue.append(c)

        
        while queue:
            popped = queue.popleft()
            ret.append(popped)

            for nei in sorted(list(adj_list[popped])):
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)

        if len(ret) == len(all_chars):
            return "".join(ret)
        else:
            return ""