board=["-","-","-",
       "-","-","-",
       "-","-","-",]
currentPlayer="X"
winner=None
isGameRunning=True
winnerArray=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

#print the board
def printBoard(board):
    print(board[0]," | ",board[1]," | ",board[2])
    print("")
    print(board[3]," | ",board[4]," | ",board[5])
    print("")
    print(board[6]," | ",board[7]," | ",board[8])

printBoard(board)

#take the player input
def playerInput(board):
    global currentPlayer
    
    inp=int(input(f"Current player is {currentPlayer} ,Enter a number 1-9: "))
  
    if(inp>=1 and inp<=9 and board[inp-1]=="-" ):
        board[inp-1]=currentPlayer
        currentPlayer= "O" if currentPlayer=="X" else "X"
    else:
        print("Player is already in that spot!")
        
def checkForWinner(winnerArray):
    global isGameRunning
    
    for i in winnerArray:
        
        if board[i[0]]==board[i[1]]==board[i[2]]:
            
            if board[i[0]]!="-":
                
                isGameRunning=False
                
                print(f"Winner is {board[i[0]]}")
                return 
        
        else:
             isGameRunning=True;
                    
while isGameRunning:
    playerInput(board)
    printBoard(board)
    checkForWinner(winnerArray)        
#check for winner

     
#take the player input

#check for winner
