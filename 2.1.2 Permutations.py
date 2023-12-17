class Permutation:
  def __init__(self,n):
    self.n=n
    self.permutation=[]
    self.chosen=[False]*(self.n+1)
  def search(self):
      if len(self.permutation)==self.n:
        print(self.permutation)
      else:
        for i in range(1,self.n+1):

          if self.chosen[i]:
            continue
          else:
            self.permutation.append(i)
            self.chosen[i]=True
            self.search()
            self.chosen[i]=False
            self.permutation.pop()


perms=Permutation(3)
perms.search()
