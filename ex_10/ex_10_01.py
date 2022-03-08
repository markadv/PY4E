name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
tdict = dict()
lst = list()

for line in handle:
    if "From " in line:
        hours = line.rstrip()
        hours = line.split()
        hours = hours[5]
        hours = hours.split(":")
        hours = hours[0]
        tdict[hours] = tdict.get(hours, 0) + 1

lst = sorted ([(k, v) for k, v in tdict.items()])

for k, v in lst:
    print(k ,v)