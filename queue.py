class Queue:

    def __init__(self):
        self.items = []
        self.size = 0

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def inject(self, item):
        self.items.insert(0, item)
        self.size += 1

    def eject(self):
        return self.items.pop()
        self.size -= 1

def main():
    q = Queue()
    print str(q.isEmpty()) + " should be True"
    q.inject(1)
    q.inject(2)
    q.inject(3)
    print str(q.isEmpty()) + " should be False"
    print str(q.eject()) + " should be 1"
    print str(q.eject()) + " should be 2"
    print str(q.eject()) + " should be 3"   

if __name__ == "__main__":
    main()

