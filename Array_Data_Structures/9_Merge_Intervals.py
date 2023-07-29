##Question: 
"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
"""

##Function Definition
def merge_intervals(intervals):
    
    ##Sort the intervals first
    intervals.sort()
    
    ##If the list of intervals is of length == 1
    if len(intervals) == 1:
        print(intervals)
    
    n = len(intervals)
    ans = [intervals[0]]
    for i in range(1, n):

        #If intervals are non overlapping 
        if intervals[i][0] > ans[-1][1]:
            ans.append(intervals[i])

        ##If two intervals overlap
        else:
            new = [min(intervals[i][0], ans[-1][0]), max(intervals[i][1], ans[-1][1])]
            ans.pop()
            ans.append(new)
            
    return ans 


##Driver code Function Calling
intervals = [[1,3],[2,6],[8,10],[15,18]]
result = merge_intervals(intervals)
print(result)
