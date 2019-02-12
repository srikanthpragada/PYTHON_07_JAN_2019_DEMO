import re

f = open("phones.txt","rt")
PATTERN  = "[^0-9]+"
phones = []

for line in f:
    lst = re.split(PATTERN,line)
    for v in lst:
        if re.fullmatch("^[0-9]{10}$",v) is not None:
            phones.append(v)


for p in sorted(phones):
    print(p)


