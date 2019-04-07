from math import gcd
list2str = lambda l: ''.join([str(x) for x in l])

n_test_cases = int(input())
for t in range(n_test_cases):
    n, l = [int(x) for x in input().strip().split()]
    cipher_text = [int(x) for x in input().strip().split()]
    st_pos = 0
    for i in range(l - 1):
        if cipher_text[i] != cipher_text[i + 1]:
            st_pos = i
            break
    
    x = gcd(cipher_text[st_pos], cipher_text[st_pos + 1])
    pangrams_enc = [x]
    for i in range(st_pos, -1, -1):
        y = cipher_text[i] // x
        pangrams_enc.append(y)
        x = y
    pangrams_enc = pangrams_enc[::-1]
    
    x = pangrams_enc[-1]
    for i in range(st_pos, l - 1):
        y = cipher_text[i + 1] // x
        pangrams_enc.append(y)
        x = y
    
    pangrams_list = list(set(pangrams_enc))
    pangrams_list.sort()
    decoder = {}
    for i in range(len(pangrams_list)):
        decoder[pangrams_list[i]] = chr(ord('A') + i)
    pangrams_dec = []
    for pangram_enc in pangrams_enc:
        pangrams_dec.append(decoder[pangram_enc])
    print('Case #{}: {}'.format(t + 1, list2str(pangrams_dec)))