import operator
d1 = {"Sreejith": 2, "Jeevan": 4, "Akash": 3, "Mohan": 1, "Nikhil": 0}
d2 = {"Science": 5, "Commerce": 6, "Economics": 7, "Politics": 8, "Computer": 9}
print("dictionary1 is ",d1)
print("dictionary2 is ",d2,"/n")
d1.update(d2)
d1 =sorted(d1.items(), key=operator.itemgetter(1))
print(d1)

