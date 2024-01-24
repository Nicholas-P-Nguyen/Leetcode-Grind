def stringSearch(matrix: list[list[int]], words: list[int]):
    rows = len(matrix)
    cols = len(matrix[0])
    validWords = {}

    for word in words:
        validWords[word] = 0
    
    def dfs(i, j, currentIndex):
        if currentIndex == len(word):
            return True
        
        if (i < 0 or i >= rows or
            j < 0 or j >= cols or
            matrix[i][j] != matrix[currentIndex]):
            return False
        
        


stringSearch((['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']), ['ABCCED', 'SEE', 'ADEE'])
    