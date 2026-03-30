sum1=0
sqtot=0
for x in range (1,6):
   sum1+=x
   sqtot+=(x*x)
print "Sum of natural numbers: ",sum1
print "Sum of squares of natural numbers: ",sqtot
[23bee052@mepcolinux python]$python sos.py
Sum of natural numbers:  15
Sum of squares of natural numbers:  55
[23bee052@mepcolinux python]$cat star.py
a=int(input("enter the limit: "))
l=1
for x in range (l,a+1):
   print(" "*(a-x),"* "*x)
for y in range (a-1, l-1, -1):
   print(" "*(a-y),"* "*y)
