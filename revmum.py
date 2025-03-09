#Program to find the reverse of a number
num=1000
strin = str(num)
print(strin)
ans=0
for i in range(0,len(strin),1): #can do this using while:    while num!=0
    rev=num%10
    ans=ans*10+rev
    num=num//10    #2 slashes for division and 1 slash for 
    

print(ans)

