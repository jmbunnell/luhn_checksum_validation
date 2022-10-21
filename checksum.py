# 

# Then, add the values of the individual digits together (ie: 17, add 1 and 7 not 17)

# Identification number is valid if the sum is divisible by 10 (ie: 176248 = 30)

import math

# Prompt user for a number
input = input("Number: ")
print(f"{input}")

# Blank list to push new numbers
new = []


# Using input, double the value of every other digit
count = 0
for i in input:
    count += 1
    if count % 2 == 0:
        j = int(i) * 2
        new.append(j)
    else:
        new.append(int(i))
    
print(f"{new}")

