#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np

def main():
    vertices = [10, 100, 1000, 10000, 10000, 50000, 100000, 1000000, 2000000]
    connections = [50, 500, 5000, 50000, 100000, 1000000, 1000000, 10000000, 10000000]
    serial_times = [1, 1, 2, 13, 11, 44, 51, 1038, 1688]
    parallel_times = [5, 4, 11, 20, 14, 53, 53, 751, 1103]

    plt.figure(figsize=(14, 8))

    plt.plot(vertices, serial_times, 'ro-', linewidth=2, markersize=8, label='Последовательная версия', markerfacecolor='red')
    plt.plot(vertices, parallel_times, 'bo-', linewidth=2, markersize=8, label='Параллельная версия', markerfacecolor='blue')

    plt.xlabel('Количество вершин', fontsize=12)
    plt.ylabel('Время выполнения (мс)', fontsize=12)
    plt.title('Зависимость времени выполнения алгоритма от объема данных', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=12)

    for i, (v, c, s, p) in enumerate(zip(vertices, connections, serial_times, parallel_times)):
        plt.annotate(f'{c} соедин.', (v, max(s, p)), textcoords="offset points", 
                     xytext=(0,15), ha='center', fontsize=9, alpha=0.7)

    plt.yscale('log')
    plt.xscale('log')

    plt.grid(True, which='both', alpha=0.2)

    plt.tight_layout()
    plt.savefig('single-vs-multithread.png', dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    main()
