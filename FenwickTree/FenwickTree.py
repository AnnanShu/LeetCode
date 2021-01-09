class FenwickTree:
    def __init__(self, n: int):
        self.sums = [0] * (n + 1)
    
    def lowbit(self, x: int) -> int:
        return x & (-x)

    def update(self, i : int, delta: int) -> None:
        while i < len(self.sums):
            self.sums[i] += delta
            i += self.lowbit(i)
    
    def query(self, i: int):
        res = 0
        while i > 0:
            res  += self.sums[i] 
            i -= self.lowbit(i)
            