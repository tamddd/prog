class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
	  int left = 0;
	  int total = 0;
      const int init = 1001001001;
	  int res = init;

	  for (int right = 0; right < nums.size(); right++){
		total += nums[right];

		while (target <= total) {
			res = min(res, right - left + 1);
			total -= nums[left++];
		  }
	  }
	  if (res == init) {
		  return 0;
		}
	  return res;
    }
};
