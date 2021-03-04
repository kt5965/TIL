A = 'asdwfoecceocdfegwasssaa'
B = '#' + '#'.join(A) + '#'
cnt_list = [0] * len(A)
r = 0
p = 0
for i in range(1, len(A)):
    if i <= r:
        m_dix = 2 * p - i
