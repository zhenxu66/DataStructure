# 349


import collections
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1).intersection(nums2))


# 350  (JAVA, treeset, treemap, hashset, hashmap, logn time constraint
class Solution2:
    def intersect(self, nums1, nums2):
        return list((collections.Counter(nums1) & collections.Counter(nums2)).elements())


if __name__ == '__main__':

    res = Solution2();
    print(res.intersect([4,9,5],[9,4,9,8,4]));
    print(res.intersect([2,2], [1, 2, 2, 1]));
