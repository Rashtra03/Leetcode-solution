class Solution(object):
    def smallestSubsequence(self, s):
        """
        :type s: str
        :rtype: str
        """
        last ={}
        for i in range(len(s)):
            last[s[i]] = i
        
        stack =[]
        val = set()

        for i in range(len(s)):
            c = s[i]

            if c in val:
                continue

            while stack and stack[-1] > c and last[stack[-1]] > i:
                val.remove(stack.pop())

            stack.append(c)
            val.add(c)

        return "".join(stack)