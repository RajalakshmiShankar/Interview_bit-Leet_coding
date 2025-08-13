class Solution(object):
    def romanToInt(self, s):
        # Mapping of Roman numerals to integers
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        # Iterate from right to left
        for char in reversed(s):
            value = roman_map[char]
            if value < prev_value:
                total -= value  # Subtract if smaller than the previous value
            else:
                total += value  # Add if greater or equal
            prev_value = value
        
        return total
