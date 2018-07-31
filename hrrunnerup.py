

arr = [5,7,3,10,10,6,7,9,10]
mini = arr[0]
maxi = arr[0]
for i in arr:
    if i<mini:
        mini = i;
    elif i > maxi:
        maxi = i


runnerup = mini
arr.sort()

for k in arr:
    if k > runnerup and k< maxi:
        runnerup = k

print (runnerup)
