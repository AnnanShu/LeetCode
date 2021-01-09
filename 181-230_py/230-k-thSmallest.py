class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def gen(r):
            if r is not None:
                yield from gen(r.left)
                yield r.val
                yield from gen(r.right)
        
        it = gen(root)
        for _ in range(k):
            ans = next(it)
        return ans
    
import random 
for _ in range(100):
    print(random.randint(0, 5))

    'a'.isalpha()

"/" + "/".join(["a", "b"])

16  ^ 15