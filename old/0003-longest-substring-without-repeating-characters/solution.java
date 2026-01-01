class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length();
        if (n == 0) {
            return 0;
        }

        int[] dp = new int[n];
        dp[0] = 1; // The first character is always part of the longest substring

        int maxLength = 1; // Initialize the maximum length to 1

        for (int i = 1; i < n; i++) {
            dp[i] = 1; // Initialize the current character as part of a new substring

            for (int j = i - 1; j >= i - dp[i - 1]; j--) {
                if (s.charAt(i) != s.charAt(j)) {
                    dp[i]++;
                } else {
                    break; // A repeating character is found, stop counting
                }
            }

            maxLength = Math.max(maxLength, dp[i]); // Update the maximum length
        }

        return maxLength;
    }

}
