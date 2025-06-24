class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n: int) -> int:
        self._validate(n)

        if (self.size + n) > self.capacity:
            raise ValueError("Capacity exceeded")

        self._size += n

        return self._size


    def withdraw(self, n: int) -> int:
        self._validate(n)

        if (self.size - n) < 0:
            raise ValueError("Not enough cookies to withdraw")

        self._size -= n

        return self._size

    @property
    def capacity(self):
        return self._capacity


    @property
    def size(self):
        return self._size


    @capacity.setter
    def capacity(self, capacity: int):
        self._validate(capacity)

        self._capacity = capacity


    @size.setter
    def size(self, size: int):
        self._validate(size)

        self._size = size


    def _validate(self, n: int):
        if not isinstance(n, int):
            raise ValueError("Not an integer")

        if n < 0:
            raise ValueError("Cannot be negative")
