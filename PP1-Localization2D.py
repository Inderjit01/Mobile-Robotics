colors = [['red', 'green', 'green',   'red', 'red'],
          ['red',   'red', 'green',   'red', 'red'],
          ['red',   'red', 'green', 'green', 'red'],
          ['red',   'red',   'red',   'red', 'red']]

measurements = ['green', 'green', 'green' ,'green', 'green']

p = [[1./20, 1./20, 1./20, 1./20, 1./20],
     [1./20, 1./20, 1./20, 1./20, 1./20],
     [1./20, 1./20, 1./20, 1./20, 1./20],
     [1./20, 1./20, 1./20, 1./20, 1./20]]

# Motion encoding
# [0,0] - no move
# [0,1] - move right
# [0,-1] - move left
# [1,0] - move down
# [-1,0] - move up

motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

sensor_right = 0.7

p_move = 0.8

def show(p):
    for i in range(len(p)):
        print (p[i])

#Do not delete this comment!
#Do not use any import statements.
#Adding or changing any code above may
#cause the assignment to be graded incorrectly.

#Enter your code here:

pHit = 0.7
pMiss = 0.3

pExact = 0.8
pOff = 0.2

def sense(p, Z):
    q=[]
    r = []
    rows, cols = 4,5
    for i in range(4):
        col = []
        for j in range(5):
            hit = (Z == colors[i][j])
            col.append(p[i][j] * (hit * pHit + (1-hit) * pMiss))
        q.append(col)
        r.append(sum(q[i])) # storing the sum of each column in r
    s = sum(r)
    for i in range(len(q)):
        for j in range(len(q[i])):
            q[i][j] = q[i][j] / s
    return q

def move(p, U):
    if(U==[0,0]):
        return p
    q = []
    for i in range(4):
        row = []
        for j in range(5):
            s = pExact * p[(i-U[0])%4][(j-U[1])%5]
            s = s + pOff * p[i][j]
            row.append(s)
        q.append(row)
    return q

for i in range(len(measurements)):
    p = move (p, motions[i])
    p = sense(p, measurements[i])

#Your probability array must be printed
#with the following code.

show(p)
