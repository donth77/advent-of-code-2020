def hasTwoCandidates(arr, sum):
    seen = set()
    for i in range(0, len(arr)):
        temp = sum - arr[i]
        if temp in seen and not arr[i] == temp:
            return True
        seen.add(arr[i])
    return False


def subarraySum(arr, targetSum):
    currSum = arr[0]
    start = 0
    i = 1
    while i <= len(arr):
        while currSum > targetSum and start < i-1:
            currSum = currSum - arr[start]
            start += 1

        if currSum == targetSum:
            subarr = arr[start:i]
            return min(subarr) + max(subarr)

        if i < len(arr):
            currSum = currSum + arr[i]
        i += 1
    return None


preambleValue = 25
lineNum = 1
nums = []
part1Result = None
with open('input.txt') as fp:
    line = fp.readline()
    while line:
        nums.append(int(line))
        if lineNum > preambleValue:
            prevNums = nums[lineNum-preambleValue-1:lineNum - 1]
            isValid = hasTwoCandidates(prevNums, int(line))
            if not isValid and part1Result == None:
                part1Result = int(line)
                print(f'Part 1\n{part1Result}')
        line = fp.readline()
        lineNum = lineNum + 1

print(f'\nPart 2\n{subarraySum(nums, part1Result)}')
