class StringIterator:

    def __init__(self, compressedString: str):
        self.uncompressed = self.uncompress(compressedString)
        self.pointer = 0

    def next(self) -> str:
        ret = ""
        if self.pointer < len(self.uncompressed):
            ret = self.uncompressed[self.pointer]
        else:
            ret = " "
        self.pointer += 1
        return ret
        
    def hasNext(self) -> bool:
        if self.pointer < len(self.uncompressed):
            return True
        else:
            return False


    def uncompress(self, s):
        result = []
        i = 0
        while i < len(s):
            char = s[i]
            i += 1
            # Greedily consume all digits after the character
            j = i
            while j < len(s) and s[j].isdigit():
                j += 1
            count = int(s[i:j]) if j > i else 1
            result.append(char * count)
            i = j
        return "".join(result)


        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
