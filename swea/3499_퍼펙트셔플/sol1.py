import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    n_list = list(map(str, input().split()))
    if len(n_list) % 2 == 0:
        n_list_left = n_list[:len(n_list)//2]
        n_list_right = n_list[len(n_list)//2:]
    else:
        n_list_left = n_list[:len(n_list)//2+1]
        n_list_right = n_list[len(n_list)//2+1:]

    x = 0
    print('#{}'.format(tc), end =' ')
    while x < len(n_list)//2:
        print(n_list_left[x], end=' ')
        print(n_list_right[x], end=' ')

        if x == len(n_list)//2-1 and len(n_list) % 2 ==1:
            print(n_list_left[x+1], end=' ')
            break
        x += 1
    print()