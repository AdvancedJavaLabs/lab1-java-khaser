package org.itmo;

import java.util.concurrent.atomic.*;

public class UnsafeCounter {
    private int counter;

    public void increment() {
        counter++; // <-- гонка данных
    }

    public int get() {
        return counter;
    }
}

// // Fixed version
// public class UnsafeCounter {
//     private final AtomicInteger counter = new AtomicInteger(0);
//
//     public void increment() {
//         counter.incrementAndGet();
//     }
//
//     public int get() {
//         return counter.get();
//     }
// }
