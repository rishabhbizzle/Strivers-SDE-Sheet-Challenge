class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows = len(matrix)
        cols = len(matrix[0])

        s = 0
        e = (rows*cols) - 1

        while s<= e:
            mid = (s+e)//2
            element = matrix[mid//cols][mid%cols]

            if element == target:
                return True
            elif element > target:
                e = mid - 1
            else:
                s = mid + 1
        return False