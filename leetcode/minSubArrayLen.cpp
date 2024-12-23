class Solution {
public:
    int minSubArrayLen(long long target, vector<int>& nums) {
	  const long long INF = 2 << 20;
	  long long tot = nums[0];
	  int slow = 0;
	  int res = INF;
	  if (tot >= target) res = 1;
	  int fast = 1;

	  while (fast < nums.size()){
		while (tot < target && fast < nums.size()){
		  tot += nums[fast++];
		}

		while (tot >= target && slow < fast){
		  res = min(res, fast - slow);
		  tot -= nums[slow++];
		}
	  }
	  return (res == INF) ? 0 : res;
    }
};
