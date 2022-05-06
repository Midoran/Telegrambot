
search_dict = {1: 'a', 2: 'b', 3: 'c'}

val_2_find = 'a'

list1 = []

for i, (k, v) in enumerate(search_dict.items()):
    if v == val_2_find:
        list1.append(k)

    else:
        print("That value does not exist!")

print(list1)
