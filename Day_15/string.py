s = "hackkerahd"
list = []
count = {}
unique_list = []
for i in s:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
        list.append(i)
for i in list:
    if count[i] ==1:
        unique_list.append(i)
unique_list.sort()
print(s.index(unique_list[0]))
    