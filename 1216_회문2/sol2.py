import sys
from datetime import datetime
sys.stdin = open('a_test.txt')



def solution(s):
    list_pa = []
    for j in range(len(s)):
        for k in range(len(s)):
            if s[j:j+k+1] == s[j:j+k+1][::-1]:
                list_pa.append(len(s[j:j+k+1]))

    return max(list_pa)

T = int(input())
for tc in range(1, T+1):
    start = datetime.now()
    solution(input())
    end = datetime.now()
    print('#{} {}'.format(10 * 10**tc, end-start))