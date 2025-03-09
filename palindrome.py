#Program to find the palindrome of a String
num=121
strin = str(num)
print(strin)
ans=0
temp=strin
for i in range(0,len(strin),1): #can do this using while:    while num!=0
    rev=num%10
    ans=ans*10+rev
    num=num//10    #2 slashes for division and 1 slash for 
    

if(str(ans)==temp):
    print("It is a Palindrome.")
else:   
    print("It is not a Palindrome")