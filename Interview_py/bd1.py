def most_freq(file_path):
    with open(file_path, 'r') as f:
         lines = f.readlines()
    the_list = [line.split() for line in lines]
    n = len(the_list)
    if n == 0: return 0, None
    cnt = dict()
    for i in range(n):
        cnt[the_list[i][2]] = cnt.get(the_list[i][2], 0) + 1

    max_cnt = 0
    max_value = None
    for key, value in cnt.items():
        if value > max_cnt:
            max_value = key 
            max_cnt = value

    return max_cnt, max_value


s = 'a-z'
s = 'abcdef' 
'acbcdef'
a - b - c 
c - d 
e - f

trie = ['abc', 'cd', 'ef']