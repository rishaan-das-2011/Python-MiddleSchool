"""
LESSON: 6.2 - Return Values
WARMUP 2
"""

#### -------------------------------- ####
#### ---- DOUBLE NUMBER FUNCTION ---- ####
#### -------------------------------- ####
def double_number(num):
    new_num = num * 2
    return new_num


#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####

num = int(input("Enter a number: "))
doubled = double_number(num)
print("The number doubled is " + str(doubled))