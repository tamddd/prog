class Solution {
public:
  int rob(vector<int>& nums) {
    int pre, cur = 0;
    for (int num : nums) {
      int tmp = pre;
      pre = cur;
      cur = max(cur, num + pre);
    }
    return cur;
  }
};
