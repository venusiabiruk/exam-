num = input("enter a  sequence of a number:")
seq = list(num)
s = input("enter a number to be searched:")
j = 0
while j < len(seq):
    for i in seq:
        if i == s:
            print("found")
            print(j)
        j += 1


