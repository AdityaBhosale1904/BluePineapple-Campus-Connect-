#====  Find total occurences of each digits(0-9) using function  ====#
#====================================================================#


# Function to Calculate Occurences of each Digits(0-9)
def DigitOccurence(Number):
    dict={}
    while Number != 0:
        try:
            dict[int(Number%10)]+=1
        except:
            dict[int(Number%10)]=1
        Number=int(Number/10)
    
    print("Occurrence of each digit: ")    
    for i in dict:
        print('Occurrence of digit', i,':',dict[i])

         
Number=int(input('Enter the Number: '))
DigitOccurence(Number)