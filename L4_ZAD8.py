"""
Zaprojektuj i przeprowadź eksperyment porównujący wydajność listy jednokierunkowej i listy wbudowanej w Pythona.
"""
from L4_ZAD5 import UnorderedList
import time
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

def time_add_to_list(kind_of_list, number_of_ele = 10000 ,repits = 30):
    times = []
    for n in range(repits):
        li = kind_of_list()
        start = time.time() 
        for i in range(number_of_ele):
            li.append(i)
        end = time.time() 
    times.append(end - start)
    return sum(times) / repits


def time_delate_from_list(kind_of_list, number_of_ele = 10000 ,repits = 30):
    times = []
    for n in range(repits):
        start = time.time()
        li = kind_of_list()
        for i in range(number_of_ele ):
            li.append(i)
        start = time.time()
        for i in range(number_of_ele):
            li.pop()
        end = time.time()
        times.append(end - start)
    return sum(times) / repits

if __name__ == "__main__":
    args = [100, 200, 300, 400]
    fig  = plt.subplots(figsize=(10, 4))
    G = gridspec.GridSpec(2, 1)
    ax1 = plt.subplot(G[0, 0])
    ax1.plot(args, [time_add_to_list(list, n) for n in args], label = "list" , marker = '.', linestyle = '--' )
    ax1.plot(args, [time_add_to_list(UnorderedList, n) for n in args], label = "UnorderedList" , marker = '.', linestyle = '--')
    ax1.set_title("Time of adding elements to list ")
    ax1.legend()
    ax1.set_xlabel("elements")
    ax1.set_ylabel("Time")
    ax2 = plt.subplot(G[1,:])
    ax2.plot(args, [time_delate_from_list(list, n) for n in args], label = "list" , marker = '.', linestyle = '--' )
    ax2.plot(args, [time_delate_from_list(UnorderedList, n) for n in args], label = "UnorderedList" , marker = '.', linestyle = '--')
    ax2.set_title("Time of removing elements from list")
    ax2.legend()
    ax2.set_xlabel("elements")
    ax2.set_ylabel("Time")
    plt.tight_layout()
    plt.show()