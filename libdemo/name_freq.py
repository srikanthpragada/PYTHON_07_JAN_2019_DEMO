f = open("names.txt","rt")
names_freq ={}
for line in f.readlines():
    names = line.strip('\n').split(",")
    for n in names:
        # Ignore empty strings
        if len(n) == 0:
            continue

        if n in names_freq:
           names_freq[n] += 1   # Increment count if name found
        else:
           names_freq[n] = 1    # Add name to dict if name is new

f.seek()
f.close()

for n,c in names_freq.items():
    print(n,c)

