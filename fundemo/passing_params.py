def fun(n):
    print('Before change', id(n))
    n = 0
    print('After change', id(n))

def add(lst,num):
    lst.append(num)

v = 100
print('Address before ', id(v))
fun(v)
print('Address after ', id(v))
print(v)

nums = [10,20]
add(nums,15)
print(nums)
