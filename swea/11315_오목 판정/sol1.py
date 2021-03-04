import sys
sys.stdin = open('input.txt')
T = int(input())

def right_o(A):
    right = 0
    left = 0
    for i in range(len(A)-4):
        for j in range(len(A)-4):
            if A[i][j] == 'o':
                right += 1
                count_r = 1
                while count_r < 5:
                    if A[i+count_r][j+count_r] == 'o':
                        right += 1
                        if right == 5:
                            return True
                    else:
                        right = 0
                        break
                    count_r += 1
            else:
                right = 0

    for i in range(len(A) - 4):
        for j in range(len(A)-1, 3, -1):
            if A[i][j] == 'o':
                left += 1
                count_l = 1
                while count_l < 5:
                    if A[i+count_l][j-count_l] == 'o':
                        left += 1
                        if left == 5:
                            return True
                    else:
                        left = 0
                        break
                    count_l += 1
            else:
                left = 0

    return False


for tc in range(1, T+1):
    N = int(input())
    omog = []
    for i in range(N):
        omog.append(list(input()))

    for i in range(len(omog)):
        count = 0
        for j in range(len(omog[i])):
            if omog[i][j] == 'o':
                count += 1
            elif omog[i][j] == '.':
                count = 0
            if count == 5:
                break
        if count == 5:
            break

    for i in range(len(omog)):
        count2 = 0
        for j in range(len(omog[i])):
            if omog[j][i] == 'o':
                count2 += 1
            elif omog[j][i] == '.':
                count2 = 0
            if count2 == 5:
                break
        if count2 == 5:
            break


    if count == 5 or count2 == 5 or right_o(omog) == True:
        print('#{} {}'.format(tc, 'YES'))
    else:
        print('#{} {}'.format(tc, 'NO'))


