class QueueBaB(object):
  """
  Klasa implementująca kolejkę za pomocą pythonowej listy tak,
  że początek kolejki jest przechowywany na początku listy.
  """
  
  def __init__(self):
    self.list_of_items = []
    
  def enqueue(self, item):
    """
    Metoda służąca do dodawania obiektu do kolejki.
    Pobiera jako argument obiekt który ma być dodany.
    Niczego nie zwraca.
    """
    self.list_of_items.append(item)
    
  def dequeue(self):
    """
    Metoda służąca do ściągania obiektu do kolejki.
    Nie pobiera argumentów.
    Zwraca ściągnięty obiekt.
    """
    return self.list_of_items.pop(0)
  
  def is_empty(self):
    """
    Metoda służąca do sprawdzania, czy kolejka jest pusta.
    Nie pobiera argumentów.
    Zwraca True jeśli kolejka jest pusta lub False gdy nie jest.
    """
    return len(self.list_of_items) == 0

    
  def size(self):
    """
    Metoda służąca do określania wielkości kolejki.
    Nie pobiera argumentów.
    Zwraca liczbę obiektów w kolejce.
    """
    return len(self.list_of_items)

  def __str__(self):
    """
    Metoda służąca do wypisania kolejki
    """
    return str(self.list_of_items)
      
    
  
class QueueBaE(object):
  """
  Klasa implementująca kolejkę za pomocą pythonowej listy tak,
  że początek kolejki jest przechowywany na końcu listy.
  """
  
  def __init__(self):
    self.list_of_items = []
    
  def enqueue(self, item):
    """
    Metoda służąca do dodawania obiektu do kolejki.
    Pobiera jako argument obiekt który ma być dodany.
    Niczego nie zwraca.
    """
    self.list_of_items.insert(0, item)
    
  def dequeue(self):
    """
    Metoda służąca do ściągania obiektu do kolejki.
    Nie pobiera argumentów.
    Zwraca ściągnięty obiekt.
    """
    return self.list_of_items.pop()
  
  def is_empty(self):
    """
    Metoda służąca do sprawdzania, czy kolejka jest pusta.
    Nie pobiera argumentów.
    Zwraca True jeśli kolejka jest pusta lub False gdy nie jest.
    """
    return len(self.list_of_items) == 0

    
  def size(self):
    """
    Metoda służąca do określania wielkości kolejki.
    Nie pobiera argumentów.
    Zwraca liczbę obiektów w kolejce.
    """
    return len(self.list_of_items)

  def __str__(self):
    """
    Metoda służąca do wypisania kolejki
    """
    return str(self.list_of_items)

if __name__ == "__main__":
  kolejka1 = QueueBaB()
  print(kolejka1.is_empty())
  for i in range(10):
    kolejka1.enqueue(i)
  print(kolejka1.dequeue())
  print(kolejka1)
  print(kolejka1.is_empty())
  print(kolejka1.size())

  kolejka2 = QueueBaE()
  print(kolejka2.is_empty())
  for i in range(10):
    kolejka2.enqueue(i)
  print(kolejka2.dequeue())
  print(kolejka2)
  print(kolejka2.is_empty())
  print(kolejka2.size())