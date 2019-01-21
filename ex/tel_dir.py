
dir = {}

while True:
    name = input("Enter name [end to stop] :")
    if name == 'end':
        break

    mobile = input("Enter mobile number :")
    dir[name] = mobile


for n,m in sorted(dir.items()):
    print(f"{n:20s} {m}")
