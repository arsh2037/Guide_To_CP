class Subsets:
    def __init__(self, n,subset=[]):
      self.n=n
      self.subset=subset
    def search(self,k):
      if k==self.n+1:
       print(self.subset)
      else:
        self.subset.append(k)
        self.search(k+1)
        self.subset.pop()
        self.search(k+1)


subset=Subsets(3)
subset.search(1)
