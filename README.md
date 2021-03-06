# Wargaming-tasks
Решение задач на вакансию Junior Python Programmer (стажер) - Wargaming

1. [isEven](https://github.com/DanilKurshanov/Wargaming-tasks/blob/main/isEven.py) - минусом предложенного решения является
наличие двух оператов (// и *), что привидит с увелечению времени выполнению операции.

2. [CircularBuffer](https://github.com/DanilKurshanov/Wargaming-tasks/blob/main/CircularBuffer.py) - минусом первой реализации 
(CircularBufferV1) явзяеться использования медленного метода list.insert(), что приведет к уменьшению скорости операций.
Использование list.insert() позволяет формировать стек так, что при возврате элемента их стека используется метод list.pop()
cо сложность равной O(1). 

Вторая реализация циклического стека (CircularBufferV2) через индексы списка позволяет сохранять сложность равной O(1)
как при добавлении, так и при извлечении элементов из стека.

Общим минусом можно названить затраты памяти при использование списков.

3. [HeapSort](https://github.com/DanilKurshanov/Wargaming-tasks/blob/main/HeapSort.py) - в качестве варианта для сортировки
массива чисел был выбран алгоритм - Пирамидальная сортировка. Организованные данные в специальную древовидную структуру
(дерево, с родительскими узлами больше чем узлы-потомки) не нужно отдельно хранить, в отличие от других видов деревьев. 
Любой массив уже является деревом, в котором прямо на ходу можно сразу определять родителей и потомков. 
Сложность по дополнительной памяти O(1), всё происходит сразу на месте.[1](https://habr.com/ru/company/edison/blog/495420/)
Сложность алгоритма O(*n*log*n*), при этом у пирамидальной сортировки нет особых случаем.
Любой массив будет обработан с одинаковой сложностью.


