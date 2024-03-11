
def deint(lst):
  outlist = []
  for i in lst:
    p = str(i)
    outlist.append(p)
  return outlist
    

def zeromaker(count):
  out = ""
  for j in range(count):
    out += "0"
  return out
    
  
def biglistmaker(length,wronglst):
  outputlst = []
  highest = 10**length
  interval = highest//100
  for i in range(highest):
    if i % interval == 0:
      print('making list:', i/interval, '%')
      
    b = str(i)
    if len(b) < length:
      b = zeromaker(length-len(b)) + b
    add = True
    for j in wronglst:
      if j in b:
        add = False
        break
    if add:
      outputlst.append(b)
  return outputlst

def wronggetter(right,all):
  wrongs = []
  for i in all:
    if i not in right:
      wrongs.append(i)

  return wrongs
def rightkeychecker(rightlst,lst):
  outlst = []
  for i in lst:
    keep = True
    for j in rightlst:
      if j not in i:
        keep = False
    if keep:
      outlst.append(i)
  return outlst
      

def runner():
  length = int(input('length:'))
  charactersCount = int(input('keysused:'))
  rightlst=[]
  alldig=['0','1','2','3','4','5','6','7','8','9']
  
  
  for i in range(charactersCount):
    rightlst.append(alldig[i])
  wronglst = wronggetter(rightlst, alldig)
  
  biglst = biglistmaker(length,wronglst)
  #print(biglst)
  
  lst3 = rightkeychecker(rightlst,biglst)
  
  print(len(lst3))
  
  g = str(input('show list?'))
  if g == "y":
    print(lst3)



def main():
  g = True
  while g:
    runner()
    if str(input('end? enter to skip'))=='end':
      g = False

main()