if __name__ == "__main__":
    n = 6
    all_trips = ["beijing nanjing",
                "nanjing guangzhou",
                "guangzhou shanghai",
                "shanghai beijing",
                "fuzhou beijing",
                "beijing fuzhou"]
    res = 0
    trips = []
    for i in range(n):
        print(trips)
        cur_start, cur_end = all_trips[i].strip().split()
        if not trips:
            trips.append([cur_start, cur_end])
            continue
        for i, (start, end) in enumerate(trips):
            if cur_start == end and cur_end == start:
                trips.pop(i)
                res += 1
                break
            if cur_start == end:
                trips[i][1] = cur_end
                break
        else:
            trips.append([cur_start, cur_end])



    print(res)

[1,2,3,4].pop(2)


# if __name__ == "__main__":
#     n = int(input().strip())
#     res = 0
#     start = input().strip().split()[0]
#     for i in range(1, n):
#         cur_start, cur_end, *other= input().strip().split()
#         if start and cur_end == start:
#             res += 1
#             start = False
#         elif not start:
#             start = cur_start
#         else:
            

#     print(res)
