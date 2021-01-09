from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [-1, ]
        for each in asteroids:
            print(stack)
            if each < 0:
                if stack[-1] < 0:
                    stack.append(each)
                else:
                    while stack[-1] > 0:
                        print(each, stack)
                        if stack[-1] + each < 0:
                            stack.pop()
                            # stack.append(each)
                        elif stack[-1] + each == 0:
                            stack.pop()
                            break 
                        else:
                            break
                    if stack[-1] < 0:
                        stack.append(each)

            else:
                stack.append(each)
        
        return stack[1:]


Solution().asteroidCollision([10, 2, -5])