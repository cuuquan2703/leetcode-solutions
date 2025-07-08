class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def BT(i,j,k):
            if k==len(word):
                return True

            if i<0 or i>=rows or j<0 or j >= cols or board[i][j] != word[k]:
                return False
            
            temp = board[i][j]
            board[i][j] = '#'

            found = (
                BT(i+1, j, k+1) or
                BT(i-1, j, k+1) or
                BT(i, j+1, k+1) or
                BT(i, j-1, k+1)
            )

            board[i][j] = temp
            return found

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:  # optional optimization
                    if BT(i, j, 0):
                        return True
        
        return False