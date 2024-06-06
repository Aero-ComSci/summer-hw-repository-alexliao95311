# Leetcode #529: Minesweeper
Algorithm: depth-first search

You are given an m x n char matrix board representing the game board where:

- 'M' represents an unrevealed mine,
- 'E' represents an unrevealed empty square,
- 'B' represents a revealed blank square that has no adjacent mines (i.e., above, below, left, right, and all 4 diagonals),
-  digit ('1' to '8') represents how many mines are adjacent to this revealed square, and
- 'X' represents a revealed mine.
You are also given an integer array click where click = [clickr, clickc] represents the next click position among all the unrevealed squares ('M' or 'E').

Return the board after revealing this position according to the following rules:

1. If a mine 'M' is revealed, then the game is over. You should change it to 'X'.
2. If an empty square 'E' with no adjacent mines is revealed, then change it to a revealed blank 'B' and all of its adjacent unrevealed squares should be revealed recursively.
3. If an empty square 'E' with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
4. Return the board when no more squares will be revealed.

**Example 1:**

Input: board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], click = [3,0]\
Output: [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]

**Example 2:**

Input: board = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]], click = [1,2]\
Output: [["B","1","E","1","B"],["B","1","X","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]

# Algorithm Explanation

**[DFS](https://en.wikipedia.org/wiki/Depth-first_search)** is an algorithm that traverses through a tree/graph-like structure where it extends as far as possible before backtracking. 
In other words: it goes to the deepest end, then goes back and tries other forks. \
![image](https://github.com/Aero-ComSci/summer-hw-repository-alexliao95311/assets/79109757/e60a8bb9-f7a4-47e2-bd0d-913744c62e5e)

Time complexity: `O(V+E)` where V is the number of vertices and E is the number of edges
Space complexity: `O(V)` (for a recursive implementation like this one)


Code line-by-line breakdown (inside dfs function):
1. define `m` as row length and `n` as column length
2. check if `i`, `j` pointers are within bounds and the current cell `board[i][j]` isn't empty
3. list of directions: north, south, east, west, northeast, northwest, southeast, southwest (not ordered)
4. `adj_mines` is a counter for the amount of adjacent mines the cell has (defined with 0)
5. iterates through all directions
	6. update `i` and `j` counters to make them move in current durection
	7. check if new cell is in bounds and has a mine: if yes, then we add 1 to our `adj_mines` counter
8. check if there are no adjacent mines to the current empty cell: 
	9. if yes, then this cell is set with `B`
	10. otherwise, set the current cell to be the number from 1~8 (`adj_mines`)
11. We dfs through all 8 adjecent directions:
	12. iterate through all 8 directions and update the `i` and `j` counters
	13. recursively call the `dfs` function

Outside of the `dfs` function:
1. Take care of edgecase: no board
2. Get first `i` and `j` counter from `click`
3. If the current cell is an unrevealed mine:
	4. reveal the mine
	5. game over: return the board

Lastly, call the dfs function and return the board.
```py
class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        def dfs(board, i, j):
            m, n = len(board), len(board[0])
            if i<0 or j<0 or i>=m or j>=n or board[i][j] != 'E':
                return

            directions = [(-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0)]

            adj_mines = 0

            for d in directions:
                di, dj = i + d[0], j + d[1]
                if 0 <= di < m and 0 <= dj < n and board[di][dj] == 'M':        
                    adj_mines += 1

            if adj_mines == 0:
                board[i][j] = 'B'
            else:
                board[i][j] = str(adj_mines)
                return

            for d in directions:
                di, dj = i + d[0], j + d[1]
                dfs(board, di, dj)
                    
        if not board:
            return []
        i, j = click[0], click[1]

        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board

        dfs(board, i, j)
        return board
```
