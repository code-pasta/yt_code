# 1 STEP

def make_str(str_char,number_times):
   res = ''

   for i in range(number_times):
       res += str_char
   return res

# 2 STEP
import math
def print_str_tree(str_char, max_line) :
    start_position = math.ceil(max_line/2.0)
    current_line = 1
    str_space = ' '

    while start_position >= 1 :
        print(make_str(str_space, start_position) + make_str(str_char, current_line))
        current_line +=2
        start_position -=1

# 3 STEP 

symbol = input("Enter a symbol : ")
number = int(input("Enter a natural number : "))

print_str_tree(symbol, number)
