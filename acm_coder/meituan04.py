# inputs = [[1,2],[2,2],[2, 3], [4, 3],[5, 4]]
# list_set = []
# list_set.append(set(inputs[0]))

# for d1, d2 in inputs:
#     for idx, cur_set in enumerate(list_set):
#         if d1 in cur_set or d2 in cur_set:
#             list_set[idx].add(d1)
#             list_set[idx].add(d2)
#             break
#     else:
#         list_set.append(set([d1, d2]))

# print(len(list_set))

# new_sets = [sorted(list(each)) for each in list_set]
# sorted_lists = sorted(new_set, key = lambda x: x[0])
# for 
inputs = []
n, m = list(map(int, input().strip().split()))
for i in range(m):
    inputs.append(list(map(int, input().strip().split())))
list_set = []
list_set.append(set(inputs[0]))

for d1, d2 in inputs[1:]:
    for idx, cur_set in enumerate(list_set):
        if d1 in cur_set or d2 in cur_set:
            list_set[idx].add(d1)
            list_set[idx].add(d2)
            break
    else:
        list_set.append(set([d1, d2]))

print(len(list_set))

new_sets = [sorted(list(each)) for each in list_set]
sorted_lists = sorted(new_sets, key = lambda x: x[0])
for each in sorted_lists:
    print(' '.join([str(i) for i in each]))
