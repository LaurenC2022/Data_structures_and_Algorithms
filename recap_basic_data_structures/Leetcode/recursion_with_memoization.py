# Brute force solution using recursion
# Problem: https://leetcode.com/problems/out-of-boundary-paths/submissions/1452994644/

class Solution(object):
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        """
        :type m: int
        :type n: int
        :type maxMove: int
        :type startRow: int
        :type startColumn: int
        :rtype: int
        """
        # example: 
        # m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
        # Initial postions (0, 0)
        # Moves: 2 
        # Matrix: 
        # [[0, 0], 
        # [0, 0]] 
        # Video help: https://youtu.be/Bg5CLRqtNmk?si=vq9Hq1hYkP1bHrgu 
        # 
        #                       (0, 0)
        #                 /   |      \     \
        #             (0, -1)(1, 0) (0, 1)(-1, 0)
        #               Out  /|\\   /| \ \   Out
        #     (1,-1)(2,0)(0,0)(1,1)(0,0)(1,1)(0,2)(-1,1)
        #       Out  Out                      Out   Out
        #
        # for startingRow or startingColumn == 0, then the list is out of range
        # for startingRow or startingColumn < 0, then the list is out of range
        
# Example usage:
result = Solution().findPaths(2, 2, 2, 0, 0)  # Expected output: 6
print(result)
