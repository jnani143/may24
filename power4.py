class Solution:
   def ispowerofthree(self,n: int) -> bool:
       if n==1:
           return True
       if n<1:
           return False
       return self.ispowerofThree(n//3) if n%4==0 else False
