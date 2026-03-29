class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}

        for w in words:
            for c in w:
                if c not in adj:
                    adj[c] = set()

        indegree = {c: 0 for c in adj.keys()}
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break

        q = deque()
        for c in indegree.keys():
            if indegree[c] == 0:
                q.append(c)
        
        res = []

        while q:
            popped = q.popleft()
            res.append(popped)
            for nei in adj[popped]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        if len(res) != len(adj):
            return ""

        return "".join(res)