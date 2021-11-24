a=int(input("Enter a number "))
b=int(input("Enter another number"))
gcd=0
if a<b:
	l=a
else:
	l=b
for i in range(1,l+1):
	if (a%i)==0 and (b%i)==0:
		gcd=i
print("GCD of ",a," and ",b," is ",gcd)
