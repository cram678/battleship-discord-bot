'''
carrier=6 spaces     x1
battleship=4 spaces    x1
submarines=3 spaces    x2
destroyer=2 spaces    x1
d=direction
s=ship
b=board
'''

carrier=6
battleship=4
submarines=3
destroyer=2

from board import ship

def place_ship(x,y,d,s,b):
  d=d.lower()
  for n in range(s):
    ship(x,y,b)
    if d=="right":
      x=x+1
      if x<0:
        print("you went off the edge try again")
        break
    elif d=="left":
      x=x-1
      if x>9:
        print("you went off the edge try again")
        break
    elif d=="down":
      y=y+1
      if y>9:
        print("you went off the edge try again")
        break
    elif d=="up":
      y=y-1
      if y<0:
        print("you went off the edge try again")
        break
    else:
      print("you went off the edge try again")
      break


def detector(x,y,b):
  global guessed
  global hit
  guessed=False
  hit=False
  z=b[y][x]
  if z=="+":
    hit=True
    guessed=False
  elif z=="x":
    hit=False
    guessed=True
  elif z=="/":
    hit=False
    guessed=True
  elif z=="0":
    hit=False
    guessed=False

