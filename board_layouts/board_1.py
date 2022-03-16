import numpy as np


SIZE = 16

board = np.zeros((SIZE, SIZE), dtype=object)
board[:, :] = '0'
# Assign hardcorded walls
board[0,:] = 'N'
board[-1,:] = 'S'
board[:,0] = 'W'
board[:,-1] = 'E'
board[0,0]= 'NW'
board[0,-1]= 'NE'
board[-1,-1]= 'SE'
board[-1,0]= 'SW'
board[0,5]+= 'E'
board[0,11]+= 'E'
board[1,9]= 'SE'
board[2,3] = 'NW'
board[2,-1]+= 'S'
board[3,0] += 'S'
board[3,5] = 'SW'
board[3,11]= 'SW'
board[4,2] = 'NE'
board[5,4] = 'SE'
board[5,14]= 'NW'
board[6,10]= 'NE'
board[7,7] = 'NW'
board[7,8] = 'NE'
board[7,13]= 'SW'
board[8,7] = 'SW'
board[8,8] = 'SE'
board[9,3] = 'NE'
board[9,12]= 'NW'
board[9,15] += 'S'
board[10,10]= 'SE'
board[11,6]= 'NW'
board[12,1]= 'SW'
board[12,14]= 'NE'
board[13,0]+= 'S'
board[14,4]= 'SE'
board[14,11]= 'SW'
board[15,6]+= 'E'
board[15,13]+= 'E'


goal_list = [{'color':'Y',  'num':1,  'row':1,   'col':9},
             {'color':'Y',  'num':2,  'row':2,   'col':3},
             {'color':'Y',  'num':3,  'row':9,   'col':3},
             {'color':'Y',  'num':4,  'row':10,  'col':10},
             {'color':'B',  'num':1,  'row':3,   'col':5},
             {'color':'B',  'num':2,  'row':5,   'col':14},
             {'color':'B',  'num':3,  'row':9,   'col':12},
             {'color':'B',  'num':4,  'row':11,  'col':6},
             {'color':'R',  'num':1,  'row':3,   'col':11},
             {'color':'R',  'num':2,  'row':4,   'col':2},
             {'color':'R',  'num':3,  'row':12,  'col':14},
             {'color':'R',  'num':4,  'row':14,  'col':4},
             {'color':'G',  'num':1,  'row':5,   'col':4},
             {'color':'G',  'num':2,  'row':6,   'col':10},
             {'color':'G',  'num':3,  'row':12,  'col':1},
             {'color':'G',  'num':4,  'row':14,  'col':11},
            #  {'color':'YBRG','num':1, 'row':7,   'col':13}
             ]
             