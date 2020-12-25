from collections import deque

inputStr = "952438716"
cupsLst = [int(n) for n in list(inputStr)]

# Part 1
def part1():
  cups = deque(cupsLst) # rotated so 1st element is current 

  def rotateCups(target, final=True):
    while cups[0] != target:
      cups.rotate(-1) 
    if final: cups.rotate(-1) 

  for i in range(100):
    currCup = cups[0]
    destCup = currCup - 1 
    if destCup < 1:
      destCup += len(cupsLst)

    cups.rotate(-1) # rotate to get picked up 

    pickedUp = (cups.popleft(), cups.popleft(), cups.popleft()) # get picked up 

    while destCup in pickedUp:
      destCup += (-1 if destCup > 1 else len(cupsLst)-1) # update dest

    rotateCups(destCup) # move head to destCup
    
    cups.extend(list(pickedUp)) # place picked up next to dest

    rotateCups(currCup) # move head back to currCup

  rotateCups(1, False) # arrange cups from 1
  cups.popleft() # remove 1

  print(f'Part 1\n{"".join([str(n) for n in cups])}')

# Part 2
class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def __str__(self):
    return f'{self.value}'

def part2():
  llist = dict()

  # Build initial linked list
  prev = None
  for i in cupsLst:
      node = Node(i)
      llist[i] = node
      if prev != None:
          prev.right = node
          node.left = prev
      prev = node

  # Add cups up to 1 million
  for i in range(len(cupsLst)+1, 1_000_001):
      node = Node(i)
      llist[i] = node
      if prev != None:
          prev.right = node
          node.left = prev
      prev = node

  # Create circular link
  head = llist[cupsLst[0]]
  prev.right = head
  head.left = prev

  curr = llist[cupsLst[0]]
  for i in range(10_000_000):
      cup1, cup2, cup3 = curr.right, curr.right.right, curr.right.right.right # Pick up 3 cups

      # Remove picked up cups from circle
      curr.right = cup3.right
      curr.right.left = curr

      # Select destination cup
      destValue = curr.value - 1 or len(llist)
      while destValue in (cup1.value, cup2.value, cup3.value):
          destValue = destValue - 1 or len(llist)

      destNode = llist[destValue]

      # Place picked up cups next to destination cup
      cup3.right = destNode.right
      cup3.right.left = cup3
      destNode.right = cup1
      cup1.left = destNode

      curr = curr.right # Advance current cup

  while curr.value != 1:
      curr = curr.right

  print(f'\nPart 2\n{curr.right.value * curr.right.right.value}')
  
part1()
part2()