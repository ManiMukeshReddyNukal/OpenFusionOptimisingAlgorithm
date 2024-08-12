class ZeroEvenOdd {
    private int n;
    private ReentrantLock lock = new ReentrantLock();
    Condition zeroc=lock.newCondition();
    Condition evenc=lock.newCondition();
    Condition oddc=lock.newCondition();
    int currentNumber;
    int currentNumberToBePrinted;
    
    public ZeroEvenOdd(int n) {
        this.n = n;
        currentNumber=1;
        currentNumberToBePrinted=0;

    }

    // printNumber.accept(x) outputs "x", where x is an integer.
    public void zero(IntConsumer printNumber) throws InterruptedException {
        lock.lock();
        while (currentNumber<=n) {
            while(currentNumberToBePrinted!=0){
                zeroc.await();
            }
            if(currentNumber<=n){
                printNumber.accept(0);
            }
            currentNumberToBePrinted=currentNumber;
            if(currentNumber%2==0){
                evenc.signal();
            }
            else{
                oddc.signal();
            }
        }
        lock.unlock();
    }

    public void even(IntConsumer printNumber) throws InterruptedException {
        lock.lock();
        while (currentNumber<=n) {
            while(currentNumberToBePrinted==0 || currentNumberToBePrinted%2!=0){
                evenc.await();
            }
            if(currentNumber<=n){
                printNumber.accept(currentNumberToBePrinted);
            }
            currentNumberToBePrinted=0;
            currentNumber++;
            zeroc.signal();
        }

        lock.unlock();
    }

    public void odd(IntConsumer printNumber) throws InterruptedException {
        lock.lock();
        while (currentNumber<=n) {
            while(currentNumberToBePrinted==0 || currentNumberToBePrinted%2==0){
                oddc.await();
            }
            if(currentNumber<=n){
                printNumber.accept(currentNumberToBePrinted);
            }
            currentNumberToBePrinted=0;
            currentNumber++;
            zeroc.signal();
        }
        lock.unlock();
    }
}
