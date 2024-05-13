

def bubblesort(alphabet):
 for i in range(0,len(alphabet)):
  for j in range(0, len(alphabet) -1-i):
      if  alphabet[j] >  alphabet[j+1]:

        alphabet[j] , alphabet[j+1] = alphabet[j+1] , alphabet[j]
alphabet = [A,S,C,I,I]
bubblesort(alphabet)
print(alphabet)
