WHITE = 'w'
BLACK = 'b'

hexGrid = dict()

hexDirs = {"e":(1,0), "w":(-1,0), "ne":(1,-1),  "nw":(0,-1), "se":(0,1), "sw":(-1,1)}

def addNeighborsToGrid(tileCoords: tuple):
  q, r  = tileCoords
  for dirs in hexDirs.values():
    dq, dr = dirs
    neighbor =  (q + dq, r + dr)
    if not neighbor in hexGrid:
      hexGrid[neighbor] = WHITE

with open('input.txt') as fp:
  line = fp.readline().strip()
  while line:
    steps = []
    q, r = 0, 0
    i = 0
    while i < len(line):
      ch = line[i]
      if ch == 'n' or ch == 's':
        steps.append(f'{ch}{line[i+1]}')
        i += 1
      else:
        steps.append(ch)
      i += 1

    for step in steps:
      hDir = hexDirs[step]
      q += hDir[0]
      r += hDir[1]
    
    if (q, r) in hexGrid and hexGrid[(q, r)] == BLACK:
      hexGrid[(q, r)] = WHITE 
    else:
      hexGrid[(q, r)] = BLACK 

    addNeighborsToGrid((q, r))
    line = fp.readline().strip()

print(f'Part 1\n{len([t for t in hexGrid.values() if t == BLACK])}')

# Part 2
for i in range(100):
  tilesToFlip = dict()
  for (q, r), color in hexGrid.items():
    numBlack = 0
    for dirs in hexDirs.values():
      dq, dr = dirs
      neighbor =  (q + dq, r + dr)
      if neighbor in hexGrid and hexGrid[neighbor] == BLACK:
          numBlack += 1
    if color == BLACK and (numBlack == 0 or numBlack > 2):
      tilesToFlip[(q, r)] = WHITE
    elif color == WHITE and numBlack == 2:
      tilesToFlip[(q, r)] = BLACK

  for (q, r), color in tilesToFlip.items():
    hexGrid[(q, r)] = color
    addNeighborsToGrid((q, r))

print(f'\nPart 2\n{len([t for t in hexGrid.values() if t == BLACK])}')