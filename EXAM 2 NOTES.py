"""""
Problem 1: Linked List Insert at Head
Step 1: Understand the situation (visually)
You have: 10 → 20 → 30 → None
You want to insert 5 at the front:
5 → 10 → 20 → 30 → None
Step 2: Think (don’t code yet)
Ask yourself:
Where does 5 point? → 10
Who becomes the new head? → 5
That’s literally the whole idea.
Step 3: Fill in the blanks
I want YOU to complete this:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def insert_head(head, data):
    new_node = Node(data)
    # what should go here? - new_node.next = head
    return new_node
👉 What line connects the new node to the old list?

🧩 Problem 2: Stack (super easy pattern)
Think:
Stack = plate stack
push → add
pop → remove last
Fill this:
class Stack:
    def __init__(self):
        self.items = []
    def push(self, x):
        # what goes here? - self.items.append(x)
    def pop(self):
        # what goes here? - self.items.pop()

🧩 Problem 3: Queue
Think:
Queue = line of people
enqueue → join line
dequeue → first leaves
Fill this:
from collections import deque
q = deque()
# add 10 - q.append(10)
# add 20 - q.append(20)
# remove first element - q.popleft()

Reverse a Linked List
This is a VERY common exam question.
Given:
10 → 20 → 30 → None
Want:
30 → 20 → 10 → None
def reverse(head):
    prev = None
    current = head
    while current:
        next_temp = current.next
        current.next = prev      #  reverse the pointer
        prev = current           #  move prev forward
        current = next_temp      #  move current forward
    return prev

# Every link ends with none. At the end of reversal:prev = new head
Problem:
Check if a string is balanced:
"(()())" → True  
"(()" → False  
")(" → False
def is_balanced(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

def is_balanced(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in "({[":
            stack.append(char)
        else:
            if not stack:
                return False
            if stack[-1] ==  pairs[char]:
                stack.pop()
            else:
                return False
    return len(stack) == 0 
PART 1: TREES (visual first)
🧠 Think of this:
        A
       / \
      B   C
     / \
    D   E
🔑 Key terms (quick, don’t memorize hard)
Root = A
Children = B, C
Leaf = D, E, C
Height = longest path down

That’s enough for now.
🔥 MOST IMPORTANT: TREE TRAVERSALS
This is GUARANTEED exam content.

🧩 Problem 1
Tree:

        A
       / \
      B   C
     / \
    D   E

🧠 Pattern (super simple)
Inorder → left first
Preorder → root first
Postorder → root last

Correct answers: 
Inorder (Left, Root, Right)
Step:
Left subtree of A → (D, B, E)
Then A
Then C
👉 Answer: D B E A C

Preorder (Root, Left, Right)
👉 Answer: A B D E C

Postorder (Left, Right, Root)
👉 Answer: D E B C A

🧠 Pattern (LOCK THIS IN)
Type	Order
Inorder	Left → Root → Right
Preorder	Root → Left → Right
Postorder	Left → Right → Root

🚀 PART 2: BST (Binary Search Tree)
🧠 Rule: Left < Root < Right
🧩 Problem 2: Insert into BST
Start with:

      10
     /  \
    5    15
👉 Where does 12 go?

Think step-by-step:
Compare with 10
Then with 15

Answer like:
goes to ___ of ___
Step-by-step:
12 > 10 → go right
12 < 15 → go left
✅ Correct answer: goes to the LEFT of 15

🌲 PART 3: BST SEARCH (pattern)
Code idea:
def search(root, key):
    if not root:
        return False
    if root.data == key:
        return True
    elif key < root.data:
        return search(root.left, key)
    else:
        return search(root.right, key)

💡 Pattern: Go left if smaller, right if bigger

⚡ PART 4: GRAPH (quick intro)
We’ll keep this simple today.
🧠 BFS vs DFS
Algorithm	Uses	Behavior
BFS	Queue	level by level
DFS	Stack/recursion	go deep first
🧩 Example Graph
A — B — D
|   
C
👉 BFS from A:
👉 DFS from A:

(No strict single answer for DFS — just follow one path fully)
✅ BFS (Queue → level order) Answer: A B C D
Start at A:
Visit A
Then neighbors: B, C
Then D

✅ DFS (go deep first) One valid path: A B D C
(DFS can vary, but must include all nodes)

🧠 Why BFS vs DFS matters
BFS = explores level by level
DFS = explores one path fully

        10
       /  \
      5    15
     / \     \
    2   7     20

 Inorder (Left,root.right): 2, 5, 7, 10, 15, 20
 Preorder (Root, Left, Right): 10, 5, 2, 7, 15, 20
 Postorder (Left, Right, Root): 2, 7, 5, 20, 15, 10

BST Insert 6
Start at root 10 → 6 < 10 → go left
Node 5 → 6 > 5 → go right
Node 7 → 6 < 7 → go left
6 becomes left child of 7
🌟 Key Takeaways / Patterns for Trees
Inorder → sorted order for BST
Preorder → root first
Postorder → root last
BST insert → always compare → go left if smaller, right if bigger, repeat until leaf

CS 132 Exam-Ready Cheatsheet: Linked Lists, Stack, Queue, Trees, Graphs
1️⃣ Linked Lists
Node & LinkedList Skeleton
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head is None
Add to Front
def add(self, value):
    newNode = Node(value)
    if self.isEmpty():
        self.head = self.tail = newNode
    else:
        newNode.next = self.head
        self.head = newNode
Duplicate a Value
def duplicate(self, item):
    current = self.head
    while current:
        if current.value == item:
            new_node = Node(item)
            new_node.next = current.next
            current.next = new_node
            if current == self.tail:
                self.tail = new_node
            current = new_node.next
        else:
            current = current.next
Length
def __len__(self):
    count = 0
    current = self.head
    while current:
        count += 1
        current = current.next
    return count
Linked List Patterns
Always save current.next if modifying during iteration
Update head or tail if affected
Traversal: while current is not None: ...
2️⃣ Stacks
Push: stack.append(x)
Pop: stack.pop()
Peek: stack[-1]
Empty check: len(stack) == 0
Example: Balanced Parentheses
def is_balanced(s):
    stack = []
    pairs = {')':'(', '}':'{', ']':'['}
    
    for c in s:
        if c in '({[':
            stack.append(c)
        else:
            if not stack or stack[-1] != pairs[c]:
                return False
            stack.pop()
    return len(stack) == 0
3️⃣ Queues
FIFO: enqueue / dequeue
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []
Pattern: Use queue for BFS / level-order traversal
4️⃣ Binary Search Trees (BST)
Node & BST Skeleton
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
Insert
def insert(self, value):
    if self.root is None:
        self.root = Node(value)
    else:
        self._insert(self.root, value)

def _insert(self, node, value):
    if value < node.value:
        if node.left is None:
            node.left = Node(value)
        else:
            self._insert(node.left, value)
    else:
        if node.right is None:
            node.right = Node(value)
        else:
            self._insert(node.right, value)
Traversals
Type	Order	Pattern
Inorder	Left → Root → Right	BST → sorted order
Preorder	Root → Left → Right	Root first
Postorder	Left → Right → Root	Root last
Kth Smallest
Approach 1: Inorder → list → lst[k-1]
Approach 2: Traversal + counter → return once counter == k
5️⃣ Graphs
BFS (Queue)
def bfs(graph, start):
    Q = Queue()
    visited = []
    order = []
    Q.enqueue(start)
    visited.append(start)

    while not Q.isEmpty():
        node = Q.dequeue()
        order.append(node)
        for neighbor in sorted(graph[node]):
            if neighbor not in visited:
                visited.append(neighbor)
                Q.enqueue(neighbor)
    return order
BFS = level-order
DFS = stack / recursion → go deep first
Always include all nodes in output
⚡ Patterns to Remember (Exam Quick Hits)
Linked List: update head & tail, save current.next if inserting/deleting
Stack: top = stack[-1], pop when matched
Queue: FIFO → use for BFS
BST: Left < Node < Right, inorder = sorted, preorder/root first, postorder/root last
Graphs: BFS = queue, DFS = recursion/stack, always traverse all nodes

DAY 3: AVL TREES + MST (Exam-heavy topics)
AVL Trees (balanced BST)
Rotations (KEY)
Minimum Spanning Trees (MST)
🌲 PART 1: AVL TREES (Balanced Trees)
🧠 Idea: AVL = BST + balance condition
Balance Factor = height(left) - height(right)

✅ Rule: Each node must have:
-1 ≤ balance ≤ 1
🧩 Problem 1 (VERY IMPORTANT)
Insert in order:
10, 20, 30
Step-by-step:
After inserting:
10 → 20 → 30

Tree becomes:
10
  \
   20
     \
      30
❌ Problem:

Unbalanced (right heavy)
🔥 Fix = ROTATION
This is a Right-Right case → Left Rotation

✅ Result:
    20
   /  \
 10   30
🧠 Pattern (MEMORIZE THIS)
Case	Shape	Fix
Right-Right	right heavy	Left rotation
Left-Left	left heavy	Right rotation
Left-Right	zigzag	Left then Right
Right-Left	zigzag	Right then Left
🧩 Problem 2

Insert: 30, 20, 10 👉 What rotation is needed?

Answer like:
Case = Left-Left (LL)
Rotation = Right Rotation
🔄 Result after rotation:
    20
   /  \
 10   30
🔥 Quick memory trick:
Shape	Case	Fix
straight left	LL	Right rotation
straight right	RR	Left rotation
zig-zag left-right	LR	Left then Right
zig-zag right-left	RL	Right then Left

🔄 PART 2: ROTATION INTUITION
🧠 Left Rotation (RR case)

Before:

10
  \
   20
     \
      30

After:

    20
   /  \
 10   30
🧠 Right Rotation (LL case)

Before:

      30
     /
    20
   /
 10

After:

    20
   /  \
 10   30
🌐 PART 3: MINIMUM SPANNING TREE (MST)
🧠 Goal:

Connect all nodes with minimum total weight

🧩 Example Graph
A---B (1)
|   |
C---D (2)
1️⃣ Kruskal’s (easier)
Steps:
Sort edges by weight
Add smallest edge
Avoid cycles
🧩 Problem 3
Edges: A-B (1), B-C (2), A-C (3)
👉 Which edges are in MST? Use Kruskal’s:
Sort edges:
A-B (1), B-C (2), A-C (3)
Pick smallest edges without cycle:
Pick A-B (1) ✅
Pick B-C (2) ✅
Skip A-C (3) (would form cycle)
✅ Correct Answer: A-B and B-C
2️⃣ Prim’s (less likely coding, more concept)
Start from a node
Always pick smallest edge connected to tree

You’re almost there — FINAL LEVEL (exam style)
🧩 AVL Problem

Insert: 10, 30, 20
👉 Answer.
Case = Right-Left (RL) 
Rotation = Right rotation on 30, then Left rotation on 10

🧩 MST Problem
Edges: A-B (4), A-C (1), B-C (3), B-D (2)
👉 Which edges are chosen? A-C, B-D, B-C

"""""