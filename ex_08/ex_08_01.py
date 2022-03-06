fname = input("Enter file name: ")
fh = open(fname)
templst = list ()
lst = list ()
for line in fh:
    temp = line.rstrip()
    temp = temp.split()
    templst = templst + temp
for test in templst:
    if test not in lst:
        lst.append(test)
lst.sort()
print(lst)
