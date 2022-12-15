A="vwgwngkwnrrvrvn"
#Создаем класс функций для создания и заполнения хеш таблицы
class HashLinearProbe:
    def __init__(self): #Функция для создания пустой хеш таблицы
        self.hashtable_size = len(A)
        self.hashtable = [0] * self.hashtable_size

    def hashcode(self, key): #создает ключ для элементов
        return (2*key+5) % self.hashtable_size

    def lprobe(self, element): #избавление от коллизий
        i = self.hashcode(element)
        j = 0
        while self.hashtable[(i+j) % self.hashtable_size] != 0:
            if (i+j) > self.hashtable_size:
                self._doublesize()           
            j = j + 1
        return (i + j) % self.hashtable_size    
            

    def insert(self, element): #заполняет хеш таблицу
        i = self.hashcode(element)
        if self.hashtable[i] == 0:            
            self.hashtable[i] = A[element]
        else:
            i = self.lprobe(element)           
            self.hashtable[i] = A[element]

  

    def display(self): #выводит хеш таблицу в консоль
        
        print(self.hashtable)

HC = HashLinearProbe()
for i in range(len(A)):
    HC.insert(i)
HC.display()

