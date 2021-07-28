import sys

file = open(f"{sys.argv[1]}", "r")

numbers = []
for number in file:
  numbers.append(float(number.strip()))

print(sorted(numbers, reverse=True), end="")
