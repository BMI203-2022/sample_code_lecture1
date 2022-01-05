#!/usr/bin/env python3

import time

class Memoizer:
    """
    Memoization is a means of avoiding repeating calculations
    """
    def __init__(self):
        self.memory = {}

    def process(self, x: int):
        """
        checks if `_work` has already been called
        for the provided number
        """
        if x not in self.memory:
            self.memory[x] = self._work(x)
        return self.memory[x]

    def _work(self, x: int):
        """
        this is a long calculation
        """
        print("working...")
        time.sleep(1)
        return x * 2
    
    def __repr__(self) -> str:
        """
        string representation of object
        """
        return f"<Memoizer> with {len(self.memory)} objects"


memo = Memoizer()
print(memo.process(1))
print(memo.process(2))
print(memo.process(1))
print(memo.process(2))

print(memo)
