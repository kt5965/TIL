import sys
sys.stdin = open('test.txt')

def manacher(s):
    s = '#' + '#'.join(s) + '#'
    N = len(s)
    cnt_list = [0] * N
    r = p = 0
    for idx in range(N):
        if idx <= r:
            m_idx = 2 * p - idx
            if cnt_list[m_idx] > r - idx:
                cnt_list[idx] = r - idx
            else:
                cnt_list[idx] = cnt_list[m_idx]
        else:
            m_idx = 0
        while idx - cnt_list[idx] - 1 >= 0 and idx + cnt_list[idx] + 1 < N and\
                s[idx - cnt_list[idx] - 1] == s[idx + cnt_list[idx] + 1]:
            cnt_list[idx] += 1
        if r < idx + cnt_list[idx]:
            r = idx + cnt_list[idx]
            p = idx
    return max(cnt_list)

T = int(input())
for tc in range(1, T+1):
    print(manacher(input()))

