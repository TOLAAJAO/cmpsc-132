# QUIZ ONE REVIEW 

"""""
Question 1: Find the Student Who Scored the Highest in Each Subject. Given a dictionary grades, where each key represents a student's 
name, and the value is  another dictionary containing their scores in three subjects: Math, Science, and English. 
Write a function find_top_students(grades) that: 
1. Finds the student who scored the highest in each subject (Math, Science, and English). 
2. Returns a dictionary where each subject is mapped to the name of the student who 
achieved the highest score. 
#Result should be 
# { 'Math': 'Bob',   'Science': 'Bob',   'English': 'Alice'  } 
"""""
def find_top_students(grades): 
    top_student = {"Math":"", "Science":"", "English": ""}
    highest_scores = { "Math": 0 , "Science": 0, 'English': 0}
    for student, subjects in grades.items():
        for subject , score in subjects.items():
            if score > highest_scores[subject]:
                highest_scores[subject]= score
                top_student[subject] = student
    return top_student
# Test Cases 
grades = { "Alice": {'Math': 90, 'Science': 85, 'English': 95}, "Bob": {'Math': 92, 'Science': 88, 'English': 95}, 
"Charlie": {'Math': 70, 'Science': 75, 'English': 80}, 
"David": {'Math': 88, 'Science': 85, 'English': 91} } 
result = find_top_students(grades) 
print(result) 

'''
Question 2: Debugging - Find the Largest Number in a List 
The following function is supposed to find the largest number in a given list. However, it  does not return the correct result in all
 cases, particularly when the list contains negative numbers. 
def find_largest(numbers): 
    largest = 0 
    for num in numbers: 
        if num > largest: 
            largest = num 
    return largest 
#Test Case 
print(find_largest([-5, -1, -10, -3])) 
#Output: 0   
# Expected Output: -1 
'''
def find_largest(numbers): 
    if not numbers:
        return None
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num 
    return largest 

'''
Question 3: Multi-Level Inheritance - Fill in the Blanks 
You are given a class hierarchy for employees in a company. Complete the missing lines to: 
• Assign salaries correctly. 
• Ensure correct inheritance (Manager from Employee, Executive from Manager). 
• Override methods correctly. 
'''
# Incomplete Code: 
class Employee: 
    def __init__(self, name, salary): 
        self.name = name 
        self.salary = salary  # (1) Fill in the missing line 
 
    def calculate_bonus(self): 
        return self.salary * 0.05  # (2) Fill in the missing line (calculate 5% bonus) 
 
class Manager(Employee):  # (3) Fill in the missing line (inheritance) 
    def __init__(self, name, salary, department): 
        super().__init__(name, salary)  # (4) Fill in the missing line (call parent 
        self.department = department 
 
    def calculate_bonus(self):  # Override the method 
        return self.salary * 0.10  # (5) Fill in the missing line (10% bonus for 
 
class Executive(Manager):  # (6) Fill in the missing line (inheritance) 
    def __init__(self, name, salary, department, stock_options): 
        super().__init__(name, salary, department)  # (7) Fill in the missing line (call Manager 
        self.stock_options = stock_options 
 
    def calculate_bonus(self):  # Override the method 
        return self.salary * 0.15  # (8) Fill in the missing line (calculate 15% bonus for 
# Test Cases 
emp = Employee("Bob", 50000) 
mgr = Manager("Alice", 70000, "Sales") 
exec1 = Executive("Charlie", 100000, "Finance", 500) 
print(emp.calculate_bonus()) # Expected Output: 2500.0 
print(mgr.calculate_bonus()) # Expected Output: 7000.0 
print(exec1.calculate_bonus()) # Expected Output: 15000.0 
print(exec1.stock_options) # Expected Output: 500 

'''''
Fill in the Blanks 
1. Assign the salary parameter correctly in init. 
2. Calculate the 5% bonus for employees. 
3. Ensure Manager inherits from Employee. 
4. Call the parent class constructor correctly in Manager . 
5. Implement the overridden calculate_bonus() method for Manager (10%) 
6. Ensure Executive inherits from Manager. 
7. Call the parent class constructor correctly in Executive 
8. Implement the overridden calculate_bonus() method for Executive (15%) 
 
'''

"""
Question 4: Dictionary Comprehension - Fill in the Blanks 
You are given a dictionary of temperatures in Celsius. Complete the function to: 
• Convert them to Fahrenheit using the formula: 
F = (C x 9/5) + 32 
• Ensure correct iteration over dictionary items. 
"""
# Incomplete Code: 
# Question 4 
def celsius_to_fahrenheit(temps): 
    converted_temps = {city: (temp * 9/5) + 32 for city, temp in temps.items()} 
    return converted_temps  
# Test Cases 
city_temps = {"New York": 0, "Los Angeles": 20, "Chicago": -5} 
print(celsius_to_fahrenheit(city_temps)) 
#Expected Output: {'New York': 32.0, 'Los Angeles': 68.0, 'Chicago': 23.0} 

