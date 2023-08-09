def is_palindrom(string):
    list1 = []
    list2 = []
    for sub_symbol in string:
        list1.append(sub_symbol)
    i = 0
    for i in range(0,len(list1)):
        list2.insert(i, list1[(len(list1)-1-i)])
    print (list1 == list2)
is_palindrom('dgfh')