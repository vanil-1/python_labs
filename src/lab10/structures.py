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


stack = Stack()

print(f"is_empty: {stack.is_empty()}")  # Если True, то stack - пустой

samples_s = [12, 20, 3, 20, 45, 9]
for i in samples_s:
    stack.push(i)

print(f"stack._data: {stack._data}")  # Содержимое stack
print(f"peek: {stack.peek()}")  # Последний элемент stack
print(f"__len__: {stack.__len__()}")

print(f"pop: {stack.pop()}")  # Последний элемент stack с последующим его удалением
print(f"stack._data: {stack._data}")  # stack после удаления последнего элемента
print(f"peek: {stack.peek()}")  # Последний элемент stack после метода pop
print(f"is_empty: {stack.is_empty()}")

print(f"__len__: {stack.__len__()}")

print("-" * 32)


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


queue = Queue()


print(f"is_empty: {queue.is_empty()}")  # Если True, то queue - пустой

samples_q = [23, 45, 75, 34, 303]
for i in samples_q:
    queue.enqueue(i)

print(f"queue._data: {queue._data}")  # Содержимое queue
print(f"peek: {queue.peek()}")  # Первый элемент queue
print(f"__len__: {queue.__len__()}")

print(f"dequeue: {queue.dequeue()}")  # Первый элемент queue с последующим его удалением
print(f"queue._data: {queue._data}")  # queue после удаления первого элемента
print(f"peek: {queue.peek()}")  # Первый элемент queue после метода dequeue
print(f"is_empty: {queue.is_empty()}")

print(f"__len__: {queue.__len__()}")
