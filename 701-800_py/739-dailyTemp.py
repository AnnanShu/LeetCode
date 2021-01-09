from collections import deque
class Solution:
    def dailyTempertures(self, T:list) -> list:
        T_index = list(zip(range(len(T)), T))
        dailyTemp = [0] * len(T)
        stack = deque()

        stack.append((0, 101))
        for tem_idx in T_index:
            while stack[-1][1] < tem_idx[1]:
                current = stack.pop()
                dailyTemp[current[0]] = tem_idx[0] - current[0]
            stack.append(tem_idx)

        return dailyTemp


Solution().dailyTempertures([73, 74, 75, 71, 69, 72, 76, 73])


