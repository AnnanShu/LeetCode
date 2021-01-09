n = input("please input the number")
all_list = []
for i in range(n):
    all_list.append(input(f"the {i}-th string is: "))
while True:
    cur = input("please enter current data (use space to split):")
    cur = cur.split(' ')
    print(all_list[int(cur[0])])
    print(all_list[int(cur[1])])