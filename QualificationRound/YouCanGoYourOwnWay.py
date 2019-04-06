n_test_cases = int(input())
for t in range(n_test_cases):
    n = int(input())
    rival_path = input().strip()
    if rival_path[0] == 'S' and rival_path[-1] == 'E':
        path = 'E' * (n - 1) + 'S' * (n - 1)
    elif rival_path[0] == 'E' and rival_path[-1] =='S':
        path = 'S' * (n - 1) + 'E' * (n - 1)
    elif rival_path[0] == 'S':
        count_e = 0
        for i in range(len(rival_path) - 1):
            if rival_path[i] == 'E': count_e += 1
            if rival_path[i] == 'E' and rival_path[i + 1] == 'E': break
        path = 'E' * count_e + 'S' * (n - 1) + 'E' * (n - count_e - 1)
    else:
        count_s = 0
        for i in range(len(rival_path) - 1):
            if rival_path[i] == 'S': count_s += 1
            if rival_path[i] == 'S' and rival_path[i + 1] == 'S': break
        path = 'S' * count_s + 'E' * (n - 1) + 'S' * (n - count_s - 1)
    print('Case #{}: {}'.format(t + 1, path))