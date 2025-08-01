class Solution:
    def __init__(self):
        self.rows = [set() for _ in range(9)]
        self.cols = [set() for _ in range(9)]
        self.boxes = [set() for _ in range(9)]

    def print_board(self, board: List[List[str]]) -> None:
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("-" * 21)
            row = ""
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    row += "| "
                row += (board[i][j] if board[i][j] != "." else ".") + " "
            print(row.strip())
        print("\n")

    def get_box_index(self, row: int, col: int) -> int:
        return (row // 3) * 3 + (col // 3)

    def solveSudoku(self, board: List[List[str]]) -> None:
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    self.rows[i].add(num)
                    self.cols[j].add(num)
                    self.boxes[self.get_box_index(i, j)].add(num)

        def BT(i, j):
            if i == 9:
                return True

            if j == 9:
                return BT(i + 1, 0)

            if board[i][j] != ".":
                return BT(i, j + 1)

            for k in range(1, 10):
                num = str(k)
                box_index = self.get_box_index(i, j)
                if num not in self.rows[i] and num not in self.cols[j] and num not in self.boxes[box_index]:
                    board[i][j] = num
                    self.rows[i].add(num)
                    self.cols[j].add(num)
                    self.boxes[box_index].add(num)

                    # self.print_board(board)
                    # print("-----------------------------------------------")

                    if BT(i, j + 1):
                        return True

                    # Backtrack
                    board[i][j] = "."
                    self.rows[i].remove(num)
                    self.cols[j].remove(num)
                    self.boxes[box_index].remove(num)

            return False

        BT(0, 0)