class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        long long res = 0;
        for (int i = 0; i < 32; i++){
            res *= 2;
            res += n & 1;
            n >>= 1;
        }
        return res;
    }
};
