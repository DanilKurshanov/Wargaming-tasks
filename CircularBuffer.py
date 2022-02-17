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