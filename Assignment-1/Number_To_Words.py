import re
ones = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 
'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 
'Nineteen']

tens = ['', '', 'Twenty', 'Thirty', 'Fourty','Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

suffix = ['', 'Thousand', 'Million', 'Billion', 'Trillion', 'Quadrillion', 'Quintillion', 
'Sextillion', 'Septillion', 'Octillion', 'Nonillion', 'Decillion', 'Undecillion',
'Duodecillion','Tredecillion', 'Quattuordecillion','Quindecillion','Sexdecillion',
'Septendecillion','Octodecillion','Novemdecillion','Vigintillion','Unvigintillion',
'Duovigintillion','Trevigintillion','Quattourvigintillion','Quinvigintillion',
'Sexvigintillion','Septenvigintillion','Octovigintillion','Novemvigintillion',
'Trigintillion','Untrigintillion','Duotrigintillion']

# function to split number in 3 digit numbers
def split_number(number, splitted_number):
    if number == 0:
        return splitted_number
    splitted_number.append(number % 1000)
    return split_number(number//1000, splitted_number)

#function to convert 3 digit numbers into words
def num_to_words(num):
    str = ''
    if num > 99:
        str += ones[num//100] + 'Hundred'
    if num % 100 < 20:
        str += ones[num % 100]
    else:
        num %= 100
        str += tens[num//10]
        num %= 10
        str += ones[num]
    return re.sub(r'(\w)([A-Z])', r'\1 \2', str) 

#function to add suffix to numbers 
def add_suffix(splitted_num_list):
    num_list = []
    for index, num in enumerate(splitted_num_list):
        if splitted_num_list[index]:
            num_list.append(splitted_num_list[index]+' '+suffix[index])
    return num_list

def main(number):
  
    if int(number) == 0:
        return 'Zero'

    splitted_num_list = split_number(int(number), []) 
    num_word_list = list(map(num_to_words, splitted_num_list)) 
    num_word_list = add_suffix(num_word_list) 
    num_word_list.reverse()

    num_into_word = ''
    for word in num_word_list:
        num_into_word += word+ ' '
    return num_into_word

# Input
number = input('Enter a number: ')
while not number.isdigit():
    print('Invalid Input, pleast enter a number')
    number = input('Enter a number: ')
print(main(number)) 

