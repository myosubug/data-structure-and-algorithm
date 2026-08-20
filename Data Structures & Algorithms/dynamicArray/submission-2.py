class DynamicArray:
    
    def __init__(self, capacity: int):
        self.cap = capacity
        self.arr = [0] * self.cap
        self.current_size = 0


    def get(self, i: int) -> int:
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        self.arr[i] = n



    def pushback(self, n: int) -> None:
        if self.current_size == self.cap:
            self.resize()
    
        self.arr[self.current_size] = n
        self.current_size += 1


    def popback(self) -> int:
        if self.current_size > 0:
            self.current_size -= 1
            return self.arr[self.current_size]
        return -1
 

    def resize(self) -> None:
        self.cap = self.cap * 2
        new_arr =  [0] * self.cap
        
        for i in range(self.current_size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def getSize(self) -> int:
        return self.current_size


        
    
    def getCapacity(self) -> int:
        return self.cap