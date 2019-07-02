


list1 = [("John", ("Physics", 80)), ("Daniel", ("Science", 90)), ("John",("Science", 95)),
         ("Mark",("Maths", 100)), ("Daniel", ("History", 75)), ("Mark", ("Social", 95))]
dict = {}

for i in list1:
    if i[0] not in dict:
        dict[i[0]] = list()
        dict[i[0]].append(i[1])
    else:
        dict[i[0]].append(i[1])

for i in dict:
    print(i,":", sorted(dict[i]))




