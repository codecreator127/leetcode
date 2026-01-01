class Solution {
    public int removeElement(int[] nums, int val) {
        int k = nums.length;
        ArrayList<Integer> temp = new ArrayList<Integer>();

        for (int i = 0; i < nums.length; i ++) {
            if (nums[i] == val) {
                nums[i] = 0;
                k -= 1;
            }
            else {
                temp.add(nums[i]);
            }
        }

        for (int i = 0; i < temp.size(); i++) {
            nums[i] = temp.get(i);
        }

        return k;

        

    }
}
