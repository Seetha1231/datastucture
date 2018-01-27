class stack:
    def __init__(self):
        self.arr=[]
    def push(self,n):
        self.arr.append(n)
    def pop(self):
        if len(self.arr)==0:
            return -1
        else :
            return self.arr.pop()
          
s=stack()
s.push(10)
s.push(11)
s.pop()
