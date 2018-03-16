str=raw_input("Enter string:")
char=0
word=1
for i in str:
      char=char+1
      if(i==' '):
            word=word+1
print("Number of words in the string:")
print(word)
print("Number of characters in the string:")
print(char)
