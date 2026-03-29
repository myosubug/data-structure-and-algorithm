class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_list = {}
        tickets_sorted = sorted(tickets, reverse=True)
        for src, dst in tickets_sorted:
            if src not in adj_list:
                adj_list[src] = []
            adj_list[src].append(dst)

        ret = []
        
        def dfs(city):
            while adj_list.get(city, []):
                next_city = adj_list[city].pop()
                dfs(next_city)
            ret.append(city)

        dfs("JFK")
        return ret[::-1]