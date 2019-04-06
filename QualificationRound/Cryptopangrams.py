from math import gcd
list2str = lambda l: ''.join([str(x) for x in l])

n_test_cases = int(input())
for t in range(n_test_cases):
    n, l = [int(x) for x in input().strip().split()]
    cipher_text = [int(x) for x in input().strip().split()]
    pangrams_enc = []
    for i in range(l - 1):
        x = gcd(cipher_text[i], cipher_text[i + 1])
        if i == 0: pangrams_enc.append(cipher_text[i] // x)
        pangrams_enc.append(x)
        if i == l - 2: pangrams_enc.append(cipher_text[i + 1] // x)
    pangrams_list = list(set(pangrams_enc))
    pangrams_list.sort()
    decoder = {}
    for i in range(len(pangrams_list)):
        decoder[pangrams_list[i]] = chr(ord('A') + i)
    pangrams_dec = []
    for pangram_enc in pangrams_enc:
        pangrams_dec.append(decoder[pangram_enc])
    print('Case #{}: {}'.format(t + 1, list2str(pangrams_dec)))