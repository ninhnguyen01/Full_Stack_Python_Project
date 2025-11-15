def write_a_book(character, setting,
special_skill):
  print(character + " is in " +
        setting + " practicing her " +
        special_skill)
  
def ready_for_school(backpack,
pencil_case):
  if (backpack == 'full' and pencil_case
== 'full'):
    print ("I'm ready for school!")


# Define a function my_function() with parameter x
def my_function(x):
  return x + 1

# Invoke the function
print(my_function(2))
print(my_function(3 + 5))  # Output: 9

# Indentation is used to identify code blocks
def testfunction(number):
  # This code is part of testfunction
  print("Inside the testfunction")
  sum = 0
  for x in range(number):
    # More indentation because 'for' has a code block
    # but still part of the function
    sum += x
  return sum
print("This is not part of testfunction")

def sales(grocery_store, item_on_sale,
cost):
  print(grocery_store + " is selling " +
item_on_sale + " for " + cost)
sales("The Farmer's Market", "toothpaste",
"$1")

def findvolume(length=1, width=1,
depth=1):
  print("Length = " + str(length))
  print("Width = " + str(width))
  print("Depth = " + str(depth))
  return length * width * depth

findvolume(1, 2, 3)
findvolume(length=5, depth=2, width=4)
findvolume(2, depth=3, width=4)

def square_point(x, y, z):
  x_squared = x * x
  y_squared = y * y
  z_squared = z * z
  # Return all three values: return x_squared, y_squared, z_squared
  three_squared, four_squared, five_squared = square_point(3, 4, 5)

a=5
def f1(): 
  a=2
  print(a)

print(a)   # Will print 5
f1()       # Will print 2

def check_leap_year(year):
  if year % 4 == 0:
    return str(year) + " is a leap year."
  else:
    return str(year) + " is not a leap year."
  
year_to_check = 2018
returned_value = check_leap_year(year_to_check)
print(returned_value) # 2018 is not a leap year.

a = "Hello"
def prints_a():
  print(a)
# will print "Hello"
prints_a()

def my_function(value):
  print(value)
# Pass the value 7 into the function
my_function(7)
