#Program to read a list and sort in alphabetic order without using sort function


"""
n = int(input("Enter the size"))
list[n]

for i in range(n):
    list.append(input("Num"))

print(list)


"""

dict={'Name':"Aswin",'Age':'20'}
# to print values only from a dict
for key,values in dict.items():
    print(values)
    print(f"{key}:{values}")
"""

for item in list:
    if(item in dict):
        dict[item]+=1

    else:
        dict[item]=1


print(dict)
mykeys=list(dict.keys())
mykeys.sort()
sortedd_dict={i: dict[i] for i in mykeys}
###########sorted_dict=sortedd_dict(reversed(mykeys))
print(sortedd_dict)
"""