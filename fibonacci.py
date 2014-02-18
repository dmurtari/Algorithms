class Fibonacci:

    def __init__(self):
        self.F = {}
        
    def recursive(self, n):
        if n < 2: 
            return n
        else:
            return self.recursive(n - 1) + self.recursive(n - 2)
    
    def memoization(self, n):
        if n < 2:
            return n
        else:
            if not self.F.has_key(n):
                self.F[n] = self.memoization(n - 1) + self.memoization(n - 2)
            return self.F[n]
            
          
def main():
    fib = Fibonacci()
    print fib.recursive(10)
    print fib.memoization(10)
  
if __name__ == "__main__":
    main()