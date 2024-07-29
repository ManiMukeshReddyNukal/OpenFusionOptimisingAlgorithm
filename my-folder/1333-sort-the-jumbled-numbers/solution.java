class Solution {
    public int[] sortJumbled(int[] mapping, int[] nums) {
        ArrayList<Integer[]> storepair=new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            String number=Integer.toString(nums[i]);
            String formed="";
            for (int j = 0; j < number.length(); j++) {
                formed+=Integer.toString(mapping[number.charAt(j)-'0']);
            }
            int mappedvalue=Integer.parseInt(formed);
            storepair.add(new Integer[]{mappedvalue,i});
        }
        Collections.sort(storepair,(a,b)->a[0].compareTo(b[0]));
        int[] answer= new int[nums.length];
        for (int i = 0; i < answer.length; i++) {
            answer[i]=nums[storepair.get(i)[1]];
        }
        return answer;
    }
}
