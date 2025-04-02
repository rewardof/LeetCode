"""
6. Zigzag Conversion
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:  # Edge case: If only one row, return original string
            return s

        arr = [""] * numRows
        row = 0  # Start at the first row
        step = 1  # Direction: +1 (down), -1 (up)

        for char in s:
            arr[row] += char  # Add character to the current row

            # Change direction at the top or bottom row
            if row == 0:
                step = 1  # Move down
            elif row == numRows - 1:
                step = -1  # Move up

            # Move to the next row
            row += step

        return "".join(arr)


s = "PAYPALISHIRING"
numRows = 3
print(Solution().convert(s, numRows))
