# Exam 3 mock 
"""
THE FAST TEST (USE THIS IN EXAM)
Ask yourself:
❓ Is there a growing sorted section on the left? 👉 YES → Insertion Sort
❓ Is the largest element moving to the far right each pass? 👉 YES → Bubble Sort
🟢 SECTION A — MULTIPLE CHOICE (15 marks)
Q1 — Sorting (5 marks)
Identify the algorithm:
[9, 2, 7, 4]
[2, 9, 7, 4]
[2, 7, 9, 4]
[2, 4, 7, 9]
a) Bubble sort
b) Selection sort
c) Insertion sort
d) Quick sort
answer: insertion sort 

Q2 — Sorting (5 marks)
[6, 3, 8, 1]
[1, 3, 6, 8]
a) Bubble sort
b) Selection sort
c) Insertion sort
d) Merge sort
answer: selection sort 

Q3 — Sorting (5 marks)
[10, 5, 8, 12, 3]
[3, 5, 8, 10, 12]
a) Selection sort
b) Bubble sort
c) Insertion sort
d) Heap sort
answer: insertion sort 

🟡 SECTION B — BIG-O + CONCEPT (20 marks)
Q4 (5 marks)
for i in range(n):
    for j in range(i):
        print(i, j)
Time complexity?
answer: o(n^2)

Q5 (5 marks)
while n > 1:
    n = n // 2
Time complexity?
answer: O(log n)

Q6 (5 marks)
Why is linear search O(n)?
answer: linear search is o(n) because it may need to check evry element in the worst case

Q7 (5 marks)
When is binary search NOT valid?
answer: not valid when the list is not sorted

⚡ LIGHTNING DRILL (FINAL)
🟢 Q1 (Sorting ID)
[5, 2, 9, 1]
[2, 5, 9, 1]
[2, 5, 1, 9]
[1, 2, 5, 9]
👉 What sort?
answer: insertion sort 

🟢 Q2 (Sorting ID)
[8, 3, 6, 2]
[2, 3, 6, 8]
👉 What sort?
answer: selection sort (picks minimum each pass)

🟢 Q3 (Big-O)
for i in range(n):
    print(i)
👉 Complexity?
answer: O(n)

🟢 Q4 (Big-O)
for i in range(n):
    for j in range(n):
        print(i, j)
👉 Complexity?
answer: O(n^2)

🟢 Q5 (Binary Search condition).Binary search works only when list is:
Answer: when the list is sorted

🟢 Q6 (map vs filter). Which one removes elements?
answer:filter

🟢 Q7 (map output)
list(map(lambda x: x+2, [1,2,3]))
answer: [3,4,5]

🟢 Q8 (filter output)
list(filter(lambda x: x > 2, [1,2,3,4]))
answer: [3,4]

🟢 Q9 (recursion check). What must recursion always have?
👉 (1 thing)
answer: must have a base case

🟢 Q10 (generator) What does yield do?
👉 (1 line answer)
answer: yield returns values one at a time

🟢 SECTION A — MCQ (10 marks)
Q1 Which algorithm is MOST likely used?
[9, 4, 1, 7]
[4, 9, 1, 7]
[1, 4, 9, 7]
[1, 4, 7, 9]
a) Selection sort
b) Bubble sort
c) Insertion sort
d) Merge sort
answer- insertion sort 

Q2 What is the time complexity?
for i in range(n):
    print(i)
for j in range(n):
    print(j)
a) O(n²)
b) O(n)
c) O(log n)
d) O(n log n)
answer- O(n^2)

Q3 What does this return?
list(filter(lambda x: x > 3, [1,4,2,6]))
a) [1,2]
b) [4,6]
c) [1,4,2,6]
d) Error
answer- [4,6]

Q4.Binary search worst case time complexity is:
a) O(n)
b) O(n²)
c) O(log n)
d) O(1)
answer- O(log n)

Q5 Which statement is TRUE about map?
a) removes elements
b) modifies every element
c) sorts elements
d) stops after first match
answer- modifies every element

🟡 SECTION B — SHORT ANSWER (10 marks)
Q6. Why is insertion sort O(n²) in worst case?
Answer: Insertion sort is O(n²) because for each element it may need to compare and shift across the already sorted portion, leading to nested comparisons in 
the worst case.

Q7. Difference between map and filter (1–2 lines only)
answer: map transforms every elemnt while filter keeps element that satisfies the condition

Q8. What does a generator do in Python?
answer: a genrator produces a value one at a time using yield putting a pause to execution between outputs

Q9. When does binary search NOT work?
answer: doesn't work when the list is not sorted.

Q10. What is the key idea of recursion in nested lists?
answer: recursion breaks a problem into smaller subproblems until a base case is reached.

FULL MOCK EXAM (CMPSC 132)
Total: 75 marks + 10 bonus
Time mindset: ~75–90 minutes

🟢 SECTION A — MULTIPLE CHOICE (15 marks)
Q1 (3 marks)
Which algorithm is this?
[10, 4, 7, 2]
[4, 10, 7, 2]
[4, 7, 10, 2]
a) Bubble sort
b) Insertion sort
c) Selection sort
d) Merge sort
answer: insertion sort

Q2 (3 marks)
Time complexity:
for i in range(n):
    for j in range(n):
        print(i, j)
a) O(n)
b) O(n log n)
c) O(n²)
d) O(log n)
answer- O(n^2)

Q3 (3 marks)
What does this return?
list(map(lambda x: x + 1, [5,6,7]))
a) [5,6,7]
b) [6,7,8]
c) [5,7,9]
d) Error
answer: [6,7,9]

Q4 (3 marks)
Binary search requires:
a) unsorted list
b) sorted list
c) linked list
d) empty list
answer: sorted list

Q5 (3 marks)
Which best describes filter()?
a) transforms each element
b) removes elements based on condition
c) sorts elements
d) duplicates elements
answer: removes elements based on condition

🟡 SECTION B — SHORT ANSWER (20 marks)
Q6 (5 marks)
Why is binary search O(log n)?
answer: because it is a loop that halves the search space

Q7 (5 marks)
Difference between bubble sort and insertion sort.
answer: bubble sort: swaps adjacent elements repeatedly while insertion sort builds sorted left portion by inserting elemnents 

Q8 (5 marks)
What does a generator do in Python?
answer: a genrator produces a value one at a time using yield putting a pause to execution between outputs

Q9 (5 marks)
What is the difference between map and filter?
answer: map transforms every elemnt while filter keeps element that satisfies the condition

🔴 SECTION C — PROGRAMMING (40 marks)
Q10 — Searching (8 marks)
Write a function that returns the index of a target in a list, or -1 if not found.
def search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i 
    return -1

Q11 — Sorting (10 marks)
Write insertion sort.
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key

Q12 — Functional Programming (6 marks)
Given: nums = [2,3,4]
Return a list where each number is squared using map.
list(map(lambda x: x**2, nums)) 
[4,9,16]

Q13 — Generator (8 marks)
Write a generator that yields running (cumulative) sum.
def accum_sum(lst):
    total_sum = o
    for item in lst:
        total_sum += item
        yield total_sum

Q14 — Recursion (8 marks)
Write a function that counts how many 0s appear in a nested list.
Example:
[0, [1,0], [0,[2]]] → 3
def count_zeros(lst):
    count = 0
    for num in lst:
        if isinstance(num,list):
            count += count_zeros(num)
        elif num ==0:
            count += 1
    return count 

⭐ BONUS QUESTION (10 marks)
Q15 — Pipeline Logic
def f(x): return x + 2
def g(x): return x * 3
def h(x): return x - 1
lst = [1,2]
Apply pipeline: f → g → h
What is the output list?
when x = 1: f= 3 g= 9 h= 8
when x = 2: f= 4 g= 12 h= 11
output = [8,11]

🟢 SECTION A — MULTIPLE CHOICE
Q1
Which algorithm is being used?

[9, 4, 7, 2]
[4, 9, 7, 2]
[4, 7, 9, 2]
a) Bubble
b) Selection
c) Insertion
d) Quick
👉 Your answer: insertion 

Q2
What is the time complexity?
for i in range(n):
    for j in range(i):
        print(i, j)
a) O(n)
b) O(log n)
c) O(n²)
d) O(n log n)
👉 Your answer: O(n^2)

Q3
What does this return?
list(map(lambda x: x+1, [1,2,3]))
a) [1,2,3]
b) [2,3,4]
c) [1,3,5]
d) Error
👉 Your answer: [2,3,4]

🟡 SECTION B — SHORT ANSWER
Q4
Why is binary search O(log n)?
👉 Your answer (1–2 sentences): Binary search is O(long n) because it halves the search space each step

Q5
What is the difference between map and filter?
👉 Your answer: map- tranforms every element, filter- keeps element that satisfy a condition

🔴 SECTION C — PROGRAMMING
Q6 — Generator (HIGH PRIORITY)
Write a generator count_down(n) that yields: n, n-1, n-2, ..., 0
👉 Your code:
def count_down(n):
    while n >= 0:
        yield n
        n-= 1

Q7 — List Comprehension
Given: nums = [3, -1, 4, -5, 2]
Return a list of only positive numbers doubled.
👉 Your answer:
[i * 2 for i in nums if i > 0]

Q8 — Searching
Write a function that returns True if a target exists in a list, otherwise False.
👉 Your code:
def search(lst,target):
    for i in lst:
        if i == target:
            return True
    return False

Q9 — Running Total
Write a generator that yields cumulative sums of a list.
👉 Your code:
def accum_sum(lst):
    total_sum = o
    for item in lst:
        total_sum += item
        yield total_sum

Q10 — Recursion
Write a function that counts how many EVEN numbers are in a nested list.
Example:
count_even([1, [2, 3, [4]], 6]) → 3
👉 Your code:
def count_even(lst):
    count = 0
    for num in lst:
        if isinstance(num, list):
            count += count_even(num)
        elif num % 2 == 0:
            count += 1
    return count 



MOCK EXAM (CMPSC 132) — ROUND 2
Total: 75 + 10 Bonus

🟢 SECTION A — MULTIPLE CHOICE (15 marks)
Q1 (3 marks)
Which algorithm is this?
[6, 2, 9, 4]
[2, 6, 9, 4]
[2, 4, 6, 9]
a) Bubble sort
b) Insertion sort
c) Selection sort
d) Quick sort
answer - Bubble sort 

Q2 (3 marks)
What is the time complexity?
for i in range(n):
    for j in range(n):
        print(i, j)
a) O(n)
b) O(n²)
c) O(log n)
d) O(n log n)
answer - O(n^2)

Q3 (3 marks)
What does this return?
list(filter(lambda x: x % 2 == 0, [1,2,3,4,5]))
a) [1,3,5]
b) [2,4]
c) [1,2,3,4,5]
d) Error
Answer - [2,4]

Q4 (3 marks)
Binary search works ONLY when:
a) list is empty
b) list is sorted
c) list has duplicates
d) list is unsorted
Answer- list is sorted

Q5 (3 marks)
Which operation describes map()?
a) filters elements
b) sorts elements
c) transforms every element
d) removes duplicates
Answer- transforms every element

🟡 SECTION B — SHORT ANSWER (20 marks)
Q6 (5 marks)
Explain why binary search is O(log n).
Answer - Binary search is O(log n) because it repeatedly divides the search space in half each iteration, reducing the number of elements to check exponentially

Q7 (5 marks)
Difference between map and filter.
Answer - Map transforms each element and filter keeps elemnts that satisfy a condition

Q8 (5 marks)
What is the difference between bubble sort and insertion sort?
Answer- bubble sort repeatedly swaps adjacent elements, pushing largest to the end each pass while insertion sort builds a sorted left portion by inserting elements
into correct position.

Q9 (5 marks)
What does a generator do in Python?
Answer- generator produces value one at a time using yield, pausing execution between outputs

🔴 SECTION C — PROGRAMMING (40 marks)
Q10 — Searching (8 marks)
Write a function that returns the index of a target in a list or -1 if not found.
def search(lst,target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

Q11 — Sorting (10 marks)
Write insertion sort.
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key

Q12 — Functional Programming (6 marks)
Given: nums = [1,2,3,4]
Return list of squares using map.
list(map(lambda x: x**2, nums))
= [1,4,9,16]

Q13 — Generator (8 marks)
Write a generator that yields cumulative sum of a list.
def accum_sum(lst):
    total_sum = 0
    for item in lst:
        total_sum += item
        yield total_sum

Q14 — Recursion (8 marks)
Write a function that counts how many 1s are in a nested list.
Example:
[1, [0, 1, [1]], 2] → 3
def count_ones(lst):
    count = 0
    for num in lst:
        if isinstance (num, list):
            count += count_ones(num)
        elif num == 1:
            count += 1
    return count

⭐ BONUS QUESTION (10 marks)
Q15 — Mixed Concept (TRICKY)
You are given:
def f(x): return x + 1
def g(x): return x * 2
def h(x): return x - 3
lst = [1,2]
Pipeline: apply f → g → h to each element.
What is the final output?  
when x= 1 f=2 g= 4 h = 1
when x= 2  f= 3 g= 6 h= 3
[1,3
]   
"""