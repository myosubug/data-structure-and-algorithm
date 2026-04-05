class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row, col = len(image), len(image[0])
        original_color = image[sr][sc]
        if original_color == color:
            return image
        self.helper(sr, sc, original_color, color, row, col, image)

        return image

    def helper(self, i, j, original_color, new_color, row, col, image):
        if not(0 <= i < row) or not(0 <= j < col) or image[i][j] != original_color:
            return
        
        image[i][j] = new_color

        for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:
            self.helper(i+dx, j+dy, original_color, new_color,row, col, image)