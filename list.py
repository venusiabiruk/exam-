
def deletelist(List,index):
    while index >=0 and index <= len(list):
        list.pop(index)
        return list
    else:
        print("invalid index")
list = [3, 7, 1, 9, 4]
print(deletelist(list,3))
