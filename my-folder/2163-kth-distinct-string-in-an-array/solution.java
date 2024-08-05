class Solution {
    public String kthDistinct(String[] arr, int k) {
        Set<String> distinctsets= new LinkedHashSet<>();
        Set<String> duplicateSets= new HashSet<>();
        // Set<String> duplicateSets = new HashSet<>();
        for (String st : arr){
            if (distinctsets.contains(st)){
                distinctsets.remove(st);
            }
            else if( !duplicateSets.contains(st)){
                distinctsets.add(st);
                duplicateSets.add(st);
            }
        }
        Iterator<String> iterator = distinctsets.iterator();
        while (k>1 && iterator.hasNext()){
            k-=1;
            iterator.next();
        }
        return iterator.hasNext() ? iterator.next() : "";
    }
}
