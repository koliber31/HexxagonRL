from Move import Move

moveArr = [] # List of moves that pawn can make
moveArr.append(Move(-11,1)) # Filling arr of moves with all possible moves
moveArr.append(Move(-10,1))
moveArr.append(Move(-1,1))
moveArr.append(Move(1,1))
moveArr.append(Move(10,1))
moveArr.append(Move(11,1))
moveArr.append(Move(-22,2))
moveArr.append(Move(-21,2))
moveArr.append(Move(-20,2))
moveArr.append(Move(-12,2))
moveArr.append(Move(-9,2))
moveArr.append(Move(-2,2))
moveArr.append(Move(2,2))
moveArr.append(Move(9,2))
moveArr.append(Move(12,2))
moveArr.append(Move(20,2))
moveArr.append(Move(21,2))
moveArr.append(Move(22,2))
moveArr.append(Move(0,0)) # move on the same tile 

tile_color = ['white', 'green', 'red']