class EvenIterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.num = self.start if self.start % 2 == 0 else self.start + 1

    def __next__(self):
        if self.num > self.end:
            raise StopIteration

        self.num += 2
        return self.num - 2


class EvenNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return EvenIterator(self.start, self.end)


e1 = EvenNumbers(10, 20)
ei1 = iter(e1)
print(ei1.__next__())  # 10
ei2 = iter(e1)
print(ei2.__next__())  # 10
print(ei2.__next__())  # 12
print(ei1.__next__())  # 12
