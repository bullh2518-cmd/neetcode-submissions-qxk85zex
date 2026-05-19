class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        for i in range(len(nums)):
            multiply = []

            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    multiply.append(nums[j])

            product = 1

            for num in multiply:
                product = product * num

            output.append(product)

        return output