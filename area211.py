import math
def minHeight(area,base):
  return math.ceil((2*area)/base)
  area=8
  base=4
  height=minHeight(area,base)
  print("Minimum height is %d"%(height))
