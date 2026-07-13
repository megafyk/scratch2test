class Solution {
public:
    int reverse(int x) {
        if (x == INT_MAX || x == INT_MIN) {
            return 0;
        }
        int negative = 1;
        if (x < 0) {
            x = -x;
            negative = -1;
        }
        int reversed_x = 0;
        while (x > 0) {
            int d = x % 10;
            if(reversed_x > (INT_MAX-d) / 10) {
                return 0;
            }
            reversed_x = reversed_x * 10 + d;
            x /= 10;
        }
        std::cout << negative << std::endl;
        return negative * reversed_x;
    }
};
