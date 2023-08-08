class Solution {
    public enum RomanNumeral {
        I(1),
        IV(4),
        V(5),
        IX(9),
        X(10),
        XL(40),
        L(50),
        XC(90),
        C(100),
        CD(400),
        D(500),
        CM(900),
        M(1000);

        private final int value;

        RomanNumeral(int value) {
            this.value = value;
        }

        public int getValue() {
            return value;
        }
    }


    public int romanToInt(String romanNumeral) {
                int result = 0;
        int prevValue = 0;

        for (int i = romanNumeral.length() - 1; i >= 0; i--) {
            char currentChar = romanNumeral.charAt(i);
            RomanNumeral currentNumeral = RomanNumeral.valueOf(String.valueOf(currentChar));

            if (currentNumeral.getValue() < prevValue) {
                result -= currentNumeral.getValue();
            } else {
                result += currentNumeral.getValue();
            }

            prevValue = currentNumeral.getValue();
        }

        return result;
    }
}
