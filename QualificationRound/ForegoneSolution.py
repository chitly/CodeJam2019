n_test_cases = int(input())
list2str = lambda l: ''.join([str(x) for x in l])
for t in range(n_test_cases):
    n = [int(x) for x in input().strip()]
    a, b = [], []
    last_idx_a, last_idx_b = 0, 0
    carry = False
    for i in range(len(n) - 1, -1, -1):
        if carry and n[i] != 0:
            n[i] -= 1
            carry = False
        elif carry:
            n[i] = 9

        for j in range(0, 10):
            if j == 4: continue
            if n[i] - j >= 0 and n[i] - j != 4:
                a.append(j)
                b.append(n[i] - j)
                if j != 0: last_idx_a = len(a)
                if n[i] - j != 0: last_idx_b = len(b)
                break
            elif n[i] - j < 0 and n[i] + 10 - j != 4:
                a.append(j)
                b.append(n[i] + 10 - j)
                carry = True
                if j != 0: last_idx_a = len(a)
                if n[i] + 10 - j != 0: last_idx_b = len(b)
                break
    a = a[:last_idx_a][::-1]
    b = b[:last_idx_b][::-1]
    print('Case #{}: {} {}'.format(t + 1, list2str(a), list2str(b)))