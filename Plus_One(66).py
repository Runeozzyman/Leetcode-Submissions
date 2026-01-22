class Solution(object):
    def plusOne(self, digits):

        end = len(digits)-1

        for i in range(len(digits)):
            if digits[end] != 9:
                digits[end] += 1
                return digits
            
            else:
                digits[end] = 0
                end -= 1
            
        return [1] + digits