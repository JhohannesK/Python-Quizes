def runner_up(arr, n):
    new = set(arr[:n])
    new_sorted = sorted(new, reverse=True)
    print(new_sorted[1])


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    runner_up(arr, n)
