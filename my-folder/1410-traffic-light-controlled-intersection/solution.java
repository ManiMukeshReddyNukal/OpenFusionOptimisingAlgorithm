class TrafficLight {

    AtomicInteger trafficSignal = new AtomicInteger(1); // 1 for road A, 2 for road B
    BlockingQueue<Integer> q = new LinkedBlockingQueue<>();
    ReentrantReadWriteLock lock = new ReentrantReadWriteLock();

    public TrafficLight() {
    }

    public void carArrived(
        int carId,           // ID of the car
        int roadId,          // ID of the road the car travels on. Can be 1 (road A) or 2 (road B)
        int direction,       // Direction of the car
        Runnable turnGreen,  // Use turnGreen.run() to turn light to green on current road
        Runnable crossCar    // Use crossCar.run() to make car cross the intersection 
    ) {
        synchronized(this){
            q.add(carId);

            while (q.peek() != carId) {
                try {
                    wait();
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt(); // Restore interrupted status
                }
            }

            if (trafficSignal.get() != roadId) {
                lock.writeLock().lock();
                try {
                    trafficSignal.set(roadId);
                    turnGreen.run();
                } finally {
                    lock.writeLock().unlock();
                }
            }

            crossCar.run();
            q.poll();
            notifyAll();
        }
    }
}

