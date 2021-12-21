nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

# Задача №1 итератор
class FlatIterator():
    
    def __init__(self, nested_list):
        self.nested_list = nested_list
    
    def __iter__(self):
        self.start = 0
        self.cursor = 0
        return self

    def __next__(self): 
        # Обнуляем курсор каждый раз, когда доходим до последнего элемента вложенного списка
        # И переходим на следующий вложенный список
        if len(self.nested_list[self.start]) == self.cursor:
            self.start += 1
            self.cursor = 0
        if len(self.nested_list) == self.start:
            raise StopIteration
        item = nested_list[self.start][self.cursor]
        self.cursor += 1
        
        return item
        
print('#### Iterator print item result ####')
for item in FlatIterator(nested_list):
	print(item)

print('#### Iterator print list result ####')
flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)

# Задача №2 Генератор
def flat_generator(some_nested_list):
    start = 0
    end = len(some_nested_list)
    while start < end:
        for item in some_nested_list[start]:
            yield item
        start += 1

print('#### Generator print item result ####')
for item in flat_generator(nested_list):
    print(item)
