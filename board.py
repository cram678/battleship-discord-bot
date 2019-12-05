playerI_defense = [["0" for _ in range(10)] for _ in range(10)]
playerI_attack = [["0" for _ in range(10)] for _ in range(10)]
playerII_defense = [["0" for _ in range(10)] for _ in range(5)]
playerII_attack = [["0" for _ in range(10)] for _ in range(10)]


def hit(x,y,b):
  b[y][x]="x"

def miss(x,y,b):
  b[y][x]="/"

def ship(x,y,b):
  b[y][x]="+"
