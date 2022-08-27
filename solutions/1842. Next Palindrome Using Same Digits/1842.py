class Solution:
  def nextPalindrome(self, num: str) -> str:
    def nextPermutation(nums: List[int]) -> bool:
      n = len(nums)

      # from back to front, find the first num < nums[i + 1]
      i = n - 2
      while i >= 0:
        if nums[i] < nums[i + 1]:
          break
        i -= 1

      if i < 0:
        return False

      # from back to front, find the first num > nums[i], swap it with nums[i]
      for j in range(n - 1, i, -1):
        if nums[j] > nums[i]:
          nums[i], nums[j] = nums[j], nums[i]
          break

      def reverse(nums, l, r):
        while l < r:
          nums[l], nums[r] = nums[r], nums[l]
          l += 1
          r -= 1

      # reverse nums[i + 1..n - 1]
      reverse(nums, i + 1, len(nums) - 1)
      return True

    n = len(num)
    A = [ord(num[i]) - ord('0') for i in range(len(num) // 2)]

    if not nextPermutation(A):
      return ''

    s = ''.join([chr(ord('0') + a) for a in A])
    if n & 1:
      return s + num[n // 2] + s[::-1]
    return s + s[::-1]
