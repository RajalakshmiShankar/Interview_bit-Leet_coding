class Solution(object):
    def plusOne(self, digits):

        results = int("".join(map(str, digits)))
        results=results+1

        answer=list(map(int, str(results)))
        
        return answer 
        