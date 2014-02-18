from binaryHeap import BinaryHeap

class Huffman():
    
    def __init__(self, text):
        self.text = text
        self.codebook = {}
        self.encoded = list()

        
    def readInput(self):
        for char in self.text:
            if self.codebook.has_key(char):
                self.codebook[char] += 1
            else:
                self.codebook[char] = 1
    
def main():
    huffman = Huffman("hello")
    huffman.readInput()
    print huffman.codebook
    
if __name__ == "__main__":
    main()