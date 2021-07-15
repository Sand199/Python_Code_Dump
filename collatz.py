import sys


def collatz(number):
    if number % 2 == 0:
        print(number // 2)

        return number // 2
    else:
        print(3 * number + 1)

        return 3 * number + 1


try:
    num = int(input("Enter a number:\n"))
except ValueError:
    print("Error: You must enter an integer")
    sys.exit()
n = 0

while num != 1:
    num = collatz(num)
    n += 1
print("steps =", n)
