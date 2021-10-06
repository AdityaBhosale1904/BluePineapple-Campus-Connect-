#====  write a program to print all perfect numbers between 1 to n  ===#
#======================================================================#

# Function to check perfect number
def perfect_number(n):
    if n< 1:
        return False
    perfect_sum = 0
    
    for i in range(1,n):
        if n%i==0:
            perfect_sum += i
    return perfect_sum == n

#Accepting umber from user to print perfect numbper upto that range
number = int(input('Enter maximum value: '))

#displaying Perfect Numbers
print('Perfect numbers from %d to %d are:' %(1,number))
for i in range(1, number+1):
    if perfect_number   (i):
        print(i, end=' ')