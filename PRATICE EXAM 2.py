"""
Question:
Given: 1 → 2 → 3 → 4
👉 Insert 99 after 2
"""
def insert_after(self, target, value):
    current = self.head
    while current:
        if current.value == target:
            new_node = Node(value)
            new_node.next = current.next
            current.next = new_node
            return
        current = current.next

"""
Given: 1 → 2 → 3 → 4
👉 Delete node with value 3
"""
def delete(self, value):
    # Case: delete head
    if self.head and self.head.value == value:
        self.head = self.head.next
        return
    current = self.head
    while current and current.next:
        if current.next.value == value:
            current.next = current.next.next
            return
        current = current.next

"""
Operation -> Pattern
Insert	-> new.next = current.next then current.next = new
Delete	-> current.next = current.next.next
"""

"""
Given BST, write:
def search(self, key):
👉 Return True if found, False if not
"""
def search(self,key):
    def scan(node):
        if node is None:
            return False
        if key == node.value:
            return True
        elif key < node.value:
            return scan(node.left)
        else:
            return scan(node.right)
    return scan(self.root)

"""
BST search ALWAYS looks like this:
if node is None → not found  
if equal → found  
if smaller → go left  
if bigger → go right  
"""

"""
Write: def is_balanced(s):
👉 Return True if brackets are balanced
Example:
"([])" → True  
"([)]" → False  
""" 
def is_balanced(s):
    stack = []
    pairs = {')':'(', ']':'[', '}':'{'}
    
    for char in s:
        if char in '([{':
            stack.append(char)
        else:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    
    return len(stack) == 0

"""
🧠 Pattern to LOCK IN
opening → push  
closing → check top → pop  
"""
"""
Write: def range_sum(self, low, high):
👉 Sum values in BST between low and high
"""
def range_sum(self, low, high):
    def scan(node):
        if not node:
            return 0
        if node.value < low:
            return scan(node.right)
        if node.value > high:
            return scan(node.left)
        return node.value + scan(node.left) + scan(node.right)
    return scan(self.root)
"""
if node > high → ignore right → go left  
if node < low → ignore left → go right  
else → include node + left + right

if too small → go right  
if too big → go left  
else → include + both sides  
"""

"""
Write: def odd_even(self):
👉 Rearrange: 1 → 2 → 5 → 6 → 4 → 8
→
1 → 5 → 4 → 2 → 6 → 8
"""
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
"""
Pattern to LOCK IN (SUPER IMPORTANT)
odd jumps → even.next  
even jumps → odd.next  
connect odd to even_head at the end
"""
"""
def range_sum(self, low, high):
💡 Only remember:
too small → go right  
too big → go left  
else → include node
"""
def range_sum(self,low,high):
    def scan(node):
        if not node:
            return 0 
        if node.value < low:
            return scan(node.right)
        if node.value > high:
            return scan(node.left)
        return node.value + scan(node.right) + scan(node.left)
    return scan(self.root)

"""
Write:
def delete(self, value): (Remove node with value)
"""
def delete(self, value):
    # delete head
    if self.head and self.head.value == value:
        self.head = self.head.next
        return
    current = self.head
    while current and current.next:
        if current.next.value == value:
            current.next = current.next.next
            return
        current = current.next
"""
Write:
def is_balanced(s):
"""
def is_balanced(s):
    stack = []
    pairs = {')':'(', ']':'[', '}':'{'}
    for char in s:
        if char in '([{':
            stack.append(char)
        else:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    return len(stack) == 0

"""
🔹 Q1: Linked List (New Twist)
Write: def reverse_pairs(self):
👉 Swap every two adjacent nodes
Example: 1 → 2 → 3 → 4 → 5
→
2 → 1 → 4 → 3 → 5
"""
def reverse_pairs(self):
    dummy = Node(0)
    dummy.next = self.head
    prev = dummy
    while prev.next and prev.next.next:
        first = prev.next
        second = first.next
        prev.next = second
        first.next = second.next
        second.next = first
        prev = first
    self.head = dummy.next

""""
🔹 Q2: BST (Different from range_sum)
Write: def count_range(self, low, high):
👉 Return how many nodes have values in [low, high]
""" 
def count_range(self, low, high):
    def scan(node):
        if not node:
            return 0
        if node.value < low:
            return scan(node.right)
        if node.value > high:
            return scan(node.left)
        return 1 + scan(node.left) + scan(node.right)
    return scan(self.root)
""""
🔹 Q3: Stack (Different twist)
Write: def is_palindrome(s):
👉 Use a stack to check if string is palindrome
Example:
"madam" → True
"hello" → False
"""
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

""""
🔹 Q4: Linked List (Rotation twist)
Write: def rotate_left(self, k):
👉 Move first k nodes to the end
Example:
1 → 2 → 3 → 4 → 5, k=2
→
3 → 4 → 5 → 1 → 2
"""
def rotate_left(self, k):
    n = len(self)
    if n == 0 or n == 1:
        return self
    k = k % n
    if k == 0:
        return self
    current = self.head
    count = 1
    while count < k:
        current = current.next
        count += 1
    new_head = current.next
    current.next = None
    tail = new_head
    while tail.next:
        tail = tail.next
    tail.next = self.head
    self.head = new_head
    return self
      
"""
🔹 Q5: Graph (BFS logic)
Given adjacency list:
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}
Write: def bfs(graph, start):
👉 Return traversal order list
"""
def bfs(graph, start):
    queue = [start]
    visited = [start]
    order = []
    while queue:
        node = queue.pop(0)
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
    return order
""""
⭐ BONUS (HARD — but doable)
Write: def remove_k_digits(num, k):
👉 Return smallest number after removing k digits
Example: "1432219", k=3 → "1219"
"""
def remove_k_digits(num, k):
    stack = []
    for digit in num:
        while k > 0 and stack and digit < stack[-1]:
            stack.pop()
            k -= 1
        stack.append(digit)
    while k > 0:
        stack.pop()
        k -= 1
    result = ''.join(stack).lstrip('0')
    return result if result else "0"

"""
1.  Linked List delete
current.next = current.next.next

2. Linked List insert
new.next = current.next
current.next = new

3. BST recursion
if node < low → right
if node > high → left
else → include

4. Stack
push → pop → compare

5. BFS
queue → pop(0) → add neighbors

FINAL SIMPLIFIED SUMMARY
If you remember ONLY THIS:
🧩 Linked List
cut + reconnect  
or skip node  
🌳 BST
left smaller  
right bigger  
📚 Stack
push / pop / top
🌐 BFS
queue → visit → add neighbors
🔢 Remove digits
remove bigger before smaller
"""