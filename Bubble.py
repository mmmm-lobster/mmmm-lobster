from typing_extensions import Doc
import random

def rlst():
  newlist = []
  for i in range(0, 10):   
    print(i)
    newlist.append(random.randint(1,50))
  return(newlist)
print(rlst())
def bubble(Badlist):
  inleng = len(Badlist) - 1
  sorted = False
  while not sorted:
   sorted = True
   for i in range(0, inleng):
    if Badlist[i] > Badlist[i+1]:
      sorted = False 
      Badlist[i],Badlist[i+1] = Badlist[i+1],Badlist[i]
      print(Badlist)
  return Badlist
print(bubble(rlst()))