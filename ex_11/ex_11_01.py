import re

name = input("Enter file:")
if len(name) < 1:
    name = "regex_sum_1501527.txt"
handle = open(name)

temp = list()
total = 0
for line in handle:
    temp = temp + re.findall('[0-9]+', line)

for sum in temp:
    sum = int(sum)
    total = total + sum

print(total)