# Allows for the computation of a given fibonacci number through a variety of
# different ways. 
class Fibonacci:

    def __init__(self):
        self.M = {}
        self.F = list()
        
    # Calulate the nth Fibonaci number recursively. Runs in O(2^n) time and 
    # space
    def recursive(self, n):
        if n < 2: 
            return n
        else:
            return self.recursive(n - 1) + self.recursive(n - 2)
    
    # Improvement over naive recursion by storing intermediate results. Runs in
    # O(n) time and O(n) space
    def memoization(self, n):
        if n < 2:
            return n
        else:
            if not self.M.has_key(n):
                self.M[n] = self.memoization(n - 1) + self.memoization(n - 2)
            return self.M[n]
            
    # Calculate by iteration. Similar to memoization. Runs in O(n) time and O(n)
    # space
    def iteration(self, n):
        self.F.append(0)
        self.F.append(1)
        for i in range(2, n + 1):
            self.F.append(self.F[i - 1] + self.F[i - 2])
        return self.F[n]
    
    # Calculate without storing intermediate results. Runs in O(n) time and O(1)
    # space
    def fasterIteration(self, n):
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b
            
          
def main():
    fib = Fibonacci()
    print "Answer by recursion is: " + str(fib.recursive(30))
    print "Answer by memoization is: " + str(fib.memoization(30))
    print "Answer by iteration is: " + str(fib.iteration(30))
    print "Answer by faster iteration is: " + str(fib.fasterIteration(30))
  
if __name__ == "__main__":
    main()