print("Hello World!")

print("   ____")
print("  |    |")
print("  |    o")
print("  |   /|\ ")
print("  |    |")
print("  |   / \ ")
print(" _|_")
print("|   |______")
print("|          |")
print("|__________|")

x = 5
y = 5

print("Type of var x is:")
print(type(x))

print("Input values are:")
print(x)
print(y)

# If Condition
if x > y:
    print("x is greater than y.")
elif x < y:
    print("y is greater than x!")
else:
    print("These numbers are equal.")

# Print Part of String
b = "This is a text!"
print(b[3:6])

# Strip Whitespace
print(b.strip())

# Arrays and Lists
c = "These,Are,Some,Values"
list = c.split(",")
list.append("Yvo")
print(list[2])
print(list[4])

print(type(list))

list = str(list.reverse())

print(type(list))

print(len(list)) # Returns length of this list

#For Item in List
for item in list:
    print("Test: " + item)

inp = raw_input("Give me a value: ")
print(inp)

#Dictionaries
thisdict =	{
  "Hallo": "Hello",
  "Apfel": "Apple",
  "Birne": "Pear"
}
print(thisdict)
thisdict["Hallo"] = "Hiigh"
print(thisdict)

#While Loop
i = 1
while i < 6:
  i += 1
  if i == 4:
    continue
  print(i)

#Recursion
def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

#Functions
def print_text(text):
  print(text)

inp = raw_input("Give me a value to print: ")
print_text(inp)

#Lambda Functions
print("Lambda Functions")

myfunc = lambda x,y: x*y
print(myfunc(3,6))


def myfunc2(n):
  return lambda i: i*n

doubler = myfunc2(2)
tripler = myfunc2(3)
val = 11
print("Doubled: " + str(doubler(val)) + ". Tripled: " + str(tripler(val)))
