from operator import itemgetter

grades = []
for i in range(int(input())):
    name = input()
    score = float(input())
    grades.append([name,score])

grades.sort()

grades.sort(key=lambda x: x[1])
lowest = []
minu = grades[0][1]




for i in range(len(grades)):
    if(grades[i][1]!=minu):
        lowest.append(grades[i])

minu = lowest[0][1]



for i in range(len(lowest)):
    if(lowest[i][1] == minu):
        print(str(lowest[i][0]))
