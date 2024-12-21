num = int(input("Enter a number:"))
sum = 0
for i in range(1,num+1,1):
    if(i%3==0 or i%5==0):
        sum+=i
print("Your total is:",sum)