a=input("Enter the values to the list1 :")
b=input("Enter the values to the list 2:")
a=a.split(" ")
b=b.split(" ")
l1=list(a)
l2=list(b)
print(l1)
print(l2)
l=0
f=0
l1sum=0
l2sum=0
if len(l1)==len(l2):
	print("Length of two list are equal")
	l=len(l1)
elif len(l1)>len(l2):
	l=len(l2)
	print("Length of two lists are different")
else:
	l=len(l1)
	print("Length of two lists are different")
for i in range(0,l):
	l1[i]=int(l1[i])
	l1sum=l1sum+l1[i]
	l2[i]=int(l2[i])
	l2sum=l2sum+l2[i]
if l1sum==l2sum:
	print("sum of two list are equal")
else:
	print("sum of two lists are different")
for i in range(0,l):
	l1[i]=int(l1[i])
	for j in range(0,l):
			l2[j]=int(l2[j])
			if l1[i]==l2[j]:
	    			f=f+1
if f==0:
	print("The values of two lists are different")
else:
	print(f," values of two lists are equal")
