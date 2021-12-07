
class Node:
  
  def __init__(self,init_data):
    self.data = init_data
    self.next = None
  
  def get_data(self):
    return self.data

  def get_next(self):
    return self.next
  
  def set_data(self,new_data):
    self.data = new_data
  
  def set_next(self,new_next):
    self.next = new_next
  
  def __str__(self) :
      return str(self.data)

class UnorderedList(object):
  
  def __init__(self):
    self.head = None
    self.lenght = 0

  def is_empty(self):
    return self.head == None

  def add(self, item):
    temp = Node(item)
    temp.set_next(self.head)
    self.head = temp
    self.lenght += 1

  def size(self):
    return self.lenght
    
  def search(self,item):
    current = self.head
    found = False
    while current != None and not found:
      if current.get_data() == item:
        found = True
      else:
        current = current.get_next()
    return found

  def remove(self, item):
    current = self.head
    previous = None
    found = False
    while not found:
        if current.get_data() == item:
            found = True
        else:
            previous = current
            current = current.get_next()
            if current == None:
                return 

    if previous == None:                  #jeśli usuwamy pierwszy element
        self.head = current.get_next()
    else:
        previous.set_next(current.get_next())

    self.lenght -= 1
      
  def append(self, item):
    """
    Metoda dodająca element na koniec listy.
    Przyjmuje jako argument obiekt, który ma zostać dodany.
    Niczego nie zwraca.
    """
    self.insert(-1,item)
    
  def index(self, item):
    """
    Metoda podaje miejsce na liście, 
    na którym znajduje się określony element - 
    element pod self.head ma indeks 0.
    Przyjmuje jako argument element, 
    którego pozycja ma zostać określona.
    Zwraca pozycję elementu na liście lub None w przypadku, 
    gdy wskazanego elementu na liście nie ma.
    """
    current = self.head
    for n in range(0,self.lenght):
      if current.get_data() == item:
        return n
      else:
        current = current.get_next()

    
  def insert(self, pos, item):
    """
    Metoda umieszcza na wskazanej pozycji zadany element.
    Przyjmuje jako argumenty pozycję, 
    na której ma umiescić element oraz ten element.
    Niczego nie zwraca.
    Rzuca wyjątkiem IndexError w przypadku, 
    gdy nie jest możliwe umieszczenie elementu
    na zadanej pozycji (np. na 5. miejsce w 3-elementowej liście).
    """
    if pos < 0 :
      pos = self.lenght + pos + 1

    if pos > self.lenght or pos < 0:
      raise IndexError("This index don't exist")

    current = self.head
    for n in range(pos -1):
      current = current.get_next()
    if pos == 0 :
      self.head = Node(item)
      self.head.set_next(current)
    else:
      temp = Node(item)
      temp.set_next(current.get_next())
      current.set_next(temp)
    self.lenght += 1
    
  
  def pop(self, pos=-1):
    """
    Metoda usuwa z listy element na zadaniej pozycji.
    Przyjmuje jako opcjonalny argument pozycję, 
    z której ma zostać usunięty element.
    Jeśli pozycja nie zostanie podana, 
    metoda usuwa (odłącza) ostatni element z listy. 
    Zwraca wartość usuniętego elementu.
    Rzuca wyjątkiem IndexError w przypadku,
    gdy usunięcie elementu z danej pozycji jest niemożliwe.
    """
    if self.lenght == 0:
      raise IndexError("List is empty!")
    if pos < 0 :
      pos = self.lenght + pos + 1

    if pos > self.lenght or pos < 0:
      raise IndexError("This index don't exist")

    current = self.head
    previous = None
    for n in range(pos - 1):
      previous = current
      current = current.get_next()
    
    if pos == 0 or self.lenght == 1:
      self.head = current.get_next()
    else:
      previous.set_next(current.get_next())
    
    self.lenght -= 1
    return current.get_data()

  def __str__(self):
    current = self.head
    li = []
    while current != None:
      li.append(current.get_data())
      current = current.get_next()
    s = ("[" + ', '.join(['{}']*len(li))+"]") 
    return s.format(*li)
  
  def __getitem__(self, pos):
    if pos < 0 :
      pos = self.lenght + pos 

    if pos > self.lenght or pos < 0:
      raise IndexError("This index don't exist")
    
    current = self.head
    for n in range(pos):
      current = current.get_next()
           
    return current.get_data()



if __name__ == "__main__":
  lista = UnorderedList()
  lista.add(1)
  lista.add(2)
  lista.add(5)
  print(lista.search("c"))
  print(lista)
  lista.add(7)
  print(lista)
  print(lista.index(5))
  lista.insert(1,10)
  print(lista)
  print(lista.pop(3))
  print(lista)
  lista2 = UnorderedList()
  print(lista2.index(1))
  lista2.append(11)
  print(lista2)
  lista.append(13)
  print(lista)
  print(lista[1])
  lista2.pop()
  print(lista2)
  lista2.append(11)
  print(lista2[0])
  