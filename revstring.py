class solution:
  def reversString(self,s: list[str]) -> None:
    def myrev(left,right,l):
      if left>=right:
        return
      s[left],s[right]=s[right],s[left]
      myrev(left+1,right-1,s)
     myrev(left=0,right=len(s)-1,l=s)
