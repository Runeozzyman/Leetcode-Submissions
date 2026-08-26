class Solution {
    public int singleNumber(int[] nums) {
        
        int uniqueNum = 0;

        for(int i=0; i<nums.length; i++){
            uniqueNum ^= nums[i];
        }

        return uniqueNum;

    }
}