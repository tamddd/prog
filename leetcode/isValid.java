class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> map = Map.of(
            ')', '(',
            '}', '{',
            ']', '['
        );

        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            char nowChar = s.charAt(i);
            if (!stack.isEmpty() && map.containsKey(nowChar) && stack.peek() == map.get(nowChar)) {
                stack.pop();
            } else {
                stack.push(nowChar);
            }
        }

        return stack.isEmpty();
    }
}
