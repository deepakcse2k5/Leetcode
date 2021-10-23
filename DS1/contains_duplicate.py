nums = [1, 2, 3, 1]


def contains_duplicate(nums):
    for i in range(len(nums)):
        if nums[i] ^ nums[i + 1]:
            return False
        else:
            return True


print(contains_duplicate(nums))

print(1^2)
