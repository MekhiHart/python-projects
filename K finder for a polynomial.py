# Max two polynomials
# ONLY whole number inputs
# Asks for the x and y values of a vertex and prints it
x = (int(input("What is your x value: ")))
y = (int(input("What is your y value: ")))

print(f"The vertex is ({x},{y})")

# Asks what is the polynomial and prints it
# Needs to keep asking for polynomials until user wishes to
print("Inputted values for the polynomial are in the terms of (x+a)(x+b)")
a = (int(input("What is the value of a: ")))
b = (int(input("What is the value of b: ")))
c = f"(x + {a})"
d = f"(x + {b})"

e = {c + d}

print(f"The whole polynomial is {e} ")

# Finding value k from the given input and printing k
A = x + a
B = x + b
C = A * B
k = y / C

print(f"The k value of the polynomial is: {k}")
