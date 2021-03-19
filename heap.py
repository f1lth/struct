class MaxHeap:
    def __init__(self):
        self.arr = []
        self.size = 0

    def extract(self):
        if len(self.arr) == 0:
            return -1
        else:
            root = self.arr[0]
            # Check if that was the only element in the array
            if len(self.arr) == 1:
                del self.arr[0]
                return root
            else:
                # Reheapify the heap such that the parent value 
                # is larger than either child's.
                self.arr[0] = self.arr[-1]
                del self.arr[-1]
                # Reheapify
                for i in range((len(self.arr)//2),  0, -1):
                    #print(i)
                    left = self.arr[(i)//2]
                    right = self.arr[(i-1)//2]
                    larger = max(left,right)

                    if self.arr[i] <= larger:
                        self.arr[i] = larger
        return root
    
    def add(self, x):
        self.arr.append(x)
        self.size += 1
    
        idx = len(self.arr) - 1 
        while self.arr[idx] > self.arr[(idx - 1) // 2]:
            # We dont want idx to dip back into the negatives
            if self.arr[(idx - 1) // 2] == self.arr[-1]:
                break

            cur = self.arr[idx]
            self.arr[idx] = self.arr[(idx - 1) // 2]
            self.arr[(idx - 1) // 2] = cur

            idx = (idx - 1) // 2

        
    def printHeap(self):
        for i in range(len(self.arr)):
            print(self.arr[i])


if __name__ == '__main__':
    h = MaxHeap()
    h.add(9)
    h.add(7)
    h.add(5)
    h.add(1)
    h.add(2)
    h.add(12)
    h.printHeap()

    print(h.extract())
