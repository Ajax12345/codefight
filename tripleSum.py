x = 15
the_list = [14, 1, 2, 3, 8, 15, 3]
flag = False
for i in the_list:
    if i in the_list:
        the_list.remove(i)
    for b in the_list:
        if b in the_list:
            the_list.remove(b)
        first = i+b
        second = x-first

        if second in the_list:
            flag = True

        the_list = [2, 3, 1]


print flag
