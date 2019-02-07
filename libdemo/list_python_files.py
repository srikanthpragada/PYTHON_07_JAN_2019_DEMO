
import os

for dn,dirs,files in os.walk(r"e:\classroom\python\jan7\demo"):
    if dn.find('.git') >= 0:  # ignore dir with .git
        continue
    print("Directory : ", dn)
    for f in files:
        if f.endswith(".py"):
            print(f)





