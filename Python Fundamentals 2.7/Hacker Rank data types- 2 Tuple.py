num = int(raw_input())
nums = tuple(int(i) for i in(raw_input().strip().split()))
print hash(nums)