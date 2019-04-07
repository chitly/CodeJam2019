def list2str(l, deli=''):
    return deli.join([str(x) for x in l])

def set_bits(bits, st, lt, n_bit_check):
    for i in range(st, lt):
        if (i // n_bit_check) % 2 == 0:
            bits[i] = 0
        else:
            bits[i] = 1

def check_bits(bits, n_bits, n_bit_check):
    # print('check_bits', list2str(bits), n_bits, n_bit_check)
    count_bits = 0
    error_list = []
    idx_range = 0
    st_range = 0

    if n_bit_check == 1:
        if n_bits == 2:
            if list2str(bits) == '0': return [1]
            elif list2str(bits) == '1': return [0]
            elif list2str(bits) == '': return [0, 1]
        elif n_bits == 1:
            if list2str(bits) == '': return [0]
        return []


    for i in range(len(bits) - 1):
        if bits[i] == bits[i + 1]:
            count_bits += 1
        else:
            if count_bits != n_bit_check - 1:
                error_list.append([idx_range, st_range, i + 1])
            count_bits = 0
            idx_range += 1
            st_range = i + 1

    if n_bits % n_bit_check != 0:
        if count_bits >= n_bits % n_bit_check:
            if count_bits != n_bit_check - 1:
                error_list.append([idx_range, st_range, len(bits)])
            error_list.append([idx_range + 1, len(bits), len(bits)])
        elif count_bits != (n_bits % n_bit_check) - 1:
            error_list.append([idx_range, st_range, len(bits)])
    else:
        if count_bits != n_bit_check - 1:
            error_list.append([idx_range, st_range, lt_range])
    
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
            error_list = check_bits(response_bits, n, n_bit_check)
        else:
            new_error_list = []
            for error in error_list:
                idx_range, st_range, lt_range = error
                if st_range != lt_range:
                    tmp_bits = response_bits[st_range: lt_range]
 
                    if n % (2 * n_bit_check) != 0 and idx_range == n // (2 * n_bit_check):
                        tmp_error_list = check_bits(tmp_bits, n % (2 * n_bit_check), n_bit_check)
                    else:
                        tmp_error_list = check_bits(tmp_bits, 2 * n_bit_check, n_bit_check)
 
                    if len(tmp_error_list) > 0 and isinstance(tmp_error_list[0], int):
                        for tmp_idx_range in tmp_error_list:
                            new_error_list.append(idx_range * 2 + tmp_idx_range)
                    else:
                        for tmp_error in tmp_error_list:
                            tmp_idx_range, tmp_st_range, tmp_lt_range = tmp_error
                            new_error_list.append([idx_range * 2 + tmp_idx_range, st_range + tmp_st_range, st_range + tmp_lt_range])
                # else:
                #     new_error_list.append([idx_range * 2, st_range, lt_range])
            error_list = new_error_list
        # print(error_list, n_bit_check)
        
        if n_bit_check == 1: break
        for error in error_list:
            idx_range, _, _ = error
            set_bits(test_bits, n_bit_check * idx_range, min(n, n_bit_check * (idx_range +1)), n_bit_check // 2)
        n_bit_check //= 2
    
    for i in range(n - (b - len(error_list)), n):
        error_list.append(i)
    print(list2str(error_list, ' '))