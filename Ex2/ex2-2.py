a=int(input("enter mark 1:"))
b=int(input("enter mark 2:"))
c=int(input("enter mark 3:"))
d=int(input("enter mark 4:"))
e=int(input("enter mark 5:"))
if(a<=100 and b<=100 and c<=100 and d<=100 and e<=100):
   avg=(a+b+c+d+e)/5
   print("The average is:",avg)
   if(avg>=90):
      print("O grade")
   elif(80<=avg<=89):
      print("A+ grade")
   elif(70<=avg<=79):
      print("A grade")
   elif(60<=avg<=69):
      print("B+ grade")
   elif(55<=avg<=59):
      print("B grade")
   elif(50<=avg<=54):
      print("C grade")
   else:
      print("fail")
else:
   print("Invalid")
