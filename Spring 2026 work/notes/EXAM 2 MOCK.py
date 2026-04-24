"""
EXAM REVIEW 
1. Implement a function odd_even(self), which rearranges the linked list by node
position: first all odd digits, then all even digits, preserving relative order.
Example:
>>>lst
1 -> 2 -> 5 -> 6 -> 4 -> 8
>>>lst.odd_even()
>>>lst
1 -> 5 -> 4 -> 2 -> 6 -> 8
SOLUTION: 
Link: 1 ->2 -> 5 -> 6 -> 4 > 8
odd = 1, 5, 4
even = 2, 6, 8
Initial: 1 ->2 -> 5 -> 6 -> 4 > 8
        ↑ ↑
        o e
Step 1: 1 ->2 ->5 ->6 ->4 ->8
                ↑ ↑
                o e
Step 2: 1 ->2 ->5 ->6 ->4 ->8
                        ↑ ↑
                        o e
Final:
odd link: 1 -> 5 -> 4
even link: 2 -> 6 -> 8
connect together: 1 ->5 ->4 ->2 ->6 ->8
Code:
def odd_even(self):
if not self.head or not self.head.next:
return
odd = self.head
even = self.head.next
even_head = even
while even and even.next:
odd.next = even.next
odd = odd.next
even.next = odd.next
even = even.next
odd.next = even_head

2. Implement range_sum(self, low, high) to return the sum of all keys in the closed
interval [low, high].
Example:
>>> tree
8
/ \
3 10
/ \ \
1 6 14
/ \ /
4 7 13
>>>tree.range_sum(5, 13)
44
SOLUTION
Key: For any node, if node.value >= low, and node.value =< high, sum = node.value +
sum(node.right) + sum(node.left)
Access path:
1: (8)
/ \
2: (3) 5: (10)
/ \ \
1 3: (6) 14
/ \ /
4 4: (7)6: (13)
Code:
def range_sum(self, low, high):
def scan(node):
if not node: return 0
if node.key > high: return scan(node.left)
if node.key < low: return scan(node.right)
return node.key + scan(node.right) + scan(node.left)
return scan(self.root)

3. Implement detect_cycle(self) to loop detection and return to the loop entry point.
Example: >>>lst :1-> 2-> 3-> 4
>>> lst.detect_cycle() : 2
>>>lst: 1 -> 2 -> 3 -> 4
>>> lst.detect_cycle(): None
SOLUTION
Key: if there is a loop, one fast could catch one slow.
1-> 2-> 3-> 4
fast: 1 slow: 1
fast: 3 slow: 2
fast: 2 slow: 3
fast: 4 slow: 4
Key: find the entry requires a math function.
a: Distance from the beginning (1) to the entry (2) 1 -> 2
b: Distance from the entry (2) to the meeting point (4) on the loop 2-> 3-> 4
c: Length of one loop 2 ->3 ->4
For the slow pointer, it walks a + b. For the fast pointer, it walks a + b + c
We want to find a, so we can continue on meeting point (4), to walk c – b, and now we walk a + b + c – b = a + c or 
a + b + c + c – b = a + 2 * c. C is the loop length, so it won’t affect. Because fast pointer is twice faster than slow pointer,
2 * (a + b) = a + b + c. Thus, a + b = c -> a = c – b.
We can start from the head (1) and meeting point (4) again, and walk a or c – b steps together,once them meet, the location is entry.
Code:
def detect_cycle_entry(self):
if not self.head or not self.head.next:
return None
slow = fast = self.head
while fast and fast.next:
slow = slow.next
fast = fast.next.next
if slow is fast:
break
else:
return None
ptr = self.head
while ptr is not slow:
ptr = ptr.next
slow = slow.next
return ptr

4. Write the Python code to implement the function `rotate_right(linked_list, k)`. This method will rotate the linked list to the 
right by `k` places. `k` will always be a non-negative integer. The method should only modify the original list and must correctly 
update the head and tail pointers. Note: `k` can be larger than the length of the list.
Example:
Head:Node(1)
Tail:Node(5)
List: 1 -> 2 -> 3 -> 4 -> 5
>>> x_rot = rotate_right(x, 2)
>>> x_rot
Head:Node(4)
Tail:Node(3)
List: 4 -> 5 -> 1 -> 2 -> 3
>>> x_rot = rotate_right(x, 6)
>>> x_rot
Head:Node(5)
Tail:Node(4)
List: 5 -> 1 -> 2 -> 3 -> 4
SOLUTION
def rotate_right(linked_list, k):
n = len(linked_list)
if n in [0, 1]:
return linked_list
k = k % n
if k == 0:
return linked_list
curr = linked_list.head
prev = None
i = 0
while i < n - k:
prev = curr
curr = curr.next
i += 1
prev.next = None
linked_list.tail.next = linked_list.head
linked_list.head = curr
linked_list.tail = prev
return linked_list

5. Write a function `is_palindrome(s)` that returns `True` if the string `s` is a
palindrome, and `False` otherwise. You must use a Stack to solve this. (A palindrome reads
the same forwards and backwards, like "racecar").
Example:
>>> is_palindrome("racecar")
True
>>> is_palindrome("hello")
False
>>> is_palindrome("madam")
True
>>> is_palindrome("noon")
True
SOLUTION 
def is_palindrome(s):
first_half = Stack()
n = len(s)
mid = n // 2
i = 0
while i < n:
if i < mid:
first_half.push(s[i])
i += 1
elif i == mid and n % 2 == 1:
i += 1
else:
char = first_half.pop()
if s[i] != char:
return False
i += 1
return first_half.isEmpty()

BONUS QUESTION: Write a Python function `remove_k_digits(num, k)` that takes a string `num`
(representing a non-negative integer) and an integer `k` (the number of digits to remove).
The function should return a string representing the smallest possible integer that can be
formed by removing exactly `k` digits from num.
Notes:
* The output string must not contain any leading zeros, unless the number itself is `0`.
* If removing `k` digits results in an empty string, your function must return "0".
Example:
>>> remove_k_digits("1432219", 3)
"1219"
>>> remove_k_digits("40500", 1)
"500"
"123"
"0"
>>> remove_k_digits("12345", 2)
>>> remove_k_digits("32", 2)
SOLUTION
def remove_k_digits(num, k):
stack = Stack()
for char in num:
while k > 0 and not stack.isEmpty() and char < stack.peek():
stack.pop()
k -= 1
stack.push(char)
while k > 0 and not stack.isEmpty():
stack.pop()
k -= 1
result = repr(stack)
result = result.lstrip("0")
if not result:
return "0"
return result

ADDITIONAL REVIEW:
1. Given a singly linked list, write a method reverse_pairs(self) in the LinkedList class that swaps every two adjacent nodes. 
If the linked list has an odd number of nodes, the last node should remain unchanged. The swapping should be performed in-
place without creating any additional nodes.
For example, given the linked list: 1 -> 2 -> 3 -> 4 -> 5
The output should be: 2 -> 1 -> 4 -> 3 -> 5
SOLUTION
dummy (prev)
0 -> 1 -> 2 -> 3 -> 4 -> 5
↑ ↑
first second
head
Swapping Steps:
· prev.next = second → dummy now points to node 2.
· first.next = second.next → node 1 now points to node 3.
· second.next = first → node 2 now points to node 1.
dummy (prev)
0 -> 2 -> 1 -> 3 -> 4 -> 5
· Update prev: Set prev = first (node 1).
· Update Head: the head of the modified list is dummy.next, which
points to node 2.
Code:
def reverse_pairs(self):
# Create a dummy node to simplify head operations.
dummy = Node(0)
dummy.next = self.head
prev = dummy
# Loop while there are at least two nodes to swap.
while prev.next and prev.next.next:
first = prev.next # Node 1 in the pair.
second = first.next # Node 2 in the pair.
# Swapping pointers:
prev.next = second # 1. Link prev to second.
first.next = second.next # 2. Link first to node after second.
second.next = first # 3. Link second to first.
# Move prev to the end of the swapped pair.
prev = first
# Update head in case it was swapped
self.head = dummy.next

Question - 2:
Write the Python code for a method get_pred(self, key) that returns the in-order predecessor of the node with the given value in a 
Binary Search Tree (BST). The predecessor of a node is the node with the next lower value in the tree when traversed in-order. For
example, if the in-order traversal of a tree is 1, 3, 4, 6, 7, 8, 10, the predecessor of 7 is 6. If the node has no predecessor
(it's the smallest element), the method should return None.
SOLUTION
Case 1: Node Has a Left Subtree
When the target node (say, N) has a left child, its in‑order predecessor is the rightmost node in its left subtree.
In‑order Traversal: 4, 5, 6, 7, 8, 10
Case 2: Node Does Not Have a Left Subtree
If the target node (say, N) does not have a left subtree, you must start from the root and traverse down, keeping track of the last
node that is less than N.
Code:
def get_pred(self, key):
# First, find the node with the given key.
node = self._find(self.root, key)
if node is None:
return None # key not found
# Case 1: Node has a left subtree.
if node.left:
pred = node.left
while pred.right:
pred = pred.right
return pred
# Case 2: Node has no left subtree.
predecessor = None
current = self.root
while current:
if key > current.value:
predecessor = current
current = current.right
elif key < current.value:
current = current.left
else:
break # key found
return predecessor

Question - 3:
Write the function lvm(string) that takes a string containing mixed brackets: '(', ')', '[', ']', '{', and '}'. It returns the length
of the longest valid (well-formed) substring, where the brackets are correctly matched and properly nested.
For example:
>>> lvm("({[()]})") 8 # entire string is valid
>>> lvm("([)]") 0 # the brackets are not properly nested
>>> lvm("{[()]}[") 6 # "{[()]}" is valid, "[" at the end is unmatched
>>> lvm("](){[()()]}") 10 # "(){[()()]" is valid
>>> lvm("}{") 0 # invalid order
SOLUTION 
def Ivm(string):
stack = Stack()
max_len = 0
last_invalid = -1 # Index before the start of a potential valid substring
matching = (): (, T: T, J:C
for i, ch in enumerate(string):
if ch in "(K:
stack.push((i, ch))
elif ch in ")Il:
if not stack.isEmpty():
top_i, top_ch = stack.peek()
if top_ch == matching[ch]:
stack.pop()
if not stack.isEmpty():
max_len = maxmax_len, i - stack.peek([O])
else:
max_len = maxmax_len, i - last_invalid)
else:
# Mismatched closing
last_invalid = i
# Clear stack since nesting is broken
while not stack.isEmpty():
stack.pop()
else:
last invalid = il
return max len


Question - 4:
Write the method rotate(self, k) that takes an integer k and moves the first k elements of the queue to the back, preserving their
order.
For example, given the queue: 1 -> 2 -> 3 -> 4 -> 5 and k = 2 The output should be:
3 -> 4 -> 5 -> 1 -> 2
You may assume that:
· k is a valid integer such that 0 <= k <= number of elements in the queue.
· The queue has at least k elements.
SOLUTION
def rotate(self, k):
#Traverse to the k-th node
current = self.head
count = 1
while count < k and current:
current = current.next
count += 1
if not current or not current.next:
return # Nothing to rotate
# Break the list at k-th node
new_head = current.next
current.next = None # Break at k-th node
old_tail = self.tail
# Attach old head to tail
old tail.next = self. head
# Update head and tail
self.head = new_head
self.tail = current

Question - 5:
Write the method get_kth_leaf(self, k) for the MaxHeap class. This method returns the kth largest leaf node value in the heap. If 
there are fewer than k leaf nodes, return None.
Assumptions for this question:
● The heap is a Max Heap where all elements are distinct integers.
● The heap is implemented as a complete binary tree.
● The heap has at least one element.
● The value k is a valid positive integer (i.e., k >= 1).
SOLUTION
Example
Python Code:
>>> heap = MaxHeap()
>>> heap.insert(40)
>>> heap.insert(35)
>>> heap.insert(30)
>>> heap.insert(20)
>>> heap.insert(25)
>>> heap.insert(10)
>>> heap.insert(5)
>>> heap.get
kth _ _ leaf(1) - 10
>>> heap.get
kth_ _leaf(3)- 5
>>> heap.get
None
kth __ leaf(4)
Explanation of Example:
zzThe MaxHeap would look like this (level-order):
40
/ \
35 30
/ \ / \
20 25 10 5
Leaf nodes are: 20, 25, 10, 5
Sorted in descending order: 25, 20, 10, 5
get_kth_leaf(1) → 25
get_kth_leaf(3) → 10
get_kth_leaf(4) → 5
get_kth_leaf(5) → None
implementation of get kth leaf in def get_kth_leaf (self, k) :
def is_leaf (index) :
left = 2 * index + 1
right = 2 * index + 2
return left >= len (self.heap) and right >= len(self.heap)
leaves = []
for i in range(len(self.heap)):
if is_leaf (i):
leaves. append (self heap[i])
leaves. sort(reverse=True)
if k <= len(leaves) :
return leaves [k - 1]
return None

MOCK EXAM 1 (Practice)
🔹 Q1: Linked List (Tracing)

Given this linked list:

10 → 20 → 30 → 40
Code:
current = head
while current is not None:
    if current.value == 20:
        new_node = Node(25)
        new_node.next = current.next
        current.next = new_node
        current = current.next
    current = current.next
❓ Question:
What is the final linked list? - 10 → 20 → 25 → 30 → 40

🔹 Q2: Stack (Output + Logic)
stack = []
stack.append(5)
stack.append(10)
stack.append(15)

stack.pop()
stack.append(20)
stack.pop()
❓ Question:
What is the final stack? - [5, 10]
What does stack[-1] return? - 10

🔹 Q3: Balanced Parentheses
Is the following string balanced?
({[]})()
Answer: True or False - True

🔹 Q4: BST Traversal

Given this BST:

        15
       /  \
      10   20
     / \     \
    5  12     25
❓ Questions:
Inorder traversal (Left → Root → Right):- 5, 10, 12, 15, 20, 25 
Preorder traversal (Root → Left → Right):- 15, 10, 5, 12, 20, 25
Postorder traversal (Left → Right → Root) - 5, 12, 10, 25, 20, 15

🔹 Q5: BST Insert
Insert:
into this tree:

        10
       /  \
      5    15
❓ Question:
Draw or describe the final tree. right of 5
        10
       /  \
      5    15
       \
        8

🔹 Q6: Graph BFS
Graph (adjacency list):
A: B, C
B: D
C: D
D: E
E: 
❓ Question:
What is the BFS traversal starting from A? - A, B, C, D, E

🔹 Q7: Graph DFS
Using the same graph:
A: B, C
B: D
C: D
D: E
E: 
❓ Question:
Give one valid DFS traversal starting from A. - A, B, C, D, E

🔹 Q8: AVL Rotation
Insert in order: 30, 40, 50
❓ Questions:
What type of imbalance occurs?-  Straight right
What rotation is needed?- Left rotation

🔹 Q9: MST (Kruskal)
Edges:
A-B (3)
A-C (1)
B-C (2)
C-D (4)
❓ Question:
Which edges are selected in the MST? - A-C, B-C, C-D
Why C–D was chosen
Even though it’s weight 4: It’s the only way to connect D, Without it, the graph is not fully connected
👉 MST must connect ALL nodes
🔥 One-line summary: MST = minimum weight + all nodes connected + no cycles

🔹 Q10: Concept Question
❓ What is the difference between:
BFS
DFS
(Just 1–2 sentences)
BFS uses a queue and explores level by level
DFS uses a stack or recursion and goes deep first
"""