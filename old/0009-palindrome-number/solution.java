import java.util.ArrayList;
import java.util.Collections;

class Solution {
    public boolean isPalindrome(int x) {
        String number = Integer.toString(x);

        ArrayList<Character> stringNumber = new ArrayList<Character>();

        for (int i = 0; i < number.length(); i++) {
            stringNumber.add(number.charAt(i));
        }

        ArrayList<Character> reversedNumber = new ArrayList<Character>(stringNumber);
        Collections.reverse(reversedNumber);

        return stringNumber.equals(reversedNumber);
    }
}

