num1 = 17
num2 = num1

print("Sebelum num2 di Update: ")
print("num1 =", num1)
print("num2 =", num2)

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))

num2 = 106

print("\n Setelah num2 di Update: ")
print("num1 =", num1)
print("num2 =", num2)

print("\nnum1 points to:", id (num1))
print("num2 points to:", id(num2))

num1 = num2

print("\nSetelah num1 di Update: ")
print("num1 =", num1)
print("num2 =", num2)

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))