a=input("Enter the values to the list:")
a=a.split(" ")
l=list(a)
print(l)
for i in range(0,len(l)):
	l[i]=int(l[i])
	if l[i]>100:
		l[i]=str("over")
print(l)
		
		


