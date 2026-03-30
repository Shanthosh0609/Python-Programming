n=int(input("Enter the number: "))
fact=1
if n<0:
   print("Invalid input")
elif n==0:
   print("Factorial is: 1")
else:
   for i in range(1,n+1):
      fact*=i
   print("The factorial is: ",fact)