"""
Fill in the Blanks 
1. Ensure correct iteration over dictionary items. 
2. Apply the correct Celsius to Fahrenheit formula: F = (C \times 9/5) + 32 
3. Map keys correctly in dictionary comprehension 
"""

"""
Question 5: Given an array of integers arr and a target sum S, determine if there is a subset 
of the array that adds up exactly to S. 
Input: arr = [3, 34, 4, 12, 5, 2], S = 9 
Output: True (because 4 + 5 = 9) 
"""
def is_subset_sum(arr, n, s):
    if s == 0:
        return True
    if n == 0:
        return False
    if arr[n-1] > s:
        return is_subset_sum(arr, n-1, s)
    else: 
        return (is_subset_sum(arr, n-1, s) or is_subset_sum(arr, n-1, s - arr[n-1]))
arr = [3, 34, 4, 12, 5, 2]
s = 9
n = len(arr)
print(is_subset_sum(arr, n, s))

""""
 Question 6: 
Write a Python function read_file_lines() that asks the user to enter the name of a text file. 
The function should: 
1. Try to open the file for reading. 
2. If the file does not exist, catch the FileNotFoundError exception and print: "Error: File 
not found." 
3. Read all lines of the file and ask the user to input an index number to print a specific 
line. 
4. If the user enters an index that is out of range, catch the IndexError exception and 
print: "Error: Index out of range." 
5. Handle any other unexpected errors with a generic message: "Unexpected error 
occurred." 
6. After each attempt, print "Operation completed." 
The function should stop if the user enters "quit" instead of a file name. 
"""
def read_file_lines():
    file_name = ""
    while file_name.lower() != "quit":
        file_name = input("Enter file name (or 'quit' to exit): ")
        if file_name.lower() != "quit":
            try:
                with open(file_name, "r") as f: 
                    lines = f.readlines()
                index_input = input("Enter line index to read")
                index = int(index_input)
                print(f"Line {index}: {lines[index].strip()}")
            except FileExistsError:
                print("Error: File not found.")
            except IndexError:
                print("Error: Index out of range.")
            except Exception: 
                print("Unexpected error occurred.")
            print ("Operation completed. \n")
    print ("Existing program.")

"""
Question 7: A coffee shop wants to update their customer points. You are given a dictionary of existing
customers and a list of new transactions.
• If the customer exists, add the new points to their total.
• If the customer is new, add them to the dictionary with their initial points.
• Important: You must return a new dictionary and not change the original one.
Example:
>>> current_members = {'Alice': 50, 'Bob': 20}
>>> transactions = {'Alice': 10, 'Charlie': 15}
>>> update_loyalty(current_members, transactions)
# Output: {'Alice': 60, 'Bob': 20, 'Charlie': 15}
"""
def update_loyalty(current_members, transactions):
    updated = {}
    for name in current_members:
        updated[name] = current_members[name]
    for name in transactions:
        if name in updated:
            updated[name] = updated[name] + transactions[name]
        else:
            updated[name] = transactions[name]
    return updated

"""
Question 8: Create a SmartLight class that uses Encapsulation to protect its brightness level.
• Initialize the class with a private variable brightness set to 100.
• Create a property method to read the brightness.
• Create a setter method that only updates the brightness if the value is between 0 and
100.
Example:
>>> my_light = SmartLight()
>>> my_light.brightness = 150 # Should not change (out of range)
>>> print(my_light.brightness)
100
>>> my_light.brightness = 50 # Should update
>>> print(my_light.brightness)
50
"""
class SmartLight: 
    def __init__(self):
        self._brightness = 100
    
    @property
    def brightness(self):
        return self._brightness
    @brightness.setter
    def brightness(self,value):
        if value >= 0 and value <= 100:
            self._brightness = value
        else: 
            print("Error: Value must be between 0 and 100")

"""
Question 9: Model a security system using Inheritance.
• Start with a base class BasicVault that has a lock() method printing "Vault is locked".
• Create a subclass BiometricVault that overrides the lock() method to print "Vault is
locked with Fingerprint".
• Use super() in the subclass constructor to set an owner name from the parent class.
Example:
>>> v1 = BasicVault("User1")
>>> v1.lock()
Vault is locked
>>> v2 = BiometricVault("User2")
>>> v2.lock()
Vault is locked with Fingerprint
"""
class BasicVault:
    def __init__(self,owner):
        self.owner = owner
    
    def lock(self):
        print("Vault is locked")

class BiometricVault(BasicVault):
    def __init__(self, owner):
        super().__init__(owner)
    
    def lock(self):
        print("Vault is locked with FingerPrint")

