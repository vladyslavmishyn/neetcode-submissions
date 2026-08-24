class Solution:
    def isThereDuplicates(self, numbers: List[List[int]]) -> bool:
        for i in range(len(numbers)):
            nums = []

            for n in numbers[i]:
                if n != 0:
                    nums.append(n)

            if len(nums) != len(set(nums)):
                return True

        return False

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        numbers = []
        columns = []
        squares = []

        # normalize board
        for row in board:
            row_cleared = []

            for cell in row:
                if cell == ".":
                    row_cleared.append(0)
                else:
                    row_cleared.append(int(cell))

            numbers.append(row_cleared)

        # check rows
        has_duplicates_rows = self.isThereDuplicates(numbers)

        # check columns
        for c in range(9):
            column = []

            for n in range(9):
                row = numbers[n]
                column.append(row[c])

            columns.append(column)

        has_duplicates_columns = self.isThereDuplicates(columns)

        # check squares
        for start_row in range(0, 9, 3):
            for start_column in range(0, 9, 3):
                square = []

                for row in range(start_row, start_row + 3):
                    for col in range(start_column, start_column + 3):
                        square.append(numbers[row][col])

                squares.append(square)

        has_duplicates_squares = self.isThereDuplicates(squares)

        if (
            has_duplicates_columns
            or has_duplicates_rows
            or has_duplicates_squares
        ):
            return False
        else:
            return True