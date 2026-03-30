a=int(input("enter the limit: "))
l=1
for x in range (l,a+1):
   print(" "*(a-x),"* "*x)
for y in range (a-1, l-1, -1):
   print(" "*(a-y),"* "*y)
