class MyArray:

    def __init__(self, capacity: int):
        self._data = []
        self._capacity = capacity

    def __getitem__(self, item: int) -> int:
        return self._data[item]

    def __setitem__(self, key: int, value: int):
        self._data[key] = value

    def __len__(self) -> int:
        return len(self._data)

    def __iter__(self):
        for item in self._data:
            yield item

    def find(self, index: int):
        try:
            self._data[index]
        except IndexError:
            return None

    def delete(self, index: int) -> bool:
        try:
            self._data.pop(index)
            return True
        except IndexError:
            return False

    def insert(self, index: int, value: int) -> bool:
        if len(self._data) >= self._capacity:
            return False
        else:
            self._data.insert(index, value)
            return True

    def __str__(self) -> str:
        return str(self._data)


if __name__ == "__main__":
    array = MyArray(5)
    array.insert(0, 0)
    array.insert(1, 1)
    array.insert(2, 2)
    array.insert(3, 3)
    array.insert(4, 4)
    print(array)
