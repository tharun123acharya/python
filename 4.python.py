# write a pythonic expression to swap two variables a and b without using a third temporary variable
a = int(input("Enter a: "))
b = int(input("Enter b: "))

temp = a
a = b
b = temp

print("a =", a)
print("b =", b)