"""
Question 10: Write a function clean_data(input_list) that converts a list of strings into integers.
• Use a try-except block to handle cases where a string cannot be converted to a number
(e.g., "abc").
• Catch the ValueError specifically and append None to the result list instead of crashing.
• Use a finally block to print "Cleaning session finished".
Example:
>>> data = ["10", "20", "hello", "40"]
>>> clean_data(data)
Error: Could not convert 'hello'
Cleaning session finished
# Result: [10, 20, None, 40]
"""
def clean_data(input_list):
    cleaned = []
    try:
        for item in input_list:
            try:
                cleaned.append(int(item))
            except ValueError:
                print(f"Error: Could not convert '{item}'")
                cleaned.append(None)
    finally:
        print("Cleaning session finished")
    return cleaned

"""
Question 11: Write a function organize_by_score that takes a dictionary where keys are student names and
values are their scores.
• Return a new dictionary where the keys are "Pass" (score >= 70) and "Fail" (score <
70).
• The values should be lists of the names of students in that category.
Example:
>>> scores = {'Alice': 85, 'Bob': 60, 'Charlie': 92}
>>> organize_by_score(scores)
# Output: {'Pass': ['Alice', 'Charlie'], 'Fail': ['Bob']}
"""    
def organize_by_score(scores):
    organized = {"Pass": [], "Fail": []}
    for name in scores:
        if scores[name] >= 70:
            organized["Pass"].append(name)
        else:
            organized["Fail"].append(name)
    return organized

# CHAT GPT QUESTIONS
"""
Question 1 — Nested Dictionary (Like Top Students) Write a function: def find_lowest_students(grades)
Return student with lowest score in each subject.
Example Output:
{ 'Math': 'Charlie',
 'Science': 'Charlie',
 'English': 'Charlie'}
"""
def find_lowest_students(grades):
    lowest_students = {"Math":"", "Science":"","English":""}
    lowest_score = {"Math": 100, "Science": 100, "English": 100}
    for student, subjects in grades.items():
        for subject, score in subjects.items():
            if score < lowest_score[subject]:
                lowest_score[subject] = score
                lowest_students[subject] = student
    return lowest_students

"""
Write function: def find_smallest(numbers): if list empty return None
"""
def find_smallest(numbers):
    if not numbers:
        return None
    smallest = numbers[0]
    for num in numbers:
        if num < smallest: 
            smallest = num
    return smallest 

"""
 Question 3 — OOP Inheritance Practice
Make classes:
Base Class
Vehicle
attributes: brand, price
method: get_tax() → 5% of price

Subclass
ElectricCar inherits Vehicle
extra attribute: battery_range
override get_tax() → 2% of price
"""
class Vechicle:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    def get_tax(self): 
        return self.price * 0.05
    
class ElectricCar(Vechicle):
    def __init__(self, brand, price,battery_range):
        super().__init__(brand, price)
        self.battery_range = battery_range
    def get_tax(self):
        return self.price * 0.02

""""
 Question 4 — Dictionary Comprehension
Convert dictionary of miles → kilometers.
Formula:
km = miles * 1.6
Input:
{"TripA": 10, "TripB": 25}
"""
def miles_to_kilometers(trips):
    return {trip: miles * 1.6 for trip, miles in trips.items()}

""""
Question 5 — Recursion Thinking
Write recursive function: Return True if list contains a subset summing to target.
Use pattern from subset sum but write from memory.
"""
def subset_sum(arr, n, target):
    if target == 0:
        return True
    if n == 0:
        return False
    if arr[n-1] > target:
        return subset_sum(arr, n-1, target)
    else:
        return (subset_sum(arr, n-1, target) or subset_sum(arr, n-1, target- arr[n-1]))

""""
Question 6 — Exception Handling Practice
Write function: read_first_line()
Steps:
Ask filename
Try to open
Print first line
Handle:
FileNotFoundError
Any other error
Always print:
Done
"""
def read_first_line():
    filename = input("Enter file name:")
    try:
        with open(filename, "r") as f:
            print(f.readline())
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception:
        print("Unexpected error occured.")
    finally:
        print("Done")

"""
Question 1 — Nested Dictionary Logic (15 pts) Write a function:
def find_subject_averages(grades):
Given: grades = { "Alice": {"Math": 90, "Science": 80, "English": 100},"Bob": {"Math": 70, "Science": 85, "English": 90},
"Charlie": {"Math": 80, "Science": 75, "English": 95}} eturn dictionary with average score per subject:
Expected:
{"Math": average_math, "Science": average_science, "English": average_english }
"""
def find_subject_averages(grades):
    totals = {'Math': 0, "Science": 0, "English": 0}
    count = len(grades)
    for student, subjects in grades.items():
        for subject, score in subjects.items():
            totals[subject] += score
    averages = {}
    for subject in totals:
        averages[subject]= totals[subject]/ count
    return averages

