# Exam 3 notes

"""
🧠 MODULE 7: Searching & Sorting
🔍 1. Searching
Linear Search (baseline)
👉 Pattern: check everything one by one
def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

Binary Search (VERY IMPORTANT)
👉 ONLY works on sorted lists
def binary_search(lst, target):
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

🚨 Recognize instantly:
“sorted list” + “efficient” → binary search
unsorted → linear search

🔄 2. Sorting Algorithms
🟡 Bubble Sort
👉 keeps swapping neighbors
def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

🔵 Selection Sort
👉 find min, place it in front
def selection_sort(lst):
    for i in range(len(lst)):
        min_idx = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]

🟢 Insertion Sort (VERY TESTED)
👉 build sorted part step by step
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        
        while j >= 0 and lst[j] > key:
            lst[j+1] = lst[j]
            j -= 1
        
        lst[j+1] = key

⚡ Pattern Recognition
swapping neighbors → bubble
finding minimum → selection
shifting elements → insertion


🧠 MODULE 8: Algorithm Analysis (Big-O)
⏱️ MUST KNOW TABLE
Pattern	            Complexity
single loop	          O(n)
nested loops	      O(n²)
halves each time	  O(log n)
binary search	      O(log n)

🔥 Recognize instantly
Example:
for i in range(n):
    for j in range(n):
        pass

👉 O(n²)
Example:
while n > 1:
    n = n // 2

👉 O(log n)
⚠️ Common Trick:
for i in range(n):
    for j in range(i):

👉 still O(n²) (don’t get tricked)

🧠 MODULE 9: Foundational Programming + Functional + Generators
🔁 1. Functional Programming
🔹 map → transform
list(map(lambda x: x*2, lst))

🔹 filter → condition
list(filter(lambda x: x > 0, lst))

🔹 reduce → combine
functools.reduce(lambda a,b: a+b, lst)

🔹 List Comprehension
[x*2 for x in lst]
[x for x in lst if x > 0]

⚡ Pattern Conversion (VERY TESTED)
map → [expression for x in lst]
filter → [x for x in lst if condition]

🧬 2. Generators (yield)
Core idea:
👉 returns values one at a time

🔹 Accumulator pattern
total = 0
for x in lst:
    total += x
    yield total

🔹 Infinite generator
while True:
    yield value

🔹 Stop condition pattern
while True:
    yield value
    
    if stop_condition:
        break
    
    update value

🔥 HAILSTONE (HIGH PRIORITY)
def hailstone(num):
    while True:
        yield num
        if num == 1:
            break
        elif num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1
⚠️ Recognize:
sequence generation → generator
“until condition” → while True + break
repeating forever → infinite generator

🚨 MOST COMMON EXAM QUESTION TYPES
1. “Write this function”
sorting
searching
generator

2. “Fill in the blank”
You already practiced these — easy points

3. “What is the output?”
👉 trace step-by-step

4. “What is the time complexity?”
👉 identify pattern fast

5. “Fix the bug”
👉 look for:

wrong loop bounds
missing updates
wrong condition

"""