#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np

def main():
    nthreads = [2, 4, 8, 16]
    times = [1370, 1288, 1304, 1290]

    plt.figure(figsize=(14, 8))

    plt.plot(nthreads, times, 'ro-', linewidth=2, markersize=8, markerfacecolor='red')

    plt.xlabel('ForkPoolJoin parallelism', fontsize=12)
    plt.ylabel('Время выполнения (мс)', fontsize=12)
    plt.title('2e6 vertices and 1e7 connections', fontsize=14)
    plt.grid(True, alpha=0.3)

    # plt.yscale('log')
    # plt.xscale('log')

    plt.grid(True, which='both', alpha=0.2)

    plt.tight_layout()
    plt.savefig('n-threads.png', dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    main()
