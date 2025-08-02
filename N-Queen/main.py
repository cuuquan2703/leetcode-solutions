class Solution:
    def is_valid(self, queens, row, col):
        for r in range(row):
            c = queens[r]
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True

    def form_board(self, queens, n):
        return [
            ''.join('Q' if c == col else '.' for c in range(n))
            for col in queens
        ]

    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = []

        if n==1:
            return [["Q"]]

        def BT(row, queens):
            if row == n:
                res.append(self.form_board(queens, n))
                return

            for col in range(n):
                if self.is_valid(queens, row, col):
                    BT(row + 1, queens + [col])


        BT(0, [])
        return res