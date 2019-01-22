dir = {}

while True:
    name = input("Enter name [end to stop] :")
    if name == 'end':
        break

    mobile = input("Enter mobile number :")
    if name in dir:  # Name is already present, so add to existing set
        dir[name].add(mobile)
    else:   # New entry so add name and mobile as element in set
        dir[name] = {mobile}


for n,m in sorted(dir.items()):
    print(f"{n:20s} {','.join(sorted(m))}")
