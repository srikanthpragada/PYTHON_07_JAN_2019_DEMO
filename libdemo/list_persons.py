from datetime import datetime

f = open("persons.txt", "rt")
persons = {}
cd = datetime.now()

for line in f.readlines():
    parts = line.split(",")
    if len(parts) < 2:
        continue  # ignore line and continue with next iteration

    name = parts[0]
    dobstr = parts[1].strip("\n")
    try:
        dob = datetime.strptime(dobstr, "%d-%m-%Y")
        td = cd - dob
        years = td.days // 365
        persons[name] = years
    except:
        pass

for (name, age) in sorted(persons.items(), key=lambda v: v[1]):
    print(name, age)
