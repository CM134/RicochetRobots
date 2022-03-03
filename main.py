# %%
# from importlib.resources import path
from ricochet import Ricochet


b1 = Ricochet(10)
print(b1.board)
print(b1.yellow)
print('\n')
# b1.yellow["row"] = 0
# b1.yellow["col"] = 1
# b1.board[0, :] = "S"
print(b1.availableMoves(b1.yellow))
print("")
b1.move(b1.yellow,'UP')
print(b1.board)
