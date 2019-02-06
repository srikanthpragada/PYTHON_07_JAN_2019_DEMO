class EvenIterator:
    def __init__(self,start,end):
        self.start = start
        self.end = end

    def __iter__(self):
        self.num = self.start if self.start % 2 == 0 else self.start + 1
        return self

    def __next__(self):
        if self.num > self.end:
            raise StopIteration

        self.num += 2
        return self.num - 2


# ei = EvenIterator(10,20)
# for n in ei:
#     print(n)

e1 = EvenIterator(10,20)
ei1 = iter(e1)
print(ei1.__next__())  # 10
ei2 = iter(e1)
print(ei2.__next__())  # 10
print(ei2.__next__())  # 12
print(ei1.__next__())  # 14





