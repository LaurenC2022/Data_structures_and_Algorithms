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
        # Base case: if out of bounds, return 1
        if startRow == m or startColumn == n or startRow < 0 or startColumn < 0:
            return 1
        
        # Base case: if no more moves left, return 0
        if maxMove == 0:
            return 0
        
        # Recursive case: explore all four possible directions (DFS)
                # 1. Move down 
        return (self.findPaths(m, n, maxMove - 1, startRow - 1, startColumn) +
                # 2. Move up
                self.findPaths(m, n, maxMove - 1, startRow + 1, startColumn) +
                # 3. Move left
                self.findPaths(m, n, maxMove - 1, startRow, startColumn - 1) +
                # 4. Move right
                self.findPaths(m, n, maxMove - 1, startRow, startColumn + 1))
        # Since this is depth first search, 
        # Video help: https://youtu.be/Urx87-NMm6c?si=HQ_qgHkRorAR_XtR
        # Through recusion each path is explored until the base case is reached all stack frames are popped off
        # and the result is returned 
        # (0, 0), maxMove == 2: (-1, 0) (1, 0) (0, -1) (0, 1)
                            # (-1, 0), maxMove == 1: return 1 because -1 < 0 
                            # (1, 0), maxMove == 1: (0, 0) (2, 0) (1, -1)(0, 1)
                                                # (0, 0), maxMove == 0: max moves == 0 :. return 0
                                                # (2, 0), maxMove == 0: return 1 because startrow == m
                                                # (1, -1), maxMove == 0: return 1 because startColumn < 0
                                                # (0, 1), maxMove == 0: max moves == 0 :. return 0
                            # (0, -1), maxMove == 1: return 1 because -1 < 0
                            # (0, 1), maxMove == 1: (-1, 1) (1, 1) (0, 0) (0, 2)
                                                # (-1, 1), maxMove == 0: return 1 because startRow < 0
                                                # (1, 1), maxMove == 0: max moves == 0 :. return 0
                                                # (0, 0), maxMove == 0: max moves == 0 :. return 0
                                                # (0, 2), maxMove == 0: return 1 because startColumn == n
                            


# Example usage:
result = Solution().findPaths(2, 2, 2, 0, 0)  # Expected output: 6
print(result)
