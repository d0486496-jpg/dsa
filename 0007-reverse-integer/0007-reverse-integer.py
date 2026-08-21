class Solution(object):
    def reverse(self, x):
      b=str(x)
      if(b[0]=="-"):
        f="-" + b[:0:-1]
        f=int(f)
      else:
        f=b[::-1]
        f=int(f)
      if(f<-2**31 or f>2**31-1):
        return 0
      return f

