class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        dups = set()
        for r in range(len(board)):
            dups.clear()
            for c in range(len(board)):
                if board[r][c].isalnum():
                    if int(board[r][c]) in dups:
                        return False
                    dups.add(int(board[r][c]))
        dups.clear()
        # check cols
        for c in range(len(board)):
            dups.clear()
            for r in range(len(board)):
                if board[r][c].isalnum():
                    if int(board[r][c]) in dups:
                        return False
                    dups.add(int(board[r][c]))
        dups.clear()
        # check sub-boxes
        for r in range(0, len(board), 3):
            for c in range(0, len(board), 3):
                dups.clear()
                for i in range(3):
                    for j in range(3):
                        if board[r + i][c + j].isalnum():
                            if int(board[r + i][c + j]) in dups:
                                return False
                            dups.add(int(board[r + i][c + j]))
        return True