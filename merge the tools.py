def merge_the_tools(string, k):
    lst = [string[i:i + k] for i in range(0, len(string), k)]

    for j in lst:
        new_list = ''
        for k in j:
            if k not in new_list:
                new_list += k
            else:
                continue
        print(new_list)

if __name__ == '__main__':
    # string, k = input(), int(input())
    merge_the_tools('AABCAAADAAXDAXSDXASXADXSAXDWSAXDSWAXA', 3)
