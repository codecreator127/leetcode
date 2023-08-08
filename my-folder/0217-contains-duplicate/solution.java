class Solution {

    public boolean containsDuplicate(int[] nums) {
        // HashMap<Integer, Integer> seen = new HashMap<>();
        // for (int num: nums) {
        //     if (seen.containsKey(num) && seen.get(num) >= 1) {
        //         return true;
        //     }
        //     seen.put(num, seen.getOrDefault(num, 0) + 1);
        // }
        // return false;

        Arrays.sort(nums);

        for (int i = 1; i < nums.length; i ++) {
            if (nums[i] == nums[i - 1]) {
                return true;
            }
        }
        return false;

    }
}
