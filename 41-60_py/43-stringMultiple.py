class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0': return '0'
        ans = '0'
        m, n = len(num1), len(num2)
        for i in range(n-1, -1, -1):
            add = 0
            
    
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        ans, carry, i = '', 0, 0
        n1, n2 = len(num1), len(num2)
        while True:
            a1 = num1[i] if i < n1 else 0
            a2 = num2[i] if i < n2 else 0
            if not a1 and not a2 and not carry: break 
            cur = int(a1) + int(a2) + carry 
            ans += str(cur % 10)
            carry = cur // 10 
            i += 1
        return ans[::-1]