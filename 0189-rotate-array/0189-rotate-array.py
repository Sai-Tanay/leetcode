class Solution:
    def rev(self,nums,i,j):
        while i<j:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1
    def rotate(self, nums: list[int], k: int) -> None:
        n=len(nums)
        k=k%n
        self.rev(nums, 0, n - 1)
        self.rev(nums, 0, k - 1)
        self.rev(nums, k, n - 1)
        
       
       