import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    room_num = [0]*201
    start = ''
    end =''
    for i in range(N):
        A, B = map(int, input().split())
        if A < B:
            start = A
            end = B
        else:
            start = B
            end = A
        if start % 2 == 0 and end % 2 == 1:
            for i in range(start//2, end//2+2):
                room_num[i] += 1
        elif start % 2 == 0 and end % 2 == 0:
            for i in range(start//2, end//2+1):
                room_num[i] += 1
        elif start % 2 == 1 and end % 2 == 1:
            for i in range(start//2+1, end//2+2):
                room_num[i] += 1
        elif start % 2 == 1 and end % 2 == 0:
            for i in range(start//2+1, end//2+1):
                room_num[i] += 1

    print('#{} {}'.format(tc, max(room_num)))


