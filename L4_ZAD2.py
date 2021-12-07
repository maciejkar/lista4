"""
 Zaprojektuj i przeprowadź eksperyment porównujący wydajność implementacji kolejek QueueBaB i QueueBaE.
"""
from L4_ZAD1 import QueueBaE, QueueBaB
import time
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import copy

def time_add_to_queue(kind_of_queue, number_of_ele = 10000 ,repits = 30):
    times = []
    for n in range(repits):
        queue = kind_of_queue()
        start = time.time() 
        for i in range(number_of_ele):
            queue.enqueue(i)
        end = time.time() 
    times.append(end - start)
    return sum(times) / repits

def time_delate_from_queue(kind_of_queue, number_of_ele = 10000 ,repits = 30):
    times = []
    queue = kind_of_queue()
    for i in range(number_of_ele ):
        queue.enqueue(i)
    for n in range(repits):
        nowa_queue = copy.deepcopy(queue)
        start = time.time()
        for i in range(number_of_ele):
            nowa_queue.dequeue()
        end = time.time()
    times.append(end - start)
    return sum(times) / repits

def time_delate_from_and_add_queue(kind_of_queue, number_of_ele = 10000 ,repits = 30):
    times = []
    for n in range(repits):
        start = time.time()
        queue = kind_of_queue()
        for i in range(number_of_ele):
            queue.enqueue(i)
        for i in range(number_of_ele):
            queue.dequeue()
        end = time.time()
        times.append(end - start)
    return sum(times) / repits

if __name__ == "__main__":
    args = [100, 1000,2500, 5000, 7500, 10000]
    fig  = plt.subplots(figsize=(10, 4))
    G = gridspec.GridSpec(2, 2)
    ax1 = plt.subplot(G[0, 0])
    ax1.plot(args, [time_add_to_queue(QueueBaB, n) for n in args], label = "QueueBaB" , marker = '.', linestyle = '--' )
    ax1.plot(args, [time_add_to_queue(QueueBaE, n) for n in args], label = "QueueBaE" , marker = '.', linestyle = '--')
    ax1.set_title("Time of adding elements to queue ")
    ax1.legend()
    ax1.set_xlabel("elements")
    ax1.set_ylabel("Time")
    ax2 = plt.subplot(G[0,1])
    ax2.plot(args, [time_delate_from_queue(QueueBaB, n) for n in args], label = "QueueBaB" , marker = '.', linestyle = '--' )
    ax2.plot(args, [time_delate_from_queue(QueueBaE, n) for n in args], label = "QueueBaE" , marker = '.', linestyle = '--')
    ax2.set_title("Time of removing elements from queue")
    ax2.legend()
    ax2.set_xlabel("elements")
    ax2.set_ylabel("Time")
    ax3 = plt.subplot(G[1,:])
    ax3.plot(args, [time_delate_from_and_add_queue(QueueBaB, n) for n in args], label = "QueueBaB" , marker = '.', linestyle = '--' )
    ax3.plot(args, [time_delate_from_and_add_queue(QueueBaE, n) for n in args], label = "QueueBaE" , marker = '.', linestyle = '--')
    ax3.set_title("Time of adding and removing elements from queue")
    ax3.legend()
    ax3.set_xlabel("elements")
    ax3.set_ylabel("Time")
    plt.tight_layout()
    plt.show()

# Wniosek kolejka mająca początek na początku listy szybciej dodaje elementy do kolejki ale wolniej usuwa
#  przez co sumarycznie jest wolniejsza gdy dodjemy do kolejki a następnie będziemy usuwać z niej wszystkie elementy 