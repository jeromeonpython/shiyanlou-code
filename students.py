name = []
kemu =['physic','english','math']
data = {}
n = int(input("Enter the students num.:"))

for i in range(0,n):
    maket = []
    names = input("Enter the name of student {}".format(i+1))
    for km in kemu:
        maket.append(int(input("Enter the score of {}".format(km))))
    data[names] = maket

for x,y in data.items():
    total = sum(y)
    print(x,"'s total marks ",total)
    if total >= 120:
        print("student {} is passed".format(x))
    else:
        print("student {} failed".format(x))
