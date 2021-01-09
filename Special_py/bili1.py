n, last = 3, 1
nums = [6, 5, 1]
cnt = 0
idx = last-1
while True:
    if nums[idx] > 0:
        nums[idx] -= 1
        cnt += 1
        if idx > 0:
            idx -= 1
        else:
            idx = n-1
    elif nums[idx] == 0:
        nums[idx] = cnt 
        break
print(" ".join([str(num) for num in nums]))