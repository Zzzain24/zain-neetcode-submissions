class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for r in range(len(board)):
            seen.clear()
            for c in range(len(board)):
                val = board[r][c]
                if val != ".":
                    if val in seen:
                        return False
                    seen.add(val)
        for c in range(len(board)):
            seen.clear()
            for r in range(len(board)):
                val = board[r][c]
                if val != ".":
                    if val in seen:
                        return False
                    seen.add(val)
        for r in range(0, len(board), 3):
            for c in range(0, len(board), 3):
                seen.clear()
                for i in range(3):
                    for j in range(3):
                        val = board[r + i][c + j]
                        if val != ".":
                            if val in seen:
                                return False
                            seen.add(val)
        return True 

        
