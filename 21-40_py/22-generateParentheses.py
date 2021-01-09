class Solution:
    def generateParenthesis(self, n: int):
        remaining = n-1
        stack = 1
        total_list = []
        list = ['(',]
        def auxiliary_func(remaining, stack, is_push, list):
            list = list.copy()
            if is_push:
                list.append('(')
                remaining -= 1
                stack += 1
                if stack > 0 and remaining > 0:
                    auxiliary_func(remaining, stack, is_push=True, list=list)
                    auxiliary_func(remaining, stack, is_push=False, list=list)

            else:
                list.append(')')
                stack -= 1
                if stack > 0 and remaining > 0:
                    auxiliary_func(remaining, stack, is_push=True, list=list)
                    auxiliary_func(remaining, stack, is_push=False, list=list)
                elif remaining > 0:
                    auxiliary_func(remaining, stack, is_push=True, list=list)

            if remaining == 0:
                for _ in range(stack):
                    list.append(')')
                str = ''.join(list)
                total_list.append(str)
                    # print(list)

        if remaining > 0:
            auxiliary_func(remaining, stack, is_push=True, list=list)
        auxiliary_func(remaining, stack, is_push=False, list=list)
        return total_list



print(Solution().generateParenthesis(3))


