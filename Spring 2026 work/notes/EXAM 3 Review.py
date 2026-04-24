# Reviews
"""
EXAM-READY DEFINITIONS (MEMORIZE THIS STYLE)
🟢 Insertion sort:
builds a sorted left portion by inserting elements into the correct position

🟡 Bubble sort:
repeatedly swaps adjacent elements, pushing largest values to the right

🔵 Binary search:
repeatedly divides sorted list in half to locate target

🟣 Linear search:
checks each element one by one

PART 1: BASIC PATTERNS
🟢 1. Single loop → O(n)
for i in range(n):
    print(i)
👉 Answer: O(n)

🟡 2. Nested loops → O(n²)
for i in range(n):
    for j in range(n):
        print(i, j)
👉 Answer: O(n²)

🔵 3. Loop that halves → O(log n)
while n > 1:
    n = n // 2
👉 Answer: O(log n)

🔵 4. Split recursion = O(n log n)
Example:
F1(left half) + F1(right half)
Algorithm	         Complexity
Linear search	       O(n)
Binary search	       O(log n)
Bubble sort	           O(n²)
Selection sort	       O(n²)
Insertion sort	       O(n²)

MODULE 9 — FUNCTIONAL PROGRAMMING
🔥 1. MAP = TRANSFORM EVERY ELEMENT
Pattern:
list(map(lambda x: x + 1, lst))
👉 THINK:
same size output
every element changes

🔥 2. FILTER = KEEP SOME ELEMENTS
Pattern:
list(filter(lambda x: x > 0, lst))
👉 THINK:
reduces list size
condition must be TRUE/FALSE

🧠 3. LIST COMPREHENSION (VERY IMPORTANT)
🔥 Pattern:
[expression for item in list if condition]
Example:
[x*2 for x in lst if x > 0]

🧠 4. GENERATORS (HIGH FREQUENCY EXAM TOPIC)
🔥 PATTERN:
def gen(lst):
    for x in lst:
        yield x
👉 KEY IDEA:
pauses function
returns one value at a time

🔥 ACCUMULATOR PATTERN (VERY COMMON)
def accum(lst):
    total = 0
    for x in lst:
        total += x
        yield total

🧠 5. RECURSION (MOST IMPORTANT PART OF MODULE 9)
🔥 PATTERN:
if list:
    recurse
else:
    process value
Example:
Flattening / nested lists:
def flatten(lst):
    for x in lst:
        if isinstance(x, list):
            yield from flatten(x)
        else:
            yield x

🧠 MINI EXAM RULES FOR MODULE 9
You MUST remember:
map: ✔ transform, changes values
filter: ✔ remove, removes values
comprehension: ✔ compact loop
generator: ✔ one-by-one output,  sequence over time
recursion:✔ nested structure = recursive call

🟢 SAFE PATTERNS:
Searching:  for i in range(len(lst))
Functional: lambda x:
Generator:  yield inside loop
Recursion:  if isinstance(x, list)

Q1 — Identify the Sorting Algorithm
Each sequence shows two consecutive steps from an algorithm. Identify which
sorting algorithm is used.
Scenario A
[12, 5, 8, 19, 2]
[5, 12, 8, 19, 2]
[5, 8, 12, 19, 2]
Options:
a) Bubble sort
b) Merge sort
c) Selection sort
d) Insertion sort
e) Quick sort
Answer:
d) Insertion sort

Elements are being inserted into the sorted prefix one at a time.
Scenario B
[18, 3, 27, 14, 9]
[9, 3, 14, 18, 27]
[3, 9, 14, 18, 27]
Answer:
c) Selection sort

It repeatedly selects the smallest remaining element.
Scenario C
[33, 12, 48, 7, 20]
[12, 7, 20, 33, 48]



[7, 12, 20, 33, 48]
Answer:
e) Quick sort
The pivot is moved to its correct position and partitions appear.

Q2 — Big-O Reasoning
Give the asymptotic worst-case runtime for searching for a value in an unordered list,
and explain briefly.
Answer:
O(n)
You may need to inspect every element until the target is found or the list ends.

Q3 — Designing a Case Where Binary Search Is
Slow
Construct a sorted list of 15 elements where binary search takes the maximum
number of comparisons to find the target value 42.
Answer:
Binary search takes the longest when the target appears in the last position that will
be inspected.
Example valid list:
[5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 40, 41, 42]
Searching for 42 takes the maximum number of halving steps.

Q4 — Basic List Comprehension
Given:
sales = [
{"name": "A", "values": [5, 6, 10]},


{"name": "B", "values": [1, 3]},
{"name": "C", "values": [20, 4, 6]}
]
Write a list comprehension that returns the names whose list sum is less than 10.
sales = [
{"name": "A", "values": [5, 6, 10]},
{"name": "B", "values": [1, 3]},
{"name": "C", "values": [20, 4, 6]}
]
[x["name"] for x in sales if sum(x["values"]) < 10]
['B']
Answer:
[x["name"] for x in sales if sum(x["values"]) < 10]

Q5 — Functional Programming
Write a single expression that uses map to take the list:
nums = [2, 3, 4]
and returns a new list containing each number tripled.
nums = [2, 3, 4]
list(map(lambda x: 3*x, nums))
[6, 9, 12]
Answer:
list(map(lambda x: 3*x, nums))

Q6 — Pipeline Mental Model
Suppose:
def f1(x): return x + 2
def f2(x): return x * 5
def f3(x): return x - 1
Given the pipeline: list [1, 3] ?
[f1, f2, f3], what is the output of the pipeline applied to the
Answer:
For element 1:
1 → f1 → 3 → f2 → 15 → f3 → 14
For element 3:
3 → 5 → 25 → 24
Final answer: [14, 24]

Q7 — Iterator Behavior
You have a predicate:
def is_pos(x): return x > 0
And the iterator is supposed to return every 3rd positive integer.
If the list is:
[-1, 2, -5, 7, 0, 9, 11, -3, 15]
What values should the iterator yield?
def is_pos(x):
return x > 0
def every_third_positive(lst, predicate):
count = 0
for x in lst:
if predicate(x):
count += 1
if count % 3 == 0:
yield x
# Example usage
lst = [-1, 2, -5, 7, 0, 9, 11, -3, 15]
print(list(every_third_positive(lst, is_pos)))
[9]
Answer:
Positive values in order: [2, 7, 9, 11, 15]


Every 3rd: 9 (the 3rd)
So the iterator yields:
[9]

Q8 — Recursive Flatten
Given:
data = [1, [2, [3, 4], 5], 6]
Write the fully flattened list.
def flatten(lst):
for item in lst:
if isinstance(item, list):
for subitem in flatten(item): # recursively iterate
yield subitem
yield item
else:
# Example usage
data = [1, [2, [3, 4], 5], 6]
flat_list = list(flatten(data))
print(flat_list)
[1, 2, 3, 4, 5, 6]
Answer:
[1, 2, 3, 4, 5, 6]

Q9 — Running Total Generator
Consider a list of numbers:
data = [3, 1, 4, 1, 5, 9, 2]
Write a generator that yields the running total of the list.
What sequence does it produce?
def running_total(lst):
total = 0
for x in lst:
total += x
yield total



data = [3, 1, 4, 1, 5, 9, 2]
print(list(running_total(data)))
[3, 4, 8, 9, 14, 23, 25]
Answer:
Running totals: 3, 3+1=4, 4+4=8, 8+1=9, 9+5=14, 14+9=23, 23+2=25
So output: [3, 4, 8, 9, 14, 23, 25]

Q10 — Write a Simple Sum Function
Write a function sum_all(lst) that computes the sum of a list using a loop.
Answer:
def sum_all(lst):
s = 0
for x in lst:
s += x
return s

Q11 — Recursion
Write a recursive function that counts how many times the number 0 appears in
nested lists.
Example:
count_zero([0, [1, 0], [0, [2, 0]]]) → 4
Answer:
def count_zero(lst):
total = 0
for x in lst:
if isinstance(x, list):
total += count_zero(x)
elif x == 0:
total += 1
return total

Q12 — Generator
Write a generator inclusive.
evens_up_to(n) that yields all even numbers from 0 to n
Answer:
def evens_up_to(n):
for i in range(0, n+1, 2):
yield i
Double-click (or enter) to edit
"""