class Solution {
    public int findJudge(int n, int[][] trust) {
        if (trust.length<n-1)
        {
            return -1;
        }
        int[] network= new int[n+1];
        for (int[] edge: trust){
            network[edge[0]]--;
            network[edge[1]]++;
        }
        for (int i=1;i<n+1;i++)
        {
            if (network[i]==n-1)
            {
                return i;
            }
        }
        return -1;
    }
}
