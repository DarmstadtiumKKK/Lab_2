ss='hello world'
sss='Python one love'

def revers(s):
 i=0
 s1=''
 while i<len(s):
   s1=s1+s[len(s)-i-1]
   i=i+1
 print(s1)
 None

revers(ss)
revers(sss)