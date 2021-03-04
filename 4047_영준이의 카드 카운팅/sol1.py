import sys
sys.stdin = open('input.txt')
T = int(input())


def count_card(A):
    count_list = []
    card_list = []
    for i in range(len(A)):
        if i % 3 == 1:
            count_list.append(A[i] + A[i + 1])

    for i in range(len(A)):
        if i % 3 == 0:
            card_list.append(A[i])

    for j in range(len(count_list)):
        for k in range(len(count_list)):
            if j != k and count_list[j] == count_list[k]:
                if card_list[j] == card_list[k]:
                    return False

    return True


for tc in range(1, T+1):
    card = input()
    count = 0
    dict_card = {}
    dict_card['S'] = 0
    dict_card['D'] = 0
    dict_card['H'] = 0
    dict_card['C'] = 0
    while count < (len(card)):
        if card[count] == 'S':
            dict_card['S'] += 1
            count += 3
        elif card[count] == 'D':
            dict_card['D'] += 1
            count += 3
        elif card[count] == 'H':
            dict_card['H'] += 1
            count += 3
        elif card[count] == 'C':
            dict_card['C'] += 1
            count += 3



    if count_card(card) == True:
        print("#{} {} {} {} {}".format(tc, 13 - dict_card['S'], 13 - dict_card['D'], 13 - dict_card['H'], 13 - dict_card['C']))
    else:
        print("#{} {}".format(tc, 'ERROR'))