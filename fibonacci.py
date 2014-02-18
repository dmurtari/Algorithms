class Fibonacci:

    def __init__(self):
        self.M = {}
        self.F = list()
        
    def recursive(self, n):
        if n < 2: 
            return n
        else:
            return self.recursive(n - 1) + self.recursive(n - 2)
    
    def memoization(self, n):
        if n < 2:
            return n
        else:
            if not self.M.has_key(n):
                self.M[n] = self.memoization(n - 1) + self.memoization(n - 2)
            return self.M[n]
            
    def iteration(self, n):
        self.F.append(0)
        self.F.append(1)
        for i in range(2, n + 1):
            self.F.append(self.F[i - 1] + self.F[i - 2])
        return self.F[n]
            
          
def main():
    fib = Fibonacci()
    print fib.recursive(10)
    print fib.memoization(10)
    print fib.iteration(10)
  
if __name__ == "__main__":
    main()