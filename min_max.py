#!python

nested_list = [['cherry', 7], ['apple',100], ['anaconda', 1360]]

# uses weight as key for calculating max or min
def weight(x):
    return x[1]

print(max(nested_list, key=weight))

print(min(nested_list, key=weight))
