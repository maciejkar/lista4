"""
Rozważ sytuację z życia wziętą, np.: 
- auta w kolejce do myjni,
- kasy w supermarkecie,
- samoloty na pasie startowym, 
- okienko w banku. 
Postaw pytanie badawcze. Wykorzystując liniowe struktury danych 
zaprojektuj i przeprowadź symulację, która udzieli na nie odpowiedzi. 
Pamiętaj o określeniu wszystkich uproszczeń swojego modelu. 
"""

"""Ile  koszyków potrzeba, ustawianych w stos aby ich nie zabrakło w sklepie do którego przychodzi średnio 6 klientów na minutę a każdy z nich wybiera produkty od  2 minut do 30 minut 
a następnie stoi w kolejce która obsługuje średnio 8 klientów w minutę. Po skasowaniu produktów koszyk wraca na stos koszyków. 
Zakładamy że czas kasowania produktów nie zależy od czasu spędzonego na ich wybieraniu, a ilość klientów od pory dnia a czas otwarcia sklepu to 18 godzin """
import random
from L4_ZAD4 import Stack
from L4_ZAD1 import QueueBaE


class Client():
    def __init__(self):
        self.shopping_time = random.randint(1200, 18000)

    def get_shopping_time(self):
        return self.shopping_time

    def tick(self):
        self.shopping_time -= 1

class Cart(Stack):
    def __init__(self, number ):
        super().__init__()
        self.items = [ 1 for  n in range(number) ]


def symulation(time):
    cart = Cart(2000)
    queue = QueueBaE()
    clients = []
    amout_of_carts = []
    for tick in range(time):
        if random.randint(1, 10) == 10 :
            cart.pop()
            clients.append(Client())
        for client in clients:
            client.tick()
            if client.get_shopping_time() == 0 :
                queue.enqueue(client)
        clients = [client for client in clients if client.get_shopping_time() != 0]
        if queue.is_empty() == False and random.random() < 8/60  :
            queue.dequeue()
            cart.push(1)

        amout_of_carts.append(cart.size())
        
    return 2000 - min(amout_of_carts)

if __name__ == "__main__":
    time = 3600 *18
    amout_of_carts_req = symulation(time)
    for i in range(10):
        n = symulation(time) 
        if n > amout_of_carts_req:
            amout_of_carts_req = n    
    print(amout_of_carts_req)