a=int(input("Enter 4 digits:"))
if(1000<=a<=9999):
   sum=0
   temp=a
   while temp!=0:
      r=temp%10
      sum+=r
      temp//=10
   print("The sum is:",sum)
else:
   print("Invalid choice")
