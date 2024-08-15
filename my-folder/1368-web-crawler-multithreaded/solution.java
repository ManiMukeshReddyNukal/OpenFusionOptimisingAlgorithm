/**
 * // This is the HtmlParser's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface HtmlParser {
 *     public List<String> getUrls(String url) {}
 * }
 */
class Solution {
    public List<String> crawl(String startUrl, HtmlParser htmlParser) {

        String hostname = getHostname(startUrl);
        Set<String> set = ConcurrentHashMap.newKeySet();
        set.add(startUrl);
        
        ExecutorService executor = Executors.newCachedThreadPool();
        
        UrlCallable task = new UrlCallable(startUrl, htmlParser, set, hostname, executor);
        Future future = executor.submit(task);
        
        try {
            future.get();
        } catch (InterruptedException | ExecutionException e) {
            e.printStackTrace();
        }
        
        executor.shutdown();
        return new ArrayList(set);
    }
    
    private String getHostname(String url) {
        int idx = url.indexOf('/', 7);
        return (idx != -1) ? url.substring(0, idx) : url;
    }
}

class UrlCallable implements Callable<Void>{
    private String inputUrl;
    private HtmlParser htmlParser;
    private Set<String> set;
    private String hostName;
    private ExecutorService executorService;

        public UrlCallable(String inputUrl, HtmlParser htmlParser, Set<String> set, String hostName, ExecutorService executorService){
        this.inputUrl=inputUrl;
        this.htmlParser=htmlParser;
        this.set=set;
        this.hostName=hostName;
        this.executorService=executorService;
    }

    public boolean isSameHost(String url, String hostName){
        if(!url.startsWith(hostName)){
            return false;
        }
        return url.length()==hostName.length() || url.charAt(hostName.length())=='/';
    }

    @Override
    public Void call(){
        List<Future> futures = new ArrayList<>();
        htmlParser.getUrls(inputUrl).parallelStream().filter(url-> isSameHost(url,hostName)).filter(url->set.add(url))
        .forEach(url-> {
            UrlCallable task = new UrlCallable(url,htmlParser,set,hostName,executorService);
            Future future = executorService.submit(task);
            futures.add(future);
        });
        futures.forEach(future -> {
            try{ future.get();
            }
            catch(Exception e){
                e.printStackTrace();
            }
        });
        return null;
    }
}
