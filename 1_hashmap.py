def two_sum(nums, target):

    num_map = {}

    for i, num in enumerate(nums):

        complete = target - num
        
        if complete in num_map:

            print(num_map[complete], i)

        num_map[num] = i

    return []


nums = list(map(int, input().split()))
target = int(input())
two_sum(nums, target)


