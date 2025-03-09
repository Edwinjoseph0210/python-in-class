""" #Multiline Comment Used
#print('Hello. First python lesson in college.')

#for i in range(0,100,10):
    #print(i)

#fibonocci series
#a =0

b =1
print(a)
print(b)
for i in range(0,10,1):
    temp=a
    a=b
    b=temp+b
    print(b)
#
#Swapping Two Numbers

n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))
temp=n1
n1=n2
n2=temp
print("First Number is:",n1)
print("First Number is:",n2)
"""

text = "PythonSlicing"

print(text[0:6])    # 'Python'  (Characters from index 0 to 5)
print(text[:6])     # 'Python'  (Start defaults to 0)
print(text[6:])     # 'Slicing' (Stop defaults to end)
print(text[::-2])      # 'PythonSlicing' (Copies the entire string)
