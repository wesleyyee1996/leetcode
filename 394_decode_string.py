class Solution:
    def decodeString(self, s: str) -> str:
        
        # abc3[cd]xyz
        #        ^
        
        # nums = [1]
        # vars = ["abccdcdcd"]
        
        # 2 stacks
        # loop thru the string
        # if encounter a number, add to nums stack
        # if encounter 
        
        nums = [1]
        strings = [""]
        
        i = 0
        while i < len(s):
            if s[i].isdigit():
                curr_digit = ""
                while s[i].isnumeric():
                    curr_digit += s[i]
                    i += 1
                i -= 1
                nums.append(int(curr_digit))                
            elif s[i] == "[":
                strings.append("")
            elif s[i].isalpha():
                strings[-1] += s[i]
            elif s[i] == "]":
                mult = nums[-1]
                nums.pop(-1)
                mult_str = strings[-1]
                strings.pop(-1)
                add_str = mult*mult_str
                strings[-1] += add_str
            i += 1
                
        return strings[0]
                