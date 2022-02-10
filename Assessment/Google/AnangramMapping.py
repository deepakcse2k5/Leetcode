
nums1 = [12,28,46,32,50]
nums2 = [50,12,32,46,28]

# print(nums1.index(12))


def anagramMapping(nums1, nums2):
    mapping = []
    # edge case
    if len(nums1) ==0:
        return []
    if len(nums1)==1:
        return [0]
    for i in range(len(nums1)):
        if nums1[i] in nums2:
            mapping.append(nums2.index(nums1[i]))
    return mapping

print(anagramMapping(nums1, nums2))
