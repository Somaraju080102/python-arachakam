# In Python, variables are just labels that can point to objects of any type.

x = 10          # sticky note "x" on an int
x = "hello"     # same note, now on a string. Totally legal.
print(type(x))  # <class 'str'>



# Python has a few built-in types. Here are some of the most common ones:

age = 30              # int (no overflow, ints can be gigantic)
price = 99.99         # float
name = "Nani"         # str (single or double quotes, same thing)
active = True         # bool (capital T/F)
nothing = None        # Python's null

print(10 / 3)    # 3.333... (always float)
print(10 // 3)   # 3 (floor division)
print(10 % 3)    # 1
print(2 ** 10)   # 1024 (power)

# Python has a few built-in types. Here are some of the most common ones:

name = "Nani"
role = "Analyst"
print(f"{name} works as {role}")   
print(f"My job roles is {role}")        # f-string, use this always
print(f"2 + 2 = {2 + 2}")                  # expressions work inside {}
print(f"{3.14159:.2f}")                    # 3.14 (format spec)
print(f"{1000000:,}")                      # 1,000,000
print(f"{name!r}")                         # 'Nani' (repr form)
print(f"{name=}")                          # name='Nani' (great for debugging)

# User input functions. input() always returns a string, so you need to convert it if you want a different type.

# user = input("Your name: ")     # always returns a string!
# age = int(input("Age: "))       # convert yourself
print("a", "b", sep="-", end="!\n")   # a-b!

# Python has a few built-in operators. Here are some of the most common ones:

print(1 < 2 < 10)        # chained comparison, legal and readable
print('x' == 'X')              # value equality (like Java's .equals())
print('x' is 'X')            # same object identity (like Java's ==)
#print(and, or, not)     # no &&, ||, !

# Python has a few built-in data structures. Here are some of the most common ones:
items = []
if not items:           # Pythonic. Don't write `len(items) == 0`
    print("empty")

# name = input("Name: ") or "Guest"    # default if empty string
# items.append(name)        # add to end
# print(items.count)           # first item

 ## Python has a few built-in functions. Here are some of the most common ones:n
print((5).bit_length()) #101
print("abc".upper())
print(type(5), type(len), type(print))
print(dir(5))        # peek at what an int can do

# Python has a few built-in modules. Here are some of the most common ones:
a = 256; b = 256
print(a is b)       # True
a = 1000; b = 1000
print(a is b)       # may be False in the REPL

if (n := len("hello")) > 3:
       print(f"long, {n} chars")


a, b = 1, 2
a, b = b, a          # swap, no temp variable needed
x = y = 0