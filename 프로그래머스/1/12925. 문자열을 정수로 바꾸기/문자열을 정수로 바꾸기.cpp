#include <string>
using namespace std;

int solution(string s) {
    int result = 0;
    int sign = 1;
    int start = 0;
    
    // 첫번째 문자열에 대한 판단(음수인가 양수인가)
    if (s[0] == '-') { sign = -1; start = 1; }
    else if (s[0] == '+') { start = 1; }
    
    // 자릿수를 계속올려서 숫자를 조립
    for (int i = start; i < s.size(); i++) {
        // 문자를 숫자로 변환하는 방식
        result = result * 10 + (s[i] - '0');
    }

    return sign * result;
}