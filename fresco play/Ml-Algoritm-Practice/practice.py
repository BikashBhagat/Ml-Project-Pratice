arr= [10,12,15,11,19]
def findmax(arr):
    if len(arr)==1:
        return arr
    maxi= max(arr)
    maxind= arr.index(maxi) 
    if maxind != len(arr)-1:
        arr[len(arr)-1], arr[maxind] =  arr[maxind],arr[len(arr)-1]
        return arr
    else:      
        maxi= arr.pop()
        findmax(arr)
        return arr+[maxi]
arr = findmax(arr)  
sum = 0 
for i in arr:
    sum += i*(arr.index(i)+1)    
print(sum,arr)
