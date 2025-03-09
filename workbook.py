
"""
lenth=len("Enter the first number")
print(lenth)

print("hi")

String = "Aromal "
print(String[0])

String2 = "is the class rep"

String+= String2
print(String[0:3])


x = "Aromal and Tom and Blesson is part of the Class Rep Gang"
#spl = x.split()
#fin = x.find('Blesson')
finde=x.strip(" Aromal ")
print(finde)

#print(ret)

#To reverse a string using the slice function
x = "Blesson" [::-1]
print(x)


list = ["Aswin MS", "Tom Sibus", "Alan Joy", "Nikki Tom","Nikki Tom", "Small Elephant"]
#r=set(list)
"""
"""
r=enumerate(list)

for i, word in r:
    print(i,word)
    
x=sorted(list,reverse=True)

x=sorted(list,key=len)
print(x)

"""
#Program to read a list of names and sort in alphabetic order
#Program to remove all duplicates form a list
n=2

switcher = {
    1:10,
    2:20

}

val=switcher.get(n)
print(val)