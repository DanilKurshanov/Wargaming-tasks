class CircularBufferV1:
    # Конструктор класса, реализующий циклический стек
    def __init__(self, size = 4):
        self.data = []
        self.size = size

    def push(self, elem):
        '''
        B.push(elem) -> добавляет элемент в начало стека
        При заполненом стеке удаляет самый старый элемент и заменят новым
        '''
        if len(self.data) < self.size:
            self.data.insert(0, elem)
        else:
            self.data.pop()
            self.data.insert(0, elem)

    def get(self):
        '''
        B.get() -> Возвращает самый "старый" элемент из стека
        Возвращает None если стек пустой
        '''
        if len(self.data) == 0:
            return None
        return self.data.pop()


class CircularBufferV2:
    # Конструктор класса, реализующий циклический стек
    # При создании экземпляа класса формируте пустой стек заполенный None
    def __init__(self, size = 4):
        self.start = 0 # Начало циклического стека - отображает самый "старый" элемент в стеке
        self.end = -1 # Конец циклического стека - отображает позицию для записи нового элемента в стек
        self.data = [None for _ in range(size)]
        self.size = size

    def push(self, elem):
        '''
        B.push(elem) -> добавляет элемент в стек
        При заполненом стеке удаляет самый старый элемент и заменят новым
        '''
        if None not in self.data:
            self.start = (self.start + 1) % self.size

        self.end = (self.end + 1) % self.size
        self.data[self.end] = elem


    def get(self):
        '''
        B.get() -> Возвращает самый "старый" элемент из стека
        Возвращает None если стек пустой
        '''
        removed, self.data[self.start] = self.data[self.start], None
        self.start = (self.start + 1) % self.size

        return removed