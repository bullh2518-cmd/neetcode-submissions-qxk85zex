class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        Left = 0
        Right = Left + 1
        
        while Left < Right:
            if numbers[Left] + numbers[Right] == target:
                return [Left + 1, Right + 1]
            else:
                Right += 1
                
                if Right == len(numbers):
                    Left +=1
                    Right = Left + 1
