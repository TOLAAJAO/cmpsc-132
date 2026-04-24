# Module 1 Pratice Exercise

# 1 Write a function that receives two integers and decides if the first divides the second, without using the % operator, giving
# a 0-division warning.
def is_divisible(x,y):
    """"
    >>> is_divisible(78,-2)
    True
    >>> is_divisible(63,9)
    True
    >>> is_divisible(63,2)
    False
    >>> is-divisibel(63,8)
    False
    """
   
    if y == 0:
        print("Zero division Error")
        return None
    x = abs(x)
    y = abs(y)
    while x >= y:
        x = x-y
    if x == 0:
        return True
    else:
        return False
    
# 2 Write a function that takes a positive integer as a parameter and returns the sum of all digits in that number. You cannot type
#  convert the number to iterate over the digits. Hint: he last digit of number is number % 10. Discard the last digit using number // 10.
# Step 1: Get the last digit n1. n1 = number % 10. Step 2: Get the second last digit n2. number = number // 10. n2 = number % 10.
def sum_digits(num):
    '''
        >>> sum_digits(2456) 
        17
        >>> sum_digits(2400562) 
        19
        >>> sum_digits(8954565211) 
        46 
    '''
    total = 0
    while num > 0:
        digit = num%10
        total += digit
        num = num//10
    return total

# 3 An ISBN-10 (International Standard Book Number) consists of 10 digits: d1d2d3d4d5d6d7d8d9d10. The last digit, d10, is a checksum, 
# which is calculated from the other nine digits using the following formula: If the checksum is 10, the last digit is denoted as X
#  according to the ISBN-10 convention. Write a function that takes a positive number as a parameter and returns a string that 
# represents the 10-digit ISBN (including leading zeros).
def get_isbn(part_num):
    '''
        >>> get_isbn(3601267)
        '003601267X'
        >>> get_isbn(13601267)  
        '0136012671'
        >>> get_isbn(13031997)  
        '013031997X'
    '''
    total = 0
    k = 9
    isbn = ['0'] * 10
    while part_num > 0 and k > 0:
        digit = part_num%10
        total += (digit * k)
        k -= 1
        isbn[k] = str(digit)
        part_num = part_num//10
    
    checksum = total % 11
    if checksum == 10:
        isbn[9] = 'X'
    else:
        isbn[9] = str(checksum)
    
    return ''.join(isbn)

# 4 Write a function that takes a list of numbers seq, and two integers that will represent a lower and upper bound. The function 
# returns a list of coordinate pairs (lists) such that: Each (x, y) pair is represented as [x, x**2] The x-coordinates are elements 
# in seq. The result contains only pairs whose y-coordinate is within the upper and lower bounds (inclusive)
def get_pairs(seq, lower, upper):
    '''
        >>> get_pairs([-4, -2, 0, 1, 3], 1, 9) 
        [[-2, 4], [1, 1], [3, 9]]
        >>> get_pairs([9, 2, 78, 12, 5, 1, 3], 8, 100) 
        [[9, 81], [5, 25], [3, 9]]
    '''
    output = []
    for num in seq:
        square_num = num**2
        if lower <= square_num <= upper:
            output.append([num, square_num])
    return output

# 5 Write that function that given a dictionary d, it creates a new dictionary that reverses the keys and values of d. Thus, the 
# keys of d become the values of the new dictionary and the values of d become the keys of the new dictionary. You may assume d
#  contains no duplicate values (that is, no two keys map to the same values.) 
def inverse(d):
    '''
        >>> inverse({1:'Hello', 'keys': 26, 'sara': '123-456-7890'}) 
        {'Hello': 1, 26: 'keys', '123-456-7890': 'sara'}
    '''
    inv_d = {}
    for key in d:
        val = d[key]
        inv_d[val] = key
    return inv_d

# 6 Write that function that given dictionaries, d1 and d2, it creates a new dictionary with the following property: for each entry
#  (a, b) in d1, if there is an entry (b, c) in d2, then the entry (a, c) should be added to the new dictionary. For example, if d1 
# is {2:3, 8:19, 6:4, 5:12} and d2 is {2:5, 4:3, 3:9}, then the new dictionary should be {2:9, 6:3}.
def matching_pairs(d1, d2):
    '''
        >>> matching_pairs({2:3, 8:19, 6:4, 5:12}, {2:5, 4:3, 3:9})
        {2: 9, 6: 3}
        >>> matching_pairs({2:3, 8:19, 6:4, 5:12}, {2:5, 4:3, 3:9, 19:236.56}) 
        {2: 9, 8: 236.56, 6: 3}
    '''
    output = {}
    for key in d1:
        value = d1[key]
        if value in d2.keys():
            output[key] = d2[value]
    return output