""""
Question 2 — Debug + Edge Cases (10 pts) Write:
def second_largest(numbers):
Rules:
Return second largest number
If list has < 2 numbers → return None
Must work with negative numbers
"""
def second_largest(numbers):
    if len(numbers) < 2:
        return None
    unique_nums = list(set(numbers))
    unique_nums.sort(reverse= True)
    if len(unique_nums) < 2:
        return None
    return unique_nums[1]

"""""
Question 3 — OOP Inheritance + Override (15 pts)
Create:
Base Class
class Employee
attributes: name, salary
method: yearly_bonus() → 4% salary

Subclass
class Developer inherits Employee
extra attribute: programming_language
override yearly_bonus() → 6% salary
Must use:
super().__init__()
"""
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def yearly_bonus(self):
        return self.salary * 0.04
    
class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language
    def yearly_bonus(self):
       return self.salary * 0.06

""""
Question 4 — Dictionary Comprehension (10 pts) Write function converting USD → EUR
Formula: eur = usd * 0.9
Input:
{"ItemA": 100, "ItemB": 50}
Return converted dictionary.
"""
def usd_to_eur(items):
    return {item: usd * 0.9 for item, usd in items.items()}

""""
 Question 5 — Recursion (Subset Style) (20 pts) Write recursive function:
def can_make_sum(arr, n, target):
Return True if subset equals target.
Must include:
Base case target == 0
Base case n == 0
"""
def can_make_sum(arr,n, target): 
    if target == 0:
        return True
    if n == 0:
        return False
    if arr[n-1] > target:
        return can_make_sum(arr, n-1, target)
    else:
        return (can_make_sum(arr, n-1, target) or can_make_sum(arr, n-1, target - arr[n-1]))

""""
 Question 6 — File + Exception Handling (20 pts) Write function:
def read_line_number():
Requirements:
Ask filename
Ask line number
Print that line
Handle:
FileNotFoundError
IndexError
Any other Exception
Always print:
Operation finished
"""
def read_line_number():
    filename = input("Enter file name: ")
    line_number = int(input("Enter line number: "))
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
            print(lines[line_number].strip())
    except FileNotFoundError:
        print("Error: File not found.")
    except IndexError:
        print("Error: Index out of range")
    except Exception:
        print('Unexpected Error ocuured.')
    finally: 
        print("Operation finished")

"""""
 Question 7 — Encapsulation (10 pts)
Create class:
class BankAccount
Rules:
Private balance starts at 0
Property getter → balance
Setter → only allow deposit if amount > 0
"""
class BankAccount:
    def __init__(self):
        self._balance = 0
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self, amount):
        if amount > 0:
            self._balance += amount

"""
Mock Question A — Inventory Update (Like Loyalty Points). A game store tracks items and stock levels.
• If item exists → add new stock
• If item new → add it
• Must return NEW dictionary (don’t modify original)
Example:
inventory = {"PS5": 5, "Xbox": 3}
shipment = {"PS5": 2, "Switch": 4}
Output:
{"PS5": 7, "Xbox": 3, "Switch": 4}
"""
def update_inventory(inventory, shipment):
    updated = {}
    for item in inventory:
        updated[item] = inventory[item]
    for item in shipment: 
        if item in updated:
            updated[item] = updated[item] + shipment[item]
        else:
            updated[item] = shipment[item]
    return updated 

"""
Mock Question B — Encapsulation (Like SmartLight)
Create class:
class SmartFan
Rules:
Private speed starts at 1
Getter returns speed
Setter only allows speed between 1 and 5
"""
class SmartFan:
    def __init__(self):
        self._speed = 1
    @ property
    def speed(self):
        return self._speed
    @speed.setter
    def speed(self,value):
        if 1<= value <= 5:
            self._speed = value
        else:
            print("Error: Speed must be between 1 and 5")

"""
Mock Question C — Inheritance Override (Like Vault)
Create:
Base class:
class Door
method: lock() → prints "Door locked"
Subclass:
class SmartDoor
Override lock() → prints "Door locked with PIN"
Use super() in constructor to set owner
"""
class Door: 
    def __init__(self,owner):
        self.owner = owner
    def lock(self):
        print("Door Locked")
class SmartDoor(Door):
    def __init__(self, owner):
        super().__init__(owner)
    def lock(self):
        print ("Door locked with PIN")
"""
Mock Question D — Try/Except Conversion (Like clean_data)
Write function: convert_prices(price_list)
Rules:
Convert strings → float
If conversion fails → append None
Use finally → print "Conversion complete"
"""
def convert_prices(price_list):
    converted = []
    try:
        for price in price_list:
            try:
                converted.append(float(price))
            except ValueError:
                print("Error converting '{price}'")
                converted.append(None)
    finally: 
        print("Conversion completed")
    return converted

