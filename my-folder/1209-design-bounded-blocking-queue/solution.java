import java.util.ArrayDeque;
import java.util.Deque;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.ReentrantLock;

public class BoundedBlockingQueue {

    private final Deque<Integer> dq = new ArrayDeque<>();
    private final int capacity;
    private final ReentrantLock lock = new ReentrantLock();
    private final Condition notFull = lock.newCondition();
    private final Condition notEmpty = lock.newCondition();

    public BoundedBlockingQueue(int capacity) {
        this.capacity = capacity;
    }

    public void enqueue(int element) throws InterruptedException {
        lock.lock();
        try {
            while (dq.size() == capacity) {  // Use while to re-check condition
                notFull.await(); 
            }
            dq.offer(element);
            notEmpty.signal(); // Signal after adding the element
        } finally {
            lock.unlock();
        }
    }

    public int dequeue() throws InterruptedException {
        lock.lock();
        try {
            while (dq.isEmpty()) {  // Use while to re-check condition
                notEmpty.await();
            }
            int element = dq.poll();
            notFull.signal(); // Signal after removing the element
            return element;
        } finally {
            lock.unlock();
        }
    }

    public int size() {
        lock.lock();
        try {
            return dq.size();
        } finally {
            lock.unlock();
        } 
    }
}

