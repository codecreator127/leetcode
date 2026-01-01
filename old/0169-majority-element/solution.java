class Solution {
    public int majorityElement(int[] nums) {
        Arrays.sort(nums);
        int current = nums[0];
        int count = 0;
        for (int i = 1; i < nums.length; i ++) {
            if (current != nums[i]) {
                current = nums[i];
                count = 0;
            }

            count ++;

            if (count >= Math.floor(nums.length/2)) {
                return current;
            }
        }

        return current;
    }
}
