a=input("Enter the values to the list :")
a=a.split(" ")
l=list(map(int,a))
l2=[]
print(l)
for i in l:
	if i%2!=0:
		l2.append(i)
print(l2)

