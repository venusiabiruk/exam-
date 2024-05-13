def mergsort(arr):
 if len(arr) > 1:
  mid = len(arr)//2
  left = arr[:mid]
  right = arr[mid:]
  mergsort(left)
  mergsort(right)
  i = 0
  j = 0
  k= 0
  while i < len(left) and j < len(right):
   if left[i] < right[j]:
    arr[k] =  left[i]
    i +=1
    k +=1
   else:
    arr[k] = right[j]
    j +=1
    k+=1
  while i < len(left):
   arr[k] = left[i]
   i +=1
   k+=1
  while j < len(right):
   arr[k] = right[j]
   j+=1
   k+=1
arr = [5,4,6,1 ,2,3,7,6,9,8]
mergsort(arr)
print(arr)