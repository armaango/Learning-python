n1 = int(raw_input())
nums1 = set(int(i) for i in(raw_input().strip().split()))
n2 = int(raw_input())
nums2 = set(int(j) for j in(raw_input().strip().split()))
s1 = nums1.difference(nums2).union(nums2.difference(nums1))
l1 = list(s1)
list.sort(l1)
for x in l1:
    print x