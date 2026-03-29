class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        counter = Counter(list(s1))

        for i, c in enumerate(list(s2)):
            if c in counter:
                temp = s2[i:i+len(s1)]
                temp_counter = Counter(temp)
                if temp_counter == counter:
                    return True
        
        return False