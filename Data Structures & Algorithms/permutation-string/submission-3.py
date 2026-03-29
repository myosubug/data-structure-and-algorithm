class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = Counter(s1)
        window = Counter(s2[:len(s1)])
        if counter == window:
            return True

        for right in range(len(s1), len(s2)):
            new_char = s2[right]
            window[new_char] += 1

            exiting_char = s2[right - len(s1)]
            window[exiting_char] -= 1

            if window[exiting_char] == 0:
                del window[exiting_char]
            
            if counter == window:
                return True
                
        return False