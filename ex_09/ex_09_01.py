name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    if "From:" in line:
        words = line.rstrip()
        words = words.split()
        words = words[1:]
        print(words)
        for word in words:
            counts[word] = counts.get(word, 0) + 1

mostcount = None
mostemail = None
for word,count in counts.items():
    if mostcount is None or count > mostcount:
            mostemail = word
            mostcount = count

print (mostemail, mostcount)