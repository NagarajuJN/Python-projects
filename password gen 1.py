
import random

print(" Well come to Password Generator ")

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*~-+()<>?,./:'

numbers = int(input("Amount of password to generate:"))

length = int(input(" number of character should contain:"))
print("\n Your Password is:")
for pwd in range(numbers):
    passwords = " "
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)