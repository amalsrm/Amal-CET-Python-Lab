w=input("Enter a line of text \n")
w=w.split(" ")
l=[]
for i in w:
        if i not in l:
                l.append(i)
for i in l:
	print(i," is repeated",w.count(i),"time")

		
