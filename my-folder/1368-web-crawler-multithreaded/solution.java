/**
 * // This is the HtmlParser's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface HtmlParser {
 *     public List<String> getUrls(String url) {}
 * }
 */
class Solution {
    public List<String> crawl(String startUrl, HtmlParser htmlParser) {
       String hostname= getHostName(startUrl);
       List<String> res = new ArrayList<>();
       Set<String> visited = new HashSet<>();
       BlockingQueue<String> q = new LinkedBlockingQueue<>();
       Deque<Future> dq = new ArrayDeque<>();
       q.offer(startUrl);
       ExecutorService executor = Executors.newFixedThreadPool(4, r->{
        Thread t = new Thread(r);
        t.setDaemon(true);
        return t;
       });

       while(true){
            String url = q.poll();
            if (url!=null){
                if (getHostName(url).equals(hostname) && !visited.contains(url)){
                    res.add(url);
                    visited.add(url);
                    dq.offerFirst(executor.submit(()->{
                        List<String> newUrls = htmlParser.getUrls(url);
                        for (String u :newUrls){
                            q.offer(u);
                        }
                    }));
                }
            }
            else{
                if (dq.isEmpty()){
                    break;
                }
                Future task = dq.poll();
                try{
                    task.get();
                }
                catch (InterruptedException | ExecutionException e) {}
            }
       }
       return res;
    }

    public String getHostName(String url){
        url=url.substring(7);
        String[] parts = url.split("/");
        return parts[0];
    }


    
}
