# Module 2 Pratice Answers

# 1 Function for flat list 
def countOdd(lst):
    if not isinstance(lst, list):
        return "Error"
    
    count = 0
    for item in lst:
        # check if item is int or a string representing an integer
        if isinstance(item, int):
            if item % 2 != 0:
                count += 1
        elif isinstance(item, str):
            # check if it represents an integer
            if item.lstrip('-').isdigit():  # handles negative numbers
                if int(item) % 2 != 0:
                    count += 1
    return count

#2 
def countOdd(lst):
    if not isinstance(lst, list):
        return "Error"
    
    count = 0
    
    def helper(sublist):
        nonlocal count
        for item in sublist:
            if isinstance(item, int):
                if item % 2 != 0:
                    count += 1
            elif isinstance(item, str):
                if item.lstrip('-').isdigit():
                    if int(item) % 2 != 0:
                        count += 1
            elif isinstance(item, list):
                helper(item)  # recursive call
    
    helper(lst)
    return count


