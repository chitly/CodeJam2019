def list2str(l, deli=''):
    return deli.join([str(x) for x in l])

def set_bits(bits, st, lt, n_bit_check):
    for i in range(st, lt):
        if (i // n_bit_check) % 2 == 0:
            bits[i] = 0
        else:
            bits[i] = 1

def check_bits(bits, n_bits, n_bit_check):
    count_bits = 0
    error_list = []
    idx_range = 0

    for i in range(n_bits - 1):
        if bits[i] == bits[i + 1]:
            count_bits += 1
        else:
            if count_bits != n_bit_check - 1:
                error_list.append(idx_range)
            count_bits = 0
            idx_range += 1

    if n_bits % n_bit_check != 0:
        if count_bits >= n_bits % n_bit_check:
            if count_bits != n_bit_check - 1:
                error_list.append(idx_range)
            error_list.append(idx_range + 1)
        elif count_bits != (n_bits % n_bit_check) - 1:
            error_list.append(idx_range)
    
    return error_list

n_test_cases = int(input())
for t in range(n_test_cases):
    n, b, f = map(int, input().split())

    test_bits = [0 for i in range(n)]
    n_bit_check = 16
    error_list = []
    set_bits(test_bits, 0, n, n_bit_check)

    while n_bit_check > 0:
        print(list2str(test_bits))
        response_bits = [int(x) for x in input().strip()]

        if len(error_list) == 0:
            error_list = check_bits(response_bits, len(response_bits), n_bit_check)
        else:
            new_error_list = []
            for idx_error in error_list:
                # this part is still not correct
                tmp_bits = response_bits[n_bit_check * idx_error: n_bit_check * (idx_error +1)]
                tmp_error_list = check_bits(tmp_bits, len(tmp_bits), n_bit_check)
                for idx_tmp in tmp_error_list:
                    new_error_list.append(n_bit_check * idx_error + idx_tmp)
            error_list = new_error_list

        n_bit_check //= 2
        if n_bit_check == 0: break
        
        for idx_error in error_list:
            set_bits(test_bits, n_bit_check * idx_error, min(n, n_bit_check * (idx_error +1)), n_bit_check)
    
    print(list2str(error_list, ' '))