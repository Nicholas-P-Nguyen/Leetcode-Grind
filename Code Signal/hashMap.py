def solution(queryType, query):
    ht = HashTable()
    results = [ht.operate(qt, q) for qt, q in zip(queryType, query)]
    return sum([r for r in results if r])
    
    
class HashTable:
    def __init__(self):
        self.dict = {}
        self.kshift = 0
        self.vshift = 0
                
    def insert(self, x, y):
        if x - self.kshift in self.dict:
            self.dict[x - self.kshift] = self.dict[x - self.kshift] + y - self.vshift
        else:
            self.dict[x - self.kshift] = y - self.vshift
    
    def get(self, x):
        if x - self.kshift in self.dict:
            return self.dict[x - self.kshift] + self.vshift
        else:
            return None
        
    def addToKey(self, x):
        self.kshift += x
        
    def addToValue(self, y):
        self.vshift += y

    def operate(self, queryType: str, query: list):
        func = None
        try:
            func = getattr(self, queryType)
        except AttributeError:
            raise Exception(f"{queryType} not found")
        return func(*query)