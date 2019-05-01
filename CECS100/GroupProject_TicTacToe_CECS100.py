import random

def print_board(board):
    rowString= ["|","x","|","x","|","x","|"]
    for x in range(3):
        row= board[x]
        for i in range(3):
            value=str(row[i])
            rowString[(2*i)+1]=value
        print ("".join(rowString))
        
def inputPlayerLetter():
    # Lets the player type which letter they want to be.
    # Returns a list with the player's letter as the first item, and the computer's letter as the second.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O? player1    ')
        letter = input().upper()

    # The first element in the list is the player1 letter, the second is the player2 letter.
    if letter == 'X':
        return ('X','O') #NOTE: you were returning a list before and then referring it to it as a tuple
                        # firstplayer,secondplayer = inputplayerletter only works if inputplayerletter is a tuple
    else:
        return ('O','X')

def whoGoesFirst():
    # Randomly choose the player who goes first.
    if random.randint(0,1) == 0:
        return 'player2'
    else:
        return 'player1'

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def isWinner(board,letter):
    winCombos= [[(0,0),(0,1),(0,2)],[(1,0),(1,1),(1,2)],[(2,0),(2,1),(2,2)],[(0,0),(1,0),(2,0)],[(0,1),(1,1),(2,1)],[(0,2),(1,2),(2,2)],[(0,0),(1,1),(2,2)],[(0,2),(1,1),(2,0)]]
    

    for combo in winCombos:
        #print combo
        #checkR= combo[0][0]
        #checkC= combo[0][1]
        winningCombo=0
        checkR,checkC = combo[0] #(0,0)
        checkCharacter= board[checkR][checkC]
        for i in range(len(combo)):
            r,c= combo[i]
            if checkCharacter == board[r][c] and checkCharacter != "*":
                winningCombo +=1
        if winningCombo ==3:
            return True
                
    return False
    

def getPlayerMove(board,turn,letter):
    
    
    moveMade= False
    while not moveMade:
        print('Select row and column(make sure to use parenthesis and the comma!!): (r,c)', turn)
        move=input()
        possibleEntries= ['0','1','2']
        if move[1] in possibleEntries and move[3] in possibleEntries:
    
            r= (int(move[1])) #fix this for errors in the input
            c= (int(move[3]))
            
        else:
            print ("That is not a valid move! Please try again. (Make sure to put the parentheses!!)")
            move= input('Select row and column: (r,c)   ')
            while move[1] not in possibleEntries and move[3] not in possibleEntries:
                print ("That is not a valid move! Please try again. (Make sure to put the parentheses!!)")
                move= input('Select row and column: (r,c)   ')
            r= (int(move[1]))
            c= (int(move[3]))
            
                
        if r in range(3) and c in range(3):
                
            #print (letter)
            if board[r][c]== '*':
                board[r][c]= letter
                moveMade= True
            else:
                print('invalid move, space taken!')
    return
    



#main module
def main():
    print('Welcome to Tic Tac Toe!')
    count = 0
    while True:
    # Reset the board
    
        board= []
        for i in range(3):
            board.append(['*','*','*'])
        
        playerLetter1,playerLetter2 = inputPlayerLetter()
        turn = whoGoesFirst()
        print('The ' + turn + ' will go first.')
        gameIsPlaying = True
    

        while gameIsPlaying:
            if turn == 'player1':
            # Player's turn.
                print_board(board)
                move = getPlayerMove(board,turn,playerLetter1)
            
                count +=1
                if isWinner(board,playerLetter1)== True:
                    print_board(board)
                    print('Hooray! You have won the game!', turn)
                    gameIsPlaying = False
                elif count ==9:
                    print_board(board)
                    print ('No winner :( ')
                    gameIsPlaying = False
                else:
                    turn = 'player2'

            else:
            # Player's turn.
                print_board(board)
                move = getPlayerMove(board,turn,playerLetter2)
            
                count +=1
                if isWinner(board,playerLetter2)== True:
                    print_board(board)
                    print('Hooray! You have won the game!', turn)
                    gameIsPlaying = False
                elif count ==9:
                    print_board(board)
                    print ('No winner :( ')
                    gameIsPlaying = False
                else:
                    turn = 'player1'

        if not playAgain():
            break
main()
