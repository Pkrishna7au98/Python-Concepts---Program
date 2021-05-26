def sort(list):
    for i in range(len(list)-2):
        mp = i
        for j in range(i,7):
            if list[j] < list[mp]:
                mp=j
        list[mp],list[i]  = list[i], list[mp]

list = [9,4,3,2,8,7,6]
sort(list)
print(list)