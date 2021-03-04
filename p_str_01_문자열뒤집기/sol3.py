word = 'edcba'

def reverse_word(a):
    if len(a) == 0:
        return a

    else:
        print(a[0], end = '')
        return reverse_word(a[1:])



print(reverse_word(word))