
# Identification number is valid if the sum is divisible by 10 (ie: 176248 = 30)

import math
from posixpath import split

# Prompt user for a number
input = input("Number: ")
print(f"{input}")

# Blank list to push new numbers
list = []


# Using input, double the value of every other digit
count = 0
for i in input:
    count += 1
    if count % 2 == 0:
        j = int(i) * 2
        j = str(j)
        for x in j:
            list.append(x)
    else:
        list.append(i)
    
# Add every digit together for checksum (ie: 17, add 1 and 7 not 17)
check_sum = 0

for sum in list:
    check_sum = int(sum) + check_sum

# If checksum not divisible by 10, add up until true
final_num = 0
new_sum = check_sum
while new_sum % 10 != 0:
    new_sum += 1
    final_num += 1

 # Validate if input was divisible by 10

if check_sum  == new_sum:
    print("Validated")
else:
    print("Access denied")  

#print(f"{list}")
print(f"OG sum: {check_sum}")
print(f"Check sum: {new_sum}")
#print(f"Check digit: {final_num}")

