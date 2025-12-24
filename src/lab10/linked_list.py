class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node

        self._size += 1

    def prepend(self, value):
        new_node = Node(value, next=self.head)
        self.head = new_node

        if self._size == 0:
            self.tail = new_node

        self._size += 1

    def insert(self, idx, value):
        if idx < 0:
            raise IndexError("Negative index is unsupported!")

        elif 0 < idx <= self._size:
            current = self.head
            for _ in range(idx - 1):
                current = current.next

            new_node = Node(value, next=current.next)

            if idx == self._size:
                self.tail = new_node
            current.next = new_node

            self._size += 1

        elif idx == 0:
            self.prepend(value)
            return

        else:
            raise IndexError("Index is out of range")

    def remove(self, value):
        if self.head is None:
            raise IndexError("List is empty")

        elif value == self.head.value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self._size -= 1
            return f"Remove element with value = {value} was successful!"

        current = self.head
        while current.next is not None and current.next.value != value:
            current = current.next

        if current.next:
            current.next = current.next.next
        else:
            raise ValueError("No such value in list!")

        if current.next is None:
            self.tail = current

        self._size -= 1
        return f"Remove element with value = {value} was successful!"

    def remove_at(self, idx: int):
        if self.head is None:
            raise IndexError("List is empty")

        else:
            if idx < 0:
                raise IndexError("Negative index is unsupported!")

            elif idx == 0:
                self.head = self.head.next
                if self._size == 1:
                    self.head = None
                    self.tail = None

            elif 0 < idx < self._size:
                current = self.head
                for _ in range(idx - 1):
                    current = current.next

                current.next = current.next.next

                if idx == self._size - 1:
                    self.tail = current
            else:
                raise IndexError("Index is not supported")

        self._size -= 1
        return f"Remove element[{idx}] was successful!"

    def __iter__(self):
        current = self.head

        while current is not None:
            yield current.value
            current = current.next

    def __len__(self):
        return self._size

    def __repr__(self):
        values = list(self)
        return f"SinglyLinkedList({values})"

    def size(self):
        return self._size

    def str_linking_list(self):
        return " -> ".join(f"[{value}]" for value in self) + " -> None"


ll = SinglyLinkedList()
samples = [1, 23, 23, 40, 50, 2]
for i in samples:
    ll.append(i)
print(ll)
print("-" * 64)

ll.insert(1, 7)
ll.insert(7, 25)
print(f"insert(): {ll}")
print("-" * 64)

ll.remove(7)
ll.remove(23)
print(f"remove: {ll}")
print("-" * 64)

ll.remove_at(0)
ll.remove_at(1)
print(f"remove_at: {ll}")
print("-" * 64)

print(ll.str_linking_list())
