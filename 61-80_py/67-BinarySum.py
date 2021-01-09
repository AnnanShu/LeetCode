class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a)>len(b):
            b = '0' * (len(a) - len(b)) + b
        elif len(a) < len(b):
            a = '0' * (len(b) - len(a)) + a
        a_rev = a[::-1]
        b_rev = b[::-1]
        carry = 0
        output = []
        for i in range(len(a)):
            current_bit = int(a_rev[i]) + int(b_rev[i]) + carry
            if current_bit > 1:
                carry = 1
                output.append(str(current_bit - 2))
            else:
                carry = 0
                output.append(str(current_bit))

        if carry:
            output.append(str(carry))

        output = output[::-1]
        output = ''.join(output)
        return output

a = "10100"
b = "01011"
Solution().addBinary(a, b)
b[::-1]
a[::-1]
