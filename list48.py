# Write a Python program to print a nested lists
# (each list on a new line) using the print() function


nested_lists = [[540], [540, 986], [540, 986, 21],
                [540, 986, 21, 263], [540, 986, 21, 263, 556],
                [540, 986, 21, 263, 556, 689],
                [540, 986, 21, 263, 556, 689, 908],
                [540, 986, 21, 263, 556, 689, 908, 421],
                [540, 986, 21, 263, 556, 689, 908, 421, 469],
                [540, 986, 21, 263, 556, 689, 908, 421, 469, 536],
                [986], [986, 21], [986, 21, 263],
                [986, 21, 263, 556], [986, 21, 263, 556, 689]]

for i in nested_lists:
    print(i)
