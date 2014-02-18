class Fibonacci:

    def __init__(self):
        self.F = {}
        
    def recursive(self, n):
        if n < 2: 
            return n
        else:
            return self.recursive(n - 1) + self.recursive(n - 2)
    
    def memoization(self, n):
        
            
          
def main():
    fib = Fibonacci()
    print fib.recursive(10)
  
if __name__ == "__main__":
    main()