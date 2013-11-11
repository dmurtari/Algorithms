class Queue:
    def __init__(self):
        self.items = []
        self.size = 0

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def enqueue(self, item):
        self.items.insert(0, item)
        self.size += 1

    def dequeue(self):
        return self.items.pop()
        self.size -= 1
