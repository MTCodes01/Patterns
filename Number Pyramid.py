from math import floor
n = int(input("Enter a number: "))
Dict = {}
for i in range(1,n*2,2):
    lst1 = [i]
    num = floor(i/2)
    if i != 1:
        for j in range(1,num+1):
            lst1.insert(0,i-j)
            lst1.append(i-j)
    Dict[num] = lst1
for i,lst in Dict.items():
    print(" "*(len(Dict)*3-i*2),end=" ")
    for j in lst:
        print(j,end=" ")
    print()