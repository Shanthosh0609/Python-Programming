s=input("Enter:")
list1=s.split(',')
list2=[]
print(list1)
for x in list1:
   if int(x,2)%5==0:
      list2.append(x)
   else:
      continue
print(list2)
