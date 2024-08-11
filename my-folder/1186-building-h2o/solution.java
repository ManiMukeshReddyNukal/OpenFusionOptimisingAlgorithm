class H2O {

    private final Semaphore hyd ;
    private final Semaphore oxy;
    private AtomicInteger noofhyd;

    public H2O() {
        hyd = new Semaphore(2);
        oxy = new Semaphore(1);
        noofhyd=new AtomicInteger(0);        
    }

    public void hydrogen(Runnable releaseHydrogen) throws InterruptedException {
        hyd.acquire();
        // releaseHydrogen.run() outputs "H". Do not change or remove this line.
        releaseHydrogen.run();
        noofhyd.incrementAndGet();
        if(noofhyd.get()==2){
            noofhyd.set(0);
            oxy.release();
        }
        
    }

    public void oxygen(Runnable releaseOxygen) throws InterruptedException {
        
        // releaseOxygen.run() outputs "O". Do not change or remove this line.
        oxy.acquire();
		releaseOxygen.run();
        hyd.release(2);
    }
}
