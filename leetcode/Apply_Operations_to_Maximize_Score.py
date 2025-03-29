class Solution(object):
    def maximumScore(self, nums, k):
        def prime(n):
            factors=set()
            while n%2==0:
                factors.add(2)
                n=n/2
            
            for i in range(3,int(math.sqrt(n))+1,2):
                while n%i==0:
                    factors.add(i)
                    n=n/i
            if n>2:
                factors.add(n)
            
            return len(factors)
        
        prime_score = [prime(n) for n in nums]
        MOD = 10**9+7
        s = []

        n=len(nums)
        # check the left
        left = [0] * n
        stack = []
        for i in range(n):
            while stack and prime_score[stack[-1]] < prime_score[i]:
                stack.pop()
            left[i] = stack[-1] + 1 if stack else 0
            stack.append(i)
        # check the right
        right = [0] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and prime_score[stack[-1]] <= prime_score[i]:
                stack.pop()
            right[i] = stack[-1] - 1 if stack else n-1
            stack.append(i)
        
        for i in range(n):
            c_count = (i-left[i]+1)*(right[i]-i+1)
            s.append((nums[i],c_count))
        
        s.sort(key=lambda x:-x[0])

        result = 1
        opl = k
        for val , cnt in s:
            opu = min(cnt,opl)
            result=(result*pow(val,opu,MOD))%MOD
            opl-=opu
            if opl == 0:
                break
        return result
        





        
