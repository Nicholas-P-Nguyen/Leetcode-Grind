def exist(board: list[list[str]], word: str) -> bool:
    rows = len(board)
    cols = len(board[0])
    path = set()

    def dfs(i, j, currentIndex):
        # Base case
        if currentIndex == len(word):
            return True
        
        # Make sure we're in bounds 
        # Make sure the current character matches the word
        # Make sure we're not reusing the same character
        if (i < 0 or i >= rows or 
            j < 0 or j >= cols or
            board[i][j] != word[currentIndex] or
            (i, j) in path):
            return False
        
        # Add to path if word[currentIndex] matches the board
        path.add((i, j))

        # Check up, down, right, left for the next correct character
        output = (dfs(i + 1, j, currentIndex + 1) or
                  dfs(i - 1, j, currentIndex + 1) or
                  dfs(i, j + 1, currentIndex + 1) or
                  dfs(i, j - 1, currentIndex + 1))
        
        # Remove everything in the path set recursively 
        path.remove((i, j))
        return output
    
    for i in range(rows):
        for j in range(cols):
            if dfs(i, j, 0):
                return True
        
    return False
        

exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")