import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;
import java.util.function.IntConsumer;

class FizzBuzz {
    private final int n;
    private int current = 1;
    private final Lock lock = new ReentrantLock();
    private final Condition condition = lock.newCondition();

    public FizzBuzz(int n) {
        this.n = n;
    }

    // printFizz.run() outputs "fizz".
    public void fizz(Runnable printFizz) throws InterruptedException {
        lock.lock();
        try {
            while (current <= n) {
                while (current <= n && (current % 3 != 0 || current % 5 == 0)) {
                    condition.await();
                }
                if (current > n) break;
                printFizz.run();
                current++;
                condition.signalAll();
            }
        } finally {
            lock.unlock();
        }
    }

    // printBuzz.run() outputs "buzz".
    public void buzz(Runnable printBuzz) throws InterruptedException {
        lock.lock();
        try {
            while (current <= n) {
                while (current <= n && (current % 3 == 0 || current % 5 != 0)) {
                    condition.await();
                }
                if (current > n) break;
                printBuzz.run();
                current++;
                condition.signalAll();
            }
        } finally {
            lock.unlock();
        }
    }

    // printFizzBuzz.run() outputs "fizzbuzz".
    public void fizzbuzz(Runnable printFizzBuzz) throws InterruptedException {
        lock.lock();
        try {
            while (current <= n) {
                while (current <= n && (current % 3 != 0 || current % 5 != 0)) {
                    condition.await();
                }
                if (current > n) break;
                printFizzBuzz.run();
                current++;
                condition.signalAll();
            }
        } finally {
            lock.unlock();
        }
    }

    // printNumber.accept(x) outputs "x", where x is an integer.
    public void number(IntConsumer printNumber) throws InterruptedException {
        lock.lock();
        try {
            while (current <= n) {
                while (current <= n && (current % 3 == 0 || current % 5 == 0)) {
                    condition.await();
                }
                if (current > n) break;
                printNumber.accept(current);
                current++;
                condition.signalAll();
            }
        } finally {
            lock.unlock();
        }
    }
}

