#include <string>
using namespace std;

int solution(string s) {
    int result = 0;
    int sign = 1;
    int start = 0;

    if (s[0] == '-') { sign = -1; start = 1; }
    else if (s[0] == '+') { start = 1; }

    for (int i = start; i < s.size(); i++) {
        result = result * 10 + (s[i] - '0');
    }

    return sign * result;
}