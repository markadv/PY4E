fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

lst = list()
for line in fh:
    if "From:" in line:
        lst = line.rstrip()
        lst = lst.split()
        lst = lst[1:]
        count = count+1
        print(lst[0])

print("There were", count, "lines in the file with From as the first word")
