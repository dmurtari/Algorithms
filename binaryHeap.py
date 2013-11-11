class BinaryHeap:

    def __init__(self):
        self.heapList = [0]
        self.size = 0

    def insert(self, element):
        self.heapList.append(element)
        self.size += 1
        self.bubbleUp(self.size)

    def deleteMin(self):
        if self.size == 0:
            return None
        else:
            minVal = self.heapList[1]
            self.heapList[1] = self.heapList[self.size]
            self.size = self.size - 1
            self.heapList.pop()
            self.bubbleDown(1)
            return minVal

    def bubbleUp(self, size):
        while size // 2 > 0:
            if self.heapList[size] < self.heapList[size // 2]:
                temp = self.heapList[size // 2]
                self.heapList[size // 2] = self.heapList[size]
                self.heapList[size] = temp
            size = size // 2

    def bubbleDown(self, element):
        while (2 * element) <= self.size:
            minChild = self.minChild(element)
            if self.heapList[element] > self.heapList[minChild]:
                temp = self.heapList[element]
                self.heapList[element] = self.heapList[minChild]
                self.heapList[minChild] = temp
            element = minChild

    def minChild(self, element):
        if 2 * element + 1 > self.size:
            return 2 * element
        else:
            if self.heapList[2 * element] < self.heapList[2 * element + 1]:
                return 2 * element
            else:
                return 2 * element + 1

    def makeHeap(self, elements):
        i = len(elements) // 2
        self.currentSize = len(elements)
        self.heapList = [0] + elements[:]
        while (i > 0):
            self.bubbleDown(i)
            i = i - 1

def main():
    heap = BinaryHeap()
    heap.insert(3)
    print heap.deleteMin()

if __name__ == "__main__":
    main()