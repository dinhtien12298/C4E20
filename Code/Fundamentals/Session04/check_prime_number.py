n = int(input("Enter a number: "))

for i in range (2,n):
    if n % i == 0:
        print(n, "is not a prime number!")
        break
print(n, "is a prime number!")

# is_prime = True
# loop = True
# i = 2

# while i < n:
#     if n % i == 0:
#         is_prime = False
#     i += 1

# # if is_prime == True:
# if is_prime:
#     print("{} is a prime number".format(n))
# else:
#     print("{} is not a prime number".format(n))