"""
Mock Question E — Organizing Data (Like Pass/Fail)
Write function: group_by_age(people)
Input:
{"Alice": 17, "Bob": 22, "Charlie": 15}
Rules:
Return:
{ "Minor": [names < 18], "Adult": [names >= 18] }
"""
def group_by_age(people):
    grouped = { "Minor": [], "Adult": []}
    for name in people:
        if people[name] < 18:
            grouped["Minor"].append(name)
        else:
            grouped["Adult"].append(name)
    return grouped

"""
Write recursive function:
def count_odd_digits(num):
Return number of odd digits in num.
Example:
count_odd_digits(12345) → 3
Rules:
No loops
Must use recursion
"""
def count_odd_digits(num):
    if num == 0: 
        return 0
    last_digit = num % 10
    if last_digit % 2 == 1:
        return 1 + count_odd_digits(num // 10)
    else:
        return count_odd_digits(num // 10)
    
"""
Write recursive function:
def only_evens(num): Return a new number containing ONLY the even digits.
Example:
only_evens(123456) → 246
Rules:
No loops
Must use recursion
Preserve order
"""
def only_evens(num):
    if num == 0:
        return 0
    last = num % 10
    rest = only_evens(num // 10)
    if last % 2 == 0:
        return rest * 10 + last
    else:
        return rest
    
"""
Write recursive function:
def right_max(num): Return a number where each digit is replaced by the maximum digit to its right.
Example:
right_max(1234) → 4444
right_max(5291) → 9991
"""
def right_max(num):
    if num < 10:
        return num
    right = right_max(num // 10)
    max_right_digit = right % 10
    current_digit = num % 10
    new_digit = max(current_digit, max_right_digit)
    return right * 10 + new_digit

def frequency(txt):
    '''
        >>> frequency('mama')
        {'m': 2, 'a': 2}
        >>> answer = frequency('We ARE Penn State!!!')
        >>> answer
        {'w': 1, 'e': 4, 'a': 2, 'r': 1, 'p': 1, 'n': 2, 's': 1, 't': 2}
        >>> frequency('One who IS being Trained')
        {'o': 2, 'n': 3, 'e': 3, 'w': 1, 'h': 1, 'i': 3, 's': 1, 'b': 1, 'g': 1, 't': 1, 'r': 1, 'a': 1, 'd': 1}
    '''
    freq = {}
    txt = txt.lower()
    for char in txt:
        if char.isalpha():
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
    return freq


def invert(d):
    """
        >>> invert({'one':1, 'two':2,  'three':3, 'four':4})
        {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
        >>> invert({'one':1, 'two':2, 'uno':1, 'dos':2, 'three':3})
        {3: 'three'}
        >>> invert({'123-456-78':'Sara', '987-12-585':'Alex', '258715':'sara', '00000':'Alex'}) 
        {'Sara': '123-456-78', 'sara': '258715'}
    """
    inverted = {}
    nu_value = {}
    for key in d:
        val = d[key]
        if val in nu_value:
            nu_value[val] += 1
        else: 
            nu_value[val] = 1
    
    for key in d:
        val = d[key]
        if nu_value[val] == 1:
            inverted[val] = key
    return inverted


def employee_update(d, bonus, year):
    """
        >>> records = {2020:{"John":["Managing Director","Full-time",65000],"Sally":["HR Director","Full-time",60000],"Max":["Sales Associate","Part-time",20000]}, 2021:{"John":["Managing Director","Full-time",70000],"Sally":["HR Director","Full-time",65000],"Max":["Sales Associate","Part-time",25000]}}
        >>> employee_update(records,7500,2022)
        {2020: {'John': ['Managing Director', 'Full-time', 65000], 'Sally': ['HR Director', 'Full-time', 60000], 'Max': ['Sales Associate', 'Part-time', 20000]}, 2021: {'John': ['Managing Director', 'Full-time', 70000], 'Sally': ['HR Director', 'Full-time', 65000], 'Max': ['Sales Associate', 'Part-time', 25000]}, 2022: {'John': ['Managing Director', 'Full-time', 77500], 'Sally': ['HR Director', 'Full-time', 72500], 'Max': ['Sales Associate', 'Part-time', 32500]}}
    """
    new_year_data = {}
    prev_year = max(d.keys())
    for employee in d[prev_year]:
        role = d[prev_year][employee][0]
        status = d[prev_year][employee][1]
        salary = d[prev_year][employee][2] + bonus
        new_year_data[employee] = [role, status, salary]
    d[year] = new_year_data
    return d

import math

# -------- SECTION 1
class Instructor:
    '''
        >>> t1= Instructor('John Doe')
        >>> t1.get_name()
        'John Doe'
        >>> t1.get_courses()
        []
        >>> t1.add_course('MATH140')
        >>> t1.get_courses()
        ['MATH140']
        >>> t1.add_course('STAT100')
        >>> t1.get_courses()
        ['MATH140', 'STAT100']
        >>> t1.add_course('STAT100')
        >>> t1.get_courses()
        ['MATH140', 'STAT100']
        >>> t1.remove_course('MATH141')
        >>> t1.get_courses()
        ['MATH140', 'STAT100']
        >>> t1.remove_course('MATH140')
        >>> t1.get_courses()
        ['STAT100']
    '''

    def __init__(self, name):
        self.name = name
        self.courses = []

    def get_name(self):
        return self.name
    
    def set_name(self, new_name):
       if isinstance(new_name, str) and new_name != "":
           self.name = new_name

    def get_courses(self):
        return self.courses

    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
        
    def add_course(self,course):
        if course not in self.courses:
            self.courses.append(course)

# -------- SECTION 2      
class Pantry:
    """"
        >>> sara_pantry = Pantry()                
        >>> sara_pantry.stock_pantry('Bread', 2)
        'Pantry Stock for Bread: 2.0'
        >>> sara_pantry.stock_pantry('Cookies', 6) 
        'Pantry Stock for Cookies: 6.0'
        >>> sara_pantry.stock_pantry('Chocolate', 4) 
        'Pantry Stock for Chocolate: 4.0'
        >>> sara_pantry.stock_pantry('Pasta', 3)     
        'Pantry Stock for Pasta: 3.0'
        >>> sara_pantry
        I am a Pantry object, my current stock is {'Bread': 2.0, 'Cookies': 6.0, 'Chocolate': 4.0, 'Pasta': 3.0}
        >>> sara_pantry.get_item('Pasta', 2)     
        'You have 1.0 of Pasta left'
        >>> sara_pantry.get_item('Pasta', 6) 
        'Add Pasta to your shopping list!'
        >>> sara_pantry
        I am a Pantry object, my current stock is {'Bread': 2.0, 'Cookies': 6.0, 'Chocolate': 4.0, 'Pasta': 0.0}
        >>> ben_pantry = Pantry()                    
        >>> ben_pantry.stock_pantry('Cereal', 2)
        'Pantry Stock for Cereal: 2.0'
        >>> ben_pantry.stock_pantry('Noodles', 5) 
        'Pantry Stock for Noodles: 5.0'
        >>> ben_pantry.stock_pantry('Cookies', 9) 
        'Pantry Stock for Cookies: 9.0'
        >>> ben_pantry.stock_pantry('Cookies', 8) 
        'Pantry Stock for Cookies: 17.0'
        >>> ben_pantry.get_item('Pasta', 2)       
        "You don't have Pasta"
        >>> ben_pantry.get_item('Cookies', 2.5) 
        'You have 14.5 of Cookies left'
        >>> sara_pantry.transfer(ben_pantry, 'Cookies')
        >>> sara_pantry
        I am a Pantry object, my current stock is {'Bread': 2.0, 'Cookies': 20.5, 'Chocolate': 4.0, 'Pasta': 0.0}
        >>> ben_pantry.transfer(sara_pantry, 'Rice')
        >>> ben_pantry.transfer(sara_pantry, 'Pasta')
        >>> ben_pantry
        I am a Pantry object, my current stock is {'Cereal': 2.0, 'Noodles': 5.0, 'Cookies': 0.0}
        >>> ben_pantry.transfer(sara_pantry, 'Pasta')
        >>> ben_pantry
        I am a Pantry object, my current stock is {'Cereal': 2.0, 'Noodles': 5.0, 'Cookies': 0.0}
        >>> sara_pantry
        I am a Pantry object, my current stock is {'Bread': 2.0, 'Cookies': 20.5, 'Chocolate': 4.0, 'Pasta': 0.0}
    """

    def __init__(self):
        self.items = {}
    
    def __repr__(self):
        return f"I am a Pantry object, my current stock is {self.items}"

    def stock_pantry(self, item, qty):
        qty = float(qty)
        if item in self.items:
            self.items[item] += qty
        else:
            self.items[item] = qty
        return f"Pantry Stock for {item}: {self.items[item]}"

    def get_item(self, item, qty):
        qty = float(qty)
        if item not in self.items:
            return f"You don't have {item}"
        if self.items[item] > qty:
            self.items[item] -= qty
            return f"You have {self.items[item]} of {item} left"
        else:
            self.items[item] = 0.0
            return f"Add {item} to your shopping list!"
    
    def transfer(self, other_pantry, item):
        if item in other_pantry.items and other_pantry.items[item] > 0:
            qty = other_pantry.items[item]
            self.items[item] = self.items.get(item, 0) + qty
            other_pantry.items[item] = 0.0

# -------- SECTION 3
class Player:
    """
        >>> p1 = Player('Susy')
        >>> print(p1)
        No game records for Susy
        >>> p1.update_loss()
        >>> p1
        *Game records for Susy*
        Total games: 1
        Games won: 0
        Games lost: 1
        Best game: None
        >>> p1.update_win(5)
        >>> p1.update_win(2)
        >>> p1
        *Game records for Susy*
        Total games: 3
        Games won: 2
        Games lost: 1
        Best game: 2 attempts
    """
    def __init__(self, name):
        self.name = name
        self.total = 0
        self.wins = 0
        self.losses = 0
        self.best = None

    def update_win(self, att):
        self.total += 1
        self.wins += 1
        if self.best is None or att < self.best:
            self.best = att
    
    def update_loss(self):
       self.total += 1
       self.losses += 1
    
    def __str__(self):
       if self.total == 0:
           return f'No game records for {self.name}'
       return (
            f"*Game records for {self.name}*\n"
            f"Total games: {self.total}\n"
            f"Games won: {self.wins}\n"
            f"Games lost: {self.losses}\n"
            f"Best game: {self.best if self.best is not None else 'None'}"
            + ("" if self.best is None else " attempts")
        )
    __repr__=__str__

class Wordle:
    """
        >>> p1 = Player('Susy')
        >>> p2 = Player('Taylor')
        >>> w1 = Wordle(p1, 'water')
        >>> w2 = Wordle(p2, 'cloud')
        >>> w3 = Wordle(p1, 'jewel')
        >>> w1.play('camel')
        '_A_E_'
        >>> w1.play('ranes')
        'rA_E_'
        >>> w1.play('baner')
        '_A_ER'
        >>> w1.play('pacer')
        '_A_ER'
        >>> w1.play('water')
        'You won the game'
        >>> w1.play('rocks')
        'Game over'
        >>> w1.play('other')
        'Game over'
        >>> w3.play('beast')
        '_E___'
        >>> w3.play('peace')
        '_E__e'
        >>> w3.play('keeks')
        '_Ee__'
        >>> w3.play('jewel')
        'You won the game'
        >>> w2.play('classes')
        'Guess must be 5 letters long'
        >>> w2.play('cs132')
        'Guess must be all letters'
        >>> w2.play('audio')
        '_ud_o'
        >>> w2.play('kudos')
        '_udo_'
        >>> w2.play('would')
        '_oulD'
        >>> w2.play('bound')
        'The word was cloud'
        >>> w2.play('cloud')
        'Game over'
        >>> p1
        *Game records for Susy*
        Total games: 2
        Games won: 2
        Games lost: 0
        Best game: 4 attempts
        >>> p2
        *Game records for Taylor*
        Total games: 1
        Games won: 0
        Games lost: 1
        Best game: None
    """
    max_attempts = 6
    def __init__(self, player, word):
       self.player = player
       self.word = word
       self.attempts = 0
       self.over = False
    
    def process_guess(self, guess):
        if len(guess) != 5:
            return "Guess must be 5 letters long"
        if not guess.isalpha():
            return "Guess must be all letters"

        result = ['_'] * 5
        word_chars = list(self.word)

        for i in range(5):
            if guess[i] == self.word[i]:
                result[i] = guess[i].upper()
                word_chars[i] = None  
        for i in range(5):
            if result[i] == '_':
                if guess[i] in word_chars:
                    result[i] = guess[i].lower()
                    word_chars[word_chars.index(guess[i])] = None

        return ''.join(result)

    def play(self, guess):
        if self.over:
            return "Game over"

        feedback = self.process_guess(guess)


        self.attempts += 1

        if guess == self.word:
            self.player.update_win(self.attempts)
            self.over = True
            return "You won the game"

        if feedback in ["Guess must be 5 letters long", "Guess must be all letters"]:
            if self.attempts >= Wordle.max_attempts:
                self.player.update_loss()
                self.over = True
                return f"The word was {self.word}"
            return feedback

        if self.attempts >= Wordle.max_attempts:
            self.player.update_loss()
            self.over = True
            return f"The word was {self.word}"

        return feedback
       

# -------- SECTION 4
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line: 
    ''' 
        >>> p1 = Point2D(-7, -9)
        >>> p2 = Point2D(1, 5.6)
        >>> line1 = Line(p1, p2)
        >>> line1.getDistance
        16.648
        >>> line1.getSlope
        1.825
        >>> line1
        y = 1.825x + 3.775
        >>> line2 = line1*4
        >>> line2.getDistance
        66.592
        >>> line2.getSlope
        1.825
        >>> line2
        y = 1.825x + 15.1
        >>> line1
        y = 1.825x + 3.775
        >>> line3 = line1*4
        >>> line3
        y = 1.825x + 15.1
        >>> line5=Line(Point2D(6,48),Point2D(9,21))
        >>> line5
        y = -9.0x + 102.0
        >>> Point2D(45,3) in line5
        False
        >>> Point2D(34,-204) in line5
        True
        >>> line6=Line(Point2D(2,6), Point2D(2,3))
        >>> line6.getDistance
        3.0
        >>> line6.getSlope
        inf
        >>> isinstance(line6.getSlope, float)
        True
        >>> line6
        Undefined
        >>> line7=Line(Point2D(6,5), Point2D(9,5))
        >>> line7.getSlope
        0.0
        >>> line7
        y = 5.0
        >>> Point2D(9,5) in line7
        True
        >>> Point2D(89,5) in line7
        True
        >>> Point2D(12,8) in line7
        False
        >>> (9,5) in line7
        False
    '''
    def __init__(self, point1, point2):
        self.p1 = point1
        self.p2 = point2

    @property

    def getDistance(self):
        return round(math.sqrt((self.p2.x - self.p1.x)**2 + (self.p2.y - self.p1.y)**2), 3)
    @property
       
    def getSlope(self):
        if self.p2.x == self.p1.x:
            return float('inf')
        return round((self.p2.y - self.p1.y) / (self.p2.x - self.p1.x), 3)

    @property
    def intercept(self):
        if self.getSlope == float('inf'):
            return None
        return round(self.p1.y - self.getSlope * self.p1.x, 3)

    def __str__(self):
        if self.getSlope == float('inf'):
            return "Undefined"
        if self.getSlope == 0:
            return f"y = {float(self.p1.y)}"
        return f"y = {self.getSlope}x + {self.intercept}"

    __repr__ = __str__

    def __mul__(self, other):
        if not isinstance(other, int):
            return None
        return Line(
            Point2D(self.p1.x * other, self.p1.y * other),
            Point2D(self.p2.x * other, self.p2.y * other)
        )

    def __contains__(self, point):
        if not isinstance(point, Point2D):
            return False
        if self.getSlope == float('inf'):
            return False

        expected_y = self.getSlope * point.x + self.intercept
        return math.isclose(point.y, expected_y)

def is_power_of(base, num):
    """
        >>> is_power_of(5, 625)  # pow(5, 4) = 5 * 5 * 5 * 5 = 625
        True
        >>> is_power_of(5, 1)    # pow(5, 0) = 1
        True
        >>> is_power_of(5, 5)    # pow(5, 1) = 5
        True
        >>> is_power_of(5, 15)   # 15 is not a power of 5 (it's a multiple)
        False
        >>> is_power_of(3, 9)
        True
        >>> is_power_of(3, 8)
        False
        >>> is_power_of(3, 10)
        False
        >>> is_power_of(1, 8)
        False
        >>> is_power_of(2, 0)    # 0 is not a power of any positive base.
        False
        >>> is_power_of(4, 16)
        True
        >>> is_power_of(4, 64)
        True
        >>> is_power_of(4, 63)
        False
        >>> is_power_of(4, 65)
        False
        >>> is_power_of(4, 32)
        False
    """
    if num == 1:
        return True
    if base == 1:
        return num == 1
    if num == 0 or num < base:
        return False
    if num % base != 0:
        return False
    return is_power_of(base, num//base)

def cut(a_list):
    """
        >>> cut([7, 4, 0])
        [7, 4, 0]
        >>> myList=[7, 4, -2, 1, 9]
        >>> cut(myList)   # Found(-2) Delete -2 and 1
        [7, 4, 9]
        >>> myList
        [7, 4, -2, 1, 9]
        >>> cut([-4, -7, -2, 1, 9]) # Found(-4) Delete -4, -7, -2 and 1
        [9]
        >>> cut([-3, -4, 5, -4, 1])  # Found(-3) Delete -2, -4 and 5. Found(-4) Delete -4 and 1
        []
        >>> cut([5, 7, -1, 6, -3, 1, 8, 785, 5, -2, 1, 0, 42]) # Found(-1) Delete -1. Found(-3) Delete -3, 1 and 8. Found(-2) Delete -2 and 0
        [5, 7, 6, 785, 5, 0, 42]
	"""
    if len(a_list) == 0:
        return []
    first = a_list[0]
    if first >= 0:
        return [first] + cut(a_list[1:])
    else:
        skip = abs(first)
        return cut(a_list[skip:])

def right_max(num_list):
    """
        >>> right_max([3, 7, 2, 8, 6, 4, 5])
        [8, 8, 8, 8, 6, 5, 5]
        >>> right_max([1, 2, 3, 4, 5, 6])
        [6, 6, 6, 6, 6, 6]
        >>> right_max([1, 25, 3, 48, 5, 6, 12, 14, 89, 3, 2])
        [89, 89, 89, 89, 89, 89, 89, 89, 89, 3, 2]
    """
    if len(num_list) == 1:
        return[num_list[0]]
    right = right_max(num_list[1:])
    current_max = num_list[0] if num_list[0] > right [0] else right [0]
    return [current_max] + right 


def consecutive_digits(num):
    """
        >>> consecutive_digits(2222466666678)
        True
        >>> consecutive_digits(12345684562)
        False
        >>> consecutive_digits(122)
        True
    """
    if num < 10:
        return False
    last = num % 10
    second_last = (num// 10) % 10
    if last == second_last:
        return True
    return consecutive_digits(num//10)
        