class Solution(object):
    def longestMountain(self, arr):
        n=len(arr)
        if n<3:
            return 0
        cnt=0
        r=1
        while r<n-1:
            if arr[r-1]<arr[r]>arr[r+1]:
                l=r-1
                while l>0 and arr[l]>arr[l-1]:
                    l-=1
                while r<n-1 and arr[r] > arr[r+1]:
                    r+=1
                cnt=max(cnt,r-l+1)
            else:
                r+=1
        
        return cnt
                


            

        
