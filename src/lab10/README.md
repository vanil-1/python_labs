# lab10

## structures

### Stacks

#### __init__(), push():

__int__() создаёт поле для хранения данных, а push() добавляет элемент в конец стека: 

![structures](/images/lab10/structures/init_push_st.png)

#### pop(), peek(), is_empty(), __len__():

pop() выводит последний (верхний) элемент стека, а затем удаляет его из стека. peek() совершает такую же работу как и pop(), но без удаления элемента. is_empty() проверяет, является ли стек пустым или нет. __len__() выводит длину стека:

![structures](/images/lab10/structures/pop_peek_is_empty_len_st.png)

#### results:

Результаты работы программы представлены ниже:

![structures](/images/lab10/structures/result_st.png)

### Queue:

#### __init__(), eqnueue(), dequeue(), peek():

__int__() создаёт поле для хранения данных, а enqueue() добавляет элемент в начало очереди. dequeue() выводит первый элемент очереди, а также удаляет его. peek() выводит самый первый элемент очереди: 

![structures](/images/lab10/structures/init_en_de_peek_q.png)

#### pop(), peek(), is_empty(), __len__():

is_empty() проверяет, является ли очередь пустой или нет. __len__() выводит длину очереди:

![structures](/images/lab10/structures/is_empty_len_q.png)

#### results:

Результаты работы программы представлены ниже:

![structures](/images/lab10/structures/result_q.png)

## linked_list

### Node, __init__(), append(), prepend():

Node - класс узла с атрибутами значения и ссылки. __init__() создаёт атрибуты начального узла (self.head) и конечного (self.tail), а также устанавливает изначальный размер (длину) односвязного списка равный 0. append() добавляет элемент в конец списка, а prepend в начало:

![linked_list](/images/lab10/linked_list/init_append_prepend.png)

#### insert():

insert() добавляет в список новый узел по индексу (idx):

![linked_list](/images/lab10/linked_list/insert.png)

#### remove():

Удаляет узел по его значению:

![linked_list](/images/lab10/linked_list/remove.png)

#### remove_at():

Удаляет узел по его индексу:

![linked_list](/images/lab10/linked_list/remove_at.png)

#### __iter__(), __len__(), __repr__(), size(), str_linking_list():

__iter__() итерирует односвязный список, позволяя работать с ним как с классическим списком. __len__() - длина списка. __repr__() выводит односвязный список в читаемом виде. size() - размер спика (равно = __len__()),  str_linking_list() - выводит список в виде:

[A] -> [B] -> [C] -> None

![linked_list](/images/lab10/linked_list/iter_len_repr_size_str.png)

#### result:

Ниже представлен результат работы программы:

![linked_list](/images/lab10/linked_list/result.png)