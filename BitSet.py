class bitset():
    def __init__(self, data):
        import sys
        self.block = sys.getsizeof(1)
        self.data = [0] * ((len(data) + self.block - 1) // self.block)
        if not self.data:
            self.data = []
        self.last = len(data) % self.block
        self.length = len(data)
        for i in range(0, len(self.data) - 1):
            for j in range(self.block):
                self.data[i] += data[self.block * i + j] * (1 << j)
        if self.data:
            for j in range((self.last - 1) % self.block + 1):
                self.data[-1] += data[self.block * (len(self.data) - 1) + j] * (1 << j)

    def __getitem__(self, i):
        if i > self.length:
            raise Exception('Index out of range')
        x, y = divmod(i, self.block)
        return (self.data[x] >> y) % 2

    def __setitem__(self, key, value):
        if key > self.length:
            raise Exception('Index out of range')
        x, y = divmod(key, self.block)
        self.data[x] -= b[key] * (1 << y)
        if value:
            self.data[x] += 1 << y
        return (self.data[x] >> y) % 2

    def append(self, item):
        item = bool(item)
        self.length += 1
        if self.last == 0:
            if item:
                self.data.append(item * (1 << self.block - 1))
            else:
                self.data.append(0)
            self.last = 1
        else:
            if item:
                self.data[-1] += item * (1 << self.last)
            self.last = (self.last + 1) % self.block

    def pop(self):
        self.length -= 1
        item = self.data[-1] % (1 << ((self.last - 1) % self.block))
        self.data[-1] %= 1 << ((self.last - 1) % self.block)
        self.last = (self.last - 1) % self.block
        return bool(item)

    def __str__(self):
        s = []
        for i in range(len(self.data) - 1):
            k = self.data[i]
            for j in range(self.block):
                s.append(bool(k % 2))
                k //= 2
        k = self.data[-1]
        for j in range((self.last + self.block - 1) % self.block + 1):
            s.append(bool(k % 2))
            k //= 2
        return s.__str__()


from random import randint
import sys
import copy
for n in range(0, 100000, 10000):
    a = [bool(randint(0, 1)) for i in range(n)]
    b = bitset(a)
    print(f'Size(list of bool) / Size(bitset) for n = {n}: {sys.getsizeof(a) / sys.getsizeof(b.data)}')
print(sys.getsizeof(1))
print(a.__str__() == b.__str__())
