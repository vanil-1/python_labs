from collections import deque


class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty!")
        else:
            return self._data.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty!")
        else:
            return self._data[-1]

    def is_empty(self) -> bool:
        return not self._data

    def __len__(self) -> int:
        return len(self._data)


class Queue:
    def __init__(self):
        self._data = deque()

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty!")
        else:
            return self._data.popleft()

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty!")
        else:
            return self._data[0]

    def is_empty(self) -> bool:
        return not self._data

    def __len__(self) -> int:
        return len(self._data)
