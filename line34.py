fname=input("Enter the file name:")
num_lines=0
with open(fname,'r')as f:
  for line in f:
    num_lines+=1
print(num of lines:")
print(num_lines)
