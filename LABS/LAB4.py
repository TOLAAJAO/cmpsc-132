# LAB4
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

class Node:   # You are not allowed to modify this class
    def __init__(self, value=None):  
        self.next = None
        self.value = value
    
    def __str__(self):
        return f"Node({self.value})"

    __repr__ = __str__

class Malloc_Library:

    """
    ** This is NOT a comprehensive test sample, test beyond this doctest
        >>> lst = Malloc_Library()
        >>> lst
        <BLANKLINE>
        >>> lst.malloc(5)
        >>> lst
        None -> None -> None -> None -> None
        >>> lst[0] = 23
        >>> lst
        23 -> None -> None -> None -> None
        >>> lst[0]
        23
        >>> lst[1]
        >>> lst.realloc(1)
        >>> lst
        23
        >>> lst.calloc(5)
        >>> lst
        0 -> 0 -> 0 -> 0 -> 0
        >>> lst.calloc(10)
        >>> lst[3] = 5
        >>> lst[8] = 23
        >>> lst
        0 -> 0 -> 0 -> 5 -> 0 -> 0 -> 0 -> 0 -> 23 -> 0
        >>> lst.realloc(5)
        >>> lst
        0 -> 0 -> 0 -> 5 -> 0
        >>> other_lst = Malloc_Library()
        >>> other_lst.realloc(9)
        >>> other_lst[0] = 12
        >>> other_lst[5] = 56
        >>> other_lst[8] = 6925
        >>> other_lst[10] = 78
        Traceback (most recent call last):
            ...
        IndexError
        >>> other_lst.memcpy(2, lst, 0, 5)
        >>> lst
        None -> None -> None -> 56 -> None
        >>> other_lst
        12 -> None -> None -> None -> None -> 56 -> None -> None -> 6925
        >>> temp = lst.head.next.next
        >>> lst.free()
        >>> temp.next is None
        True
    """

    def __init__(self): # You are not allowed to modify the constructor
        self.head = None
    
    def __repr__(self):  # You are not allowed to modify this method
        current = self.head
        out = []
        while current != None:
            out.append(str(current.value))
            current = current.next
        return " -> ".join(out)

    __str__ = __repr__
    
    def __len__(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count 
    
    def __setitem__(self, pos, value):
       if pos < 0:
           raise IndexError
       current = self.head
       index = 0
       while current is not None and index < pos:
           current = current.next
           index += 1
       if current is None: 
           raise IndexError
       current.value = value

    def __getitem__(self, pos):
        if pos < 0: 
            raise IndexError
        current = self.head
        index = 0
        while current is not None and index < pos:
            current = current.next
            index += 1
        if current is None:
            raise IndexError
        return current.value
    
    def malloc(self, size):
        self.free()
        if size <= 0:
            return 
        self.head = Node(None)
        current = self.head
        count = 1
        while count < size:
            current.next = Node(None)
            current = current.next
            count += 1

    def calloc(self, size):
        self.free()
        if size <= 0:
            return 
        self.head = Node(0)
        current = self.head
        count = 1
        while count < size:
            current.next = Node(0)
            current = current.next
            count += 1

    def free(self):
        current = self.head
        while current is not None: 
            nxt = current.next
            current.next = None
            current = nxt
        self.head = None 

    def realloc(self, size):
        if size == 0:
            self.free()
            return 
        if self.head is None:
            self.malloc(size)
            return 
        length = len(self)
        if size == length:
            return 
        if size > length:
            current = self.head
            while current.next is not None:
                current = current.next 
            count = length 
            while count < size : 
                current.next = Node(None)
                current = current.next
                count += 1
        else:
            current = self.head
            index = 1
            while index < size:
                current = current.next 
                index += 1
            temp = current.next 
            current.next = None
            while temp is not None:
                nxt = temp.next
                temp.next = None
                temp = nxt

    def memcpy(self, ptr1_start_idx, pointer_2, ptr2_start_idx, size):
       if self.head is None or pointer_2.head is None:
           return 
       src = self.head
       index = 0
       while src is not None and index < ptr1_start_idx: 
           src = src.next 
           index += 1
       dst = pointer_2.head
       index = 0
       while dst is not None and index < ptr2_start_idx:
           dst = dst.next
           index += 1
       if src is None or dst is None: 
           return 
       count = 0
       while src is not None and dst is not None and count < size:
           dst.value = src.value 
           src = src.next
           dst = dst.next
           count += 1
    

def run_tests():
    import doctest
    doctest.testmod(verbose=True)
     

if __name__ == "__main__":
     run_tests()