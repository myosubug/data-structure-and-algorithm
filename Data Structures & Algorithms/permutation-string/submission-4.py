class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = Counter(s1)
        window = Counter(s2[:len(s1)])
        left = 0

        if counter == window:
            return True

        for i in range(len(s1), len(s2)):
            new_char = s2[i]
            window[new_char] += 1

            existing_char = s2[left]
            window[existing_char] -= 1

            if window[existing_char] == 0:
                del window[existing_char]
            left += 1
            if counter == window:
                return True

        
        return False