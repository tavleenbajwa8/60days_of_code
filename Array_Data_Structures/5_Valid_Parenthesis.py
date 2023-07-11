##Question 
"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 
Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false

"""

##Solution 1

class Solution:
    def isValid(self, s: str) -> bool:
            d = {"[":"]","{": "}","(":")"}  ## Made a dictionary containing mirror elements 
            for i in range(0,len(s),2):  ## Looping through even elements in an array with a step size of 2
                if s[i] in d:  ##Checking if those even elements are in the dict d as a key
                    if d[s[i]] != s[i + 1]:   ##Checking if the next element after every even element in string s matches the value of key (mirror image)
                        return False ##If the corresponding element do not match, means they are not the mirror image or is some other element, return False
                    return True ##Else return True
                
                
##Solution 2 
##The code uses a stack data structure to keep track of opening parentheses encountered while iterating through the string.
    def isValid2(self, s: str) -> bool:
        stack = []  #Initialize an empty stack to store opening parentheses
        for char in s:
            if char == '[' or char == '(' or char == '{':
                stack.append(char)  #If the character is an opening parenthesis ('[', '(', '{'), push it onto the stack
            
            #If the character is a closing parenthesis (']', ')', '}'), perform the following checks
            else:
                #If the stack is empty, it means there is no corresponding opening parenthesis for the current closing parenthesis, 
                #so the arrangement is invalid. Return False
                if not stack:
                    return False
                
                ##If the stack is not empty, compare the current closing parenthesis with the top element of the stack.
                ## #If the top of the stack matches the current closing parenthesis, it means the parentheses are properly balanced. 
                #Then, Pop the top element from the stack
                if char == ']' and stack[-1] == '[':
                    stack.pop() 
                elif char == ')' and stack[-1] == '(':
                    stack.pop()
                elif char == '}' and stack[-1] == '{':
                    stack.pop()
                
                ##If the top of the stack does not match the current closing parenthesis, it means the arrangement is invalid, Return False
                else:
                    return False
        ##After iterating through all characters in s, if the stack is empty, it means all opening parentheses have been matched and 
        ##canceled out by their corresponding closing parentheses. Return True, else return False
        
        return not stack  ## True if stack is empty [], else return False
 
    #Object Initialization
    obj = Solution()
    result1 = obj.isValid("()[]{}")
    result1_ = obj.isValid2("()[]{}")

    result2 = obj.isValid("()[]{}")
    result2_ = obj.isValid2("(([]{}")
    print(result1, result2)
    print(result2_, result2_)
