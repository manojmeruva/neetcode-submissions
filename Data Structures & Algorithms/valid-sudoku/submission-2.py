class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    c19 = self.checkin1x9(board,i,j)
                    if c19 == False:
                        return False
                    c91 = self.checkin9x1(board,i,j)
                    
                    if c91 == False:
                        return False
                    
                    r, c = (i // 3) * 3, (j // 3) * 3
                    c33 = self.checkin3x3(board, r, c)
                    if  c33 == False:
                        return False
        return True
    
    def checkin3x3(self,board,start,end):
        i=0
        s = set()
        while i < 3 and start+i<len(board):
            j=0
            while j<3 and end+j<len(board[0]):
                
                if board[start+i][end+j] in s:
                    return False
                if board[start+i][end+j] != ".":
                    s.add(board[start+i][end+j])
                j+=1
            i+=1
        
        return True
    
    def checkin1x9(self,board,start,end):
        s = set()
        # Check column end
        for r in range(len(board)):
            if board[r][end] != ".":
                if board[r][end] in s:
                    return False
                s.add(board[r][end])
        return True
    
    def checkin9x1(self,board,start,end):
        s = set()
        # Check row start
        for c in range(len(board[0])):
            if board[start][c] != ".":
                if board[start][c] in s:
                    return False
                s.add(board[start][c])
            end+=1

