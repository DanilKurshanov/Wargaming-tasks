def heapSort(data: list) -> list:
    '''
    Пирамидальная сортировка массива
    :return: list
    '''
    # Формирование первоначального сортирующего дерева и нахождение максимального элемента
    n = len(data)

    for start in range(n // 2 - 1, -1, -1):
        heapSift(data, start, len(data) - 1)

    # Перенос максимального элемента в концен массива и восстановление сортирующего дерева
    for end in range(n-1, 0, -1):
        # Замена максимального элемента с последним элементом массива
        data[end], data[0] = data[0], data[end]

        heapSift(data, 0, end - 1)

    return data

# Отсеивание элементов для формирования девера по правилу: дочерние элементы меньше родительских
def heapSift(data, start, end):
    '''
    :param data: исходный массив
    :param start: родительский элемент подмассива
    :param end: размер исходного массива
    :return: None
    '''
    # Начало узла, с которого начинается отсеивание
    root = start

    while True:
        child = root * 2 + 1   # Левый потомок
        # Дочерний элемент за пределами подмассива
        if child > end:
            break
        # Определение наибольшего элемента между Левым и Правым потомком
        if child + 1 <= end and data[child] < data[child + 1]:
            child += 1
        # Замена корненго элемента с потомком при условии Родитель < Потомка
        if data[root] < data[child]:
            data[root], data[child] = data[child], data[root]
            root = child
        else:
